from flask import Flask, render_template , redirect, url_for , send_from_directory
from flask_bootstrap import Bootstrap5
import os
import csv
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
Bootstrap5(app)
@app.route("/")
def home():
    with open('michaelkim-portfolio.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template("index.html", projects=list_of_rows)
@app.route("/resume")
def resume():
    return render_template("resume.html")
@app.route('/download')
def download():
    return send_from_directory(
        "static", path = "files/MichaelKimResume.pdf"
    )
if __name__ == "__main__":
    app.run(debug=False, port=5003)