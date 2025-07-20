
Resume Parser

A simple resume parser built using Python that extracts essential information from resumes such as name, email, phone number, education, skills, and project experience. The application uses Natural Language Processing (NLP) techniques including Named Entity Recognition (NER) with spaCy and text extraction from PDF/DOCX files using PyMuPDF (fitz) and python-docx.

Features
	•	Extracts candidate details including:
	•	Full Name
	•	Email Address
	•	Phone Number
	•	Location
	•	Education
	•	Work Experience
	•	Skills
	•	Projects
	•	Supports both PDF and DOCX formats
	•	Custom mapping for correcting misclassified entities
	•	Easily integratable with a backend or web application

Technologies Used
	•	Python
	•	spaCy (for Named Entity Recognition)
	•	PyMuPDF (fitz) (for PDF text extraction)
	•	python-docx (for DOCX text extraction)
	•	re (regular expressions)

Installation

Clone the repository:
git clone https://github.com/your-username/resume-parser.git
cd resume-parser

Install the required Python libraries:
pip install spacy pymupdf python-docx
python -m spacy download en_core_web_sm


Project structure:

resume-parser/
│
├── parser.py               # Main script to extract information
├── sample-resume.pdf       # Sample input file (optional)
├── models/                 # (Optional) Any models or assets used
└── README.md               # This file
