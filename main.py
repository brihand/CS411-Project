
from flask import Flask, redirect, url_for, render_template, request
from flask_cors import CORS
from APIcall import getQuotes 

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins': 'http://localhost:8080',
    "allow_headers":"Access-Control-Allow-Origin"}})


@app.route("/", methods = ["POST", "GET"])
def search():
    if request.method == "POST":
        user = request.form["q"]
        name = user.lower()
        return redirect(url_for("success", name = name))
    else:
      return render_template("index.html")


@app.route("/success/<name>", methods = ["GET"])
def success(name):
    data =  getQuotes(name)
    return render_template("search.html", data = data)
    #return "you searched for %s" %name



if __name__ == "__main__":
    app.run(debug=True)
