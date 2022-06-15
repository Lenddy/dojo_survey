from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)

app.secret_key = "key"
#home page
@app.route("/servey")
def survey():
    return render_template("index.html")


#this will show the result when somthing is submited
@app.route("/results")
def resuls():
    return render_template("results.html")


# this route will redirect to "/servey"
@app.route("/process", methods = ["post"])
def process():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["favorite_language"] = request.form["favorite_language"]
    session["comment"] = request.form["comment"]
    return redirect("/results")


if __name__=="__main__":
    app.run( debug= True)