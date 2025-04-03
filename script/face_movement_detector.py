import cv2
import dlib
import numpy as np

# Load Dlib's face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('/Users/tharunsmac/Downloads/shape_predictor_68_face_landmarks.dat')

# Initialize webcam
cap = cv2.VideoCapture(0)

# Store the previous position of the face and eyes
prev_landmarks = None
prev_eye_positions = None
movement_threshold = 2  # Lower threshold for more sensitivity
movement_history = []  # Store recent movement values for smoothing
history_length = 10  # Number of frames to consider for smoothing

def calculate_movement(landmarks, prev_landmarks):
    """Calculate the Euclidean distance between current and previous landmarks."""
    if prev_landmarks is None:
        return 0
    
    movement = np.linalg.norm(np.array(landmarks) - np.array(prev_landmarks), axis=1)
    avg_movement = np.mean(movement)  # Compute the average movement across all landmarks
    return avg_movement

def calculate_head_tilt(landmarks):
    """Calculate the angle of head tilt using eye and nose landmarks."""
    left_eye = np.mean(landmarks[36:42], axis=0)  # Average position of left eye landmarks
    right_eye = np.mean(landmarks[42:48], axis=0)  # Average position of right eye landmarks
    nose_tip = landmarks[30]  # Nose tip landmark

    # Calculate the angle between the eyes and the nose
    eye_line = right_eye - left_eye
    angle = np.arctan2(eye_line[1], eye_line[0]) * (180 / np.pi)
    return angle

def calculate_head_turn(landmarks):
    """Calculate the horizontal displacement to detect head turns."""
    left_eye = np.mean(landmarks[36:42], axis=0)  # Average position of left eye landmarks
    right_eye = np.mean(landmarks[42:48], axis=0)  # Average position of right eye landmarks
    nose_tip = landmarks[30]  # Nose tip landmark

    # Calculate the horizontal displacement of the nose relative to the eyes
    eye_center = (left_eye + right_eye) / 2
    horizontal_displacement = nose_tip[0] - eye_center[0]

    return horizontal_displacement

def detect_eyeball_movement(landmarks, prev_eye_positions):
    """Detect eyeball movement based on the relative positions of eye landmarks."""
    if prev_eye_positions is None:
        return False

    left_eye = landmarks[36:42]  # Left eye landmarks
    right_eye = landmarks[42:48]  # Right eye landmarks

    # Calculate the average position of the eyes
    current_eye_positions = {
        "left": np.mean(left_eye, axis=0),
        "right": np.mean(right_eye, axis=0)
    }

    # Calculate the movement of the eyes
    left_eye_movement = np.linalg.norm(current_eye_positions["left"] - prev_eye_positions["left"])
    right_eye_movement = np.linalg.norm(current_eye_positions["right"] - prev_eye_positions["right"])

    # Threshold for detecting significant eyeball movement
    eye_movement_threshold = 2  # Adjust as needed
    if left_eye_movement > eye_movement_threshold or right_eye_movement > eye_movement_threshold:
        return True

    return False

def smooth_movement(movement, history, length):
    """Smooth the movement using a moving average."""
    history.append(movement)
    if len(history) > length:
        history.pop(0)
    return np.mean(history)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)
        landmarks_points = [(p.x, p.y) for p in landmarks.parts()]

        # Calculate movement between frames
        movement = calculate_movement(landmarks_points, prev_landmarks)
        smoothed_movement = smooth_movement(movement, movement_history, history_length)

        # Calculate head tilt angle
        head_tilt_angle = calculate_head_tilt(landmarks_points)

        # Calculate head turn
        head_turn_displacement = calculate_head_turn(landmarks_points)

        # Detect eyeball movement
        eyeball_movement_detected = detect_eyeball_movement(landmarks_points, prev_eye_positions)

        # Draw face bounding box
        x, y, w, h = (face.left(), face.top(), face.width(), face.height())
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Draw landmarks
        for (x, y) in landmarks_points:
            cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)

        # Alert if movement, tilt, turn, or eyeball movement is detected
        dynamic_threshold = movement_threshold + np.std(movement_history)  # Dynamic threshold
        if smoothed_movement > dynamic_threshold or abs(head_tilt_angle) > 15 or abs(head_turn_displacement) > 20 or eyeball_movement_detected:  # Adjust thresholds as needed
            cv2.putText(frame, "Warning: Movement Detected!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        # Update previous landmarks and eye positions
        prev_landmarks = landmarks_points
        prev_eye_positions = {
            "left": np.mean(landmarks_points[36:42], axis=0),
            "right": np.mean(landmarks_points[42:48], axis=0)
        }

    # Display video feed
    cv2.imshow("Face Movement Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
