from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def dashboard():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["resume_db"]
    collection = db["resumes"]
    resumes = list(collection.find({}, {"_id": 0}))
    return render_template("dashboard.html", resumes=resumes)

if __name__ == "__main__":
    app.run(debug=True)