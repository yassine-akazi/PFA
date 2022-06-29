from flask import Flask,render_template, request , redirect
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__ ) 


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
db=SQLAlchemy(app)

class Contact(db.Model) : 
  id= db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(200), nullable=False)
  email = db.Column(db.String(200), nullable=False)
  message = db.Column(db.String(200), nullable=False)
  def __repr__(self):
        return "<Contact %r>" % self.id


class Formule(db.Model) : 
  id= db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(200), nullable=False)
  lastname = db.Column(db.String(200), nullable=False)
  city = db.Column(db.String(200), nullable=False)  
  email = db.Column(db.String(200), nullable=False)
  number = db.Column(db.String(200), nullable=False)
  typeblood = db.Column(db.String(200), nullable=False)
  years = db.Column(db.String(200), nullable=False)
  tattoo = db.Column(db.String(200), nullable=False)
  birth = db.Column(db.String(200), nullable=False)
  heart = db.Column(db.String(200), nullable=False)
  iron = db.Column(db.String(200), nullable=False)
  risk = db.Column(db.String(200), nullable=False)
  injected = db.Column(db.String(200), nullable=False)





  def __repr__(self):
        return "<Formule %r>" % self.id

@app.route("/")
def home():
    return render_template("home.html",pagetitle="Homepage" , custom_css="home" )


@app.route("/about")
def about():
    return render_template("about.html", pagetitle="About Us" ,  custom_css="about")



@app.route("/contact-us", methods=['POST', 'GET'] )
def contact(): 
  if(request.method == "POST"):
    form_fullname = request.form["name"]
    form_email = request.form["email"]
    form_message = request.form["message"]
    newcontact = Contact(email=form_email, name = form_fullname , message =form_message )
    db.session.add(newcontact)
    db.session.commit()
    db.session.rollback()
    return redirect('/contact-us')

  return render_template("countact-us.html", pagetitle="cotact us" ,custom_css="countact" )

@app.route("/terms")
def terms():
  return render_template("terms.html", pagetitle="terms" , custom_css="terms_and_Privacy" )

@app.route("/Privacy")
def Privacy():
  return render_template("Privacy.html", pagetitle="Privacy" , custom_css="terms_and_Privacy" )

@app.route("/formule" ,methods=['POST', 'GET'])
def formule():
   
  if(request.method == "POST"):
    form_Firstname= request.form["firstname"]
    form_email = request.form["email"]
    form_city = request.form["city"]
    form_lastname = request.form["lastname"]
    form__number= request.form["number"]
    form_typeblood= request.form["typeblood"]
    form_years= request.form["years"]
    form_tattoo = request.form["tattoo"]
    form_birth = request.form["birth"]
    form_heart = request.form["heart"]
    form_iron = request.form["iron"]
    form_risk = request.form["risk"]
    form_injected = request.form["injected"]


    new = Formule( email = form_email , firstname = form_Firstname , city = form_city , lastname  = form_lastname ,  number = form__number ,typeblood = form_typeblood, years = form_years , tattoo = form_tattoo , birth = form_birth , heart = form_heart , iron = form_iron , risk = form_risk , injected = form_injected )
    db.session.add(new)
    db.session.commit()
    db.session.rollback()
    
    return redirect('/formule')

  return render_template("formule.html", pagetitle="formule" , custom_css="formule" )

@app.route("/congrat")
def congrats():
  return render_template("congrats.html", pagetitle="congrats" , custom_css="about" )

if __name__ == "__main__":  
  app.run(debug=True, port=9000)
