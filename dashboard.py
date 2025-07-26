import streamlit as st
from pymongo import MongoClient
import pandas as pd

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")  # Adjust if hosted remotely
db = client["resume_db"]
collection = db["resumes"]

# Fetch all documents from MongoDB
resumes = list(collection.find())

# Convert to DataFrame for easy viewing
if resumes:
    df = pd.DataFrame(resumes)

    # Drop the MongoDB object ID for display
    if "_id" in df.columns:
        df.drop(columns=["_id"], inplace=True)

    # Streamlit dashboard UI
    st.title("📄 Resume Parser Dashboard")
    st.write("Below is the parsed resume data fetched from MongoDB.")

    # Filter by skill
    if "Skills" in df.columns:
        all_skills = sorted(set(skill for sublist in df["Skills"] if isinstance(sublist, list) for skill in sublist))
        selected_skills = st.multiselect("Filter by Skills", all_skills)

        if selected_skills:
            df = df[df["Skills"].apply(lambda skills: all(skill in skills for skill in selected_skills) if isinstance(skills, list) else False)]

    # Display DataFrame
    st.dataframe(df)
else:
    st.warning("No data found in MongoDB. Please run the parser first.")