from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)
app.secret_key = "key"


#home page
@app.route("/survey")
def survey():
    return render_template("index.html")


#this will show the result when somthing is submited
@app.route("/results")
def results():
    return render_template("results.html")


# this route will redirect to "/survey"
@app.route("/process", methods = ["post"])
def process():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["favorite_language"] = request.form["favorite_language"]
    session["comment"] = request.form["comment"]
    return redirect("/results")


if __name__=="__main__":
    app.run( debug= True)