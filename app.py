from flask import Flask, render_template,request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('feedback.html')
@app.route('/save',methods=['POST'])
def save():
    name = request.form['name']
    message = request.form['message']
    with open("submissions.txt","a") as file:
        file.write(f"{datetime.now()} | Name: {name} | Message: {message}\n")
    return f"Thanks {name}, your feedback has been saved!"

if __name__=='__main__':
    app.run(debug=True)