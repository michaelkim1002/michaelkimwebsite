from flask import Flask, render_template , redirect, url_for , send_from_directory
from flask_bootstrap import Bootstrap5
import os
import csv
application = Flask(__name__)
application.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
Bootstrap5(application)
@application.route("/")
def home():
    with open('michaelkim-portfolio.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template("index.html", projects=list_of_rows)
@application.route("/resume")
def resume():
    return render_template("resume.html")
@application.route('/download')
def download():
    return send_from_directory("static/files", "MichaelKimResume.pdf", as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    application.run(debug=False, host='0.0.0.0', port=port)