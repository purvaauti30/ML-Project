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
    

    yp= (linreg.predict([[c1,c2,c3,c4]])[0])

    return render_template("home.html" , sales=yp)

if __name__ == "__main__" :
    app.run(debug=True)