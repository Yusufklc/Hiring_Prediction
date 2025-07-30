from flask import Flask,render_template,request
import numpy as np
import pickle as pc

app = Flask(__name__,template_folder="Template")

model = pc.load(open("hiring.pkl","rb"))


@app.route("/")

def home():

    return render_template("frontend.html")

@app.route("/hiring",methods=["POST","GET"])

def hiring():
    if request.method == "POST":

        Interwiev = float(request.form["Interwiev"])

        skill = float(request.form["skill"])

        personal = float(request.form["person"])

        Rec = float(request.form["Rec"])


        values = np.array([[Interwiev,skill,personal,Rec]])

        result = model.predict(values)

    return render_template("frontend.html",result=result)


app.run(debug=True)

