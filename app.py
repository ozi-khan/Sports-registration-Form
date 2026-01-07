from flask import Flask,render_template,request,redirect
from flask_sqlalchemy  import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sports.db"
db=SQLAlchemy(app)

class Sports(db.Model):
    Sno=db.Column(db.Integer, primary_key=True)
    Name=db.Column(db.String, nullable=False)
    Class=db.Column(db.String, nullable=False)
    Section=db.Column(db.Integer, primary_key=False)
    College_Id=db.Column(db.Integer, primary_key=False)
    City=db.Column(db.String, nullable=False)
    Sport=db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("home.html")
@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/register")
def resitration():
    return render_template("register.html")

@app.route("/sports")
def sports():
    return render_template("sports.html")

@app.route("/participants",methods=["GET","POST"])
def participents():
    if request.method=="POST":
        Name=request.form["name"]
        Class=request.form["class"]
        Section=request.form["Section"]
        College_ID=request.form["id"]
        City=request.form["city"]
        Sport=request.form["sports"]
        mySports=Sports(Name=Name,Class=Class,Section=Section,College_Id=College_ID,City=City,Sport=Sport)
        db.session.add(mySports)
        db.session.commit() 
        return redirect("/participants")
    allsports=Sports.query.all()
    return render_template("participant.html",allsports=allsports)

if __name__=="__main__":
    app.run(debug=True)