# Resume Parser using spaCy & PyMuPDF

📄 **Description**

A simple and effective resume parser that extracts relevant information such as name, email, phone number, skills, experience, education, and more from PDF or DOCX resumes using natural language processing (NLP) techniques. The extracted information is stored in a MongoDB database, and can be visualized via a connected dashboard interface.

⚙️ **Technologies Used**

- Python  
- spaCy (NLP for Named Entity Recognition)  
- PyMuPDF (fitz) (for PDF text extraction)  
- python-docx (for DOCX file parsing)  
- Regular Expressions (for custom parsing)  
- pymongo (to interact with MongoDB)  
- MongoDB (to store parsed data)

🗃️ **Project Structure**

```
resume-parser/
├── parser.py               # Main script for parsing and storing data
├── models/                 # Pretrained models (if any)
├── sample_resumes/         # Sample resumes to test
├── requirements.txt        # List of required Python packages
├── dashboard.py            # Streamlit dashboard to view parsed data
└── README.md               # Project documentation
```

🧠 **Features**

- Extracts information using NER (spaCy).  
- Supports both PDF and DOCX resumes.  
- Custom regex-based extraction for emails, phone numbers, and skills.  
- Stores parsed results in MongoDB.  
- Optional dashboard integration to display stored data (e.g., Flask/Streamlit frontend).

🚀 **Getting Started**

1. Clone the Repository  
   ```bash
   git clone https://github.com/yourusername/resume-parser.git
   cd resume-parser
   ```

2. Install Dependencies  
   Make sure you have Python 3.10+ installed. Then install the required packages:  
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Parser  
   Edit parser.py and change the file path:  
   ```python
   file_path = "/path/to/your/resume.pdf"  # or .docx
   ```  
   Then run:  
   ```bash
   python parser.py
   ```

4. View Data in MongoDB  
   Start the mongo shell:  
   ```bash
   mongosh
   ```  
   Use the database:  
   ```javascript
   use resumeDB
   ```  
   Find the data:  
   ```javascript
   db.resumes.find().pretty()
   ```

📊 **Streamlit Dashboard (Optional)**

To visualize the parsed resume data using Streamlit:

1. Make sure MongoDB is running and parser.py has already inserted data.

2. Launch the Streamlit dashboard:  
   ```bash
   streamlit run dashboard.py
   ```

3. Open the provided local URL in your browser (usually http://localhost:8501) to see the parsed resumes in a clean UI.

The dashboard will automatically fetch documents from the MongoDB collection and display them in a user-friendly layout.
