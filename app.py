from flask import Flask, render_template, request
import pyqrcode
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_image = None
    user_url = ""
    if request.method == "POST":
        user_url = request.form["url"]
        if user_url:
            qr = pyqrcode.create(user_url)
            file_path = os.path.join("static", "qr.png")
            qr.png(file_path, scale=6)
            qr_image = file_path
    return render_template("index.html", qr_image=qr_image, user_url=user_url)

if __name__ == "__main__":
    app.run(debug=True)
