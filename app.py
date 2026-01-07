from flask import Flask,render_template,request,redirect,session
from flask_sqlalchemy  import SQLAlchemy
from flask_session import Session


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sports.db"
db=SQLAlchemy(app)
app.config['SESSION_TYPE'] = 'filesystem'
app.config["SESSION_PERMANENET"]=False
Session(app)
app.secret_key="secret-key"


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

@app.route("/",methods=["GET","POST"]) 
def login():
    if request.method=="POST":
        name=request.form.get("name")
        session["name"]=name
        return redirect("/home")
    return render_template("login.html")
@app.route("/logout")
def logout():
    if request.method=="POST":
        session.clear()
        return redirect("/")
    return render_template("logout.html")


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