from flask import Flask, render_template
from datetime import datetime
import requests


app = Flask(__name__)

@app.route("/")
def home() -> str:
    current_year = datetime.now().year
    return render_template("index.html", year= current_year)

@app.route("/guess/<name>")
def guess(name: str) -> str:
    genderize_url = "https://api.genderize.io"
    agify_url = "https://api.agify.io"

    params = {
        "name": name
    }
    
    genderize_response = requests.get(genderize_url, params= params)
    gender_data = genderize_response.json()
    gender = gender_data["gender"]

    agify_response = requests.get(agify_url, params= params)
    agify_data = agify_response.json()
    age = agify_data["age"]
    return render_template("guess.html", persone_name= name, gender= gender, age= age)

@app.route("/blog")
def blog() -> str:
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template("blog.html", posts= all_posts)

if __name__ == "__main__":
    app.run(debug= True)