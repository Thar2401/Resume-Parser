Face Movement & Eye Tracking Detector

Project Description

This project is a real-time face movement detection system that uses Dlib and OpenCV to track facial landmarks. It detects:

	•	Head tilt (left/right)
 
	•	Head movement (left/right)
 
	•	Eyeball movement
 
	•	General face movement

This can be used for attention tracking, security applications, and gesture recognition.

Features

	•	Detects head tilt based on eye alignment
 
	•	Detects head turns using nose position
 
	•	Detects eyeball movement based on relative eye landmark shifts
 
	•	Alerts when movement exceeds a threshold


How It Works

	1.	The script captures video frames from the webcam.
 
	2.	It uses Dlib’s face detector to find a face in the frame.
 
	3.	The shape predictor model detects 68 facial landmarks.
 
	4.	Movement detection is performed by analyzing landmark changes.
 
	5.	If significant movement is detected, an alert message is displayed.


References

	•	Dlib Library
 
	•	OpenCV Documentation
 
	•	NumPy Docs

Feel free to fork the repository and submit pull requests. Contributions are welcome.

This project is open-source under the MIT License.
