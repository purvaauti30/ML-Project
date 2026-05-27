from flask import Flask , render_template, request
import pickle
app=Flask(__name__)

with open("trainedmodel.pkl",mode="rb") as file:
    linreg=pickle.load(file)




@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pred" ,methods=["GET" , "POST"])
def prediction():
    c1=int(request.form.get("v1"))
    c2=int(request.form.get("v2"))
    c3=int(request.form.get("v3"))
    c4=int(request.form.get("v4"))
    c5=int(request.form.get("v5"))
    c6=int(request.form.get("v6"))
    c7=int(request.form.get("v7"))
    c8=int(request.form.get("v8"))
    c9=int(request.form.get("v9"))
    c10=int(request.form.get("v10"))
    c11=int(request.form.get("v11"))

    yp= (linreg.predict([[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11]])[0])

    return render_template("home.html" , sales=yp)

if __name__ == "__main__" :
    app.run(debug=True)