from flask import Flask, render_template

app = Flask(__name__)#__name__ is the saved file name

@app.route("/")#
def websitedata():
    return render_template("index.html")

@app.route("/about")#
def aboutdata():
    print("got request")
    return render_template("about.html")
if __name__=="__main__":
    app.run(debug=True, port=5000)
    print("running")
