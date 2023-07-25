from flask import Flask, render_template
import requests
from post import Post

BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"
blog_response = requests.get(BLOG_URL)
posts = blog_response.json()

post_objects: list[object] = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)
    
app = Flask(__name__)

@app.route('/')
def home() -> str:
    return render_template("index.html", posts= post_objects)

@app.route("/post/<int:blog_num>")
def get_post(blog_num: int) -> str:
    requested_post = None
    for post in post_objects:
        if post.id == blog_num:
            requested_post = post
            return render_template("post.html", post= requested_post)

if __name__ == "__main__":
    app.run(debug=True)
