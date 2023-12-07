from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template ('index.html')

@app.route("/riddle1/")
def riddle1():
    return render_template('riddle1.html')

@app.route("/riddle1w/")
def riddle1w():
    return render_template('riddle1w.html')

@app.route("/success/")
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
