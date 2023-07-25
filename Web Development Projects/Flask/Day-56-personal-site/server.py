from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home() -> None:
    return render_template("Lior's protfolio.html")

if __name__ == "__main__":
    app.run(debug= True)