import fitz  # PyMuPDF for PDF processing
import spacy
import re
import docx
from pymongo import MongoClient

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_entities(text):
    doc = nlp(text)
    entities = {ent.label_: ent.text for ent in doc.ents}

    corrected_entities = {
        "Name": re.search(r"([A-Z][a-z]+ [A-Z][a-z]+)", text),
        "Email": re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text),
        "Phone": re.search(r"\+?\d[\d\s\-]{9,}", text),
        "Skills": re.findall(r"\b(Python|Java|C\+\+|Machine Learning|Deep Learning|Data Science|NLP|SQL|HTML|CSS|JavaScript)\b", text, re.IGNORECASE),
        "Projects": [entities[k] for k in entities if k in ["WORK_OF_ART", "PRODUCT"]],
        "Experience": [entities[k] for k in entities if k == "ORG"],
        "Location": entities.get("GPE", "N/A"),
        "Education": entities.get("DATE", "N/A")
    }

    for key, value in corrected_entities.items():
        if isinstance(value, re.Match):
            corrected_entities[key] = value.group()

    return corrected_entities

def save_to_mongo(data):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["resume_db"]
    collection = db["resumes"]
    collection.insert_one(data)
    #print("Data inserted into MongoDB.")

if __name__ == "__main__":
    file_path = "RESUME.docx"  # or "RESUME.pdf"

    if file_path.endswith(".pdf"):
        extracted_text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        extracted_text = extract_text_from_docx(file_path)
    else:
        print("Unsupported file format")
        exit()

    parsed_data = extract_entities(extracted_text)
    print("Extracted Resume Data:")
    print(parsed_data)

    save_to_mongo(parsed_data)