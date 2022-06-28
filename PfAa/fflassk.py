from flask import Flask,render_template

skills_app = Flask(__name__ ) 

@skills_app.route("/")
def home():
    return render_template("home.html",pagetitle="Homepage" , custom_css="home" )


@skills_app.route("/about")
def about():
    return render_template("about.html", pagetitle="About Us" ,  custom_css="about")




@skills_app.route("/contact-us")
def countact():
    return render_template("countact-us.html", pagetitle="cotact us" ,custom_css="countact" )

@skills_app.route("/terms")
def terms():
  return render_template("terms.html", pagetitle="terms" , custom_css="terms_and_Privacy" )

@skills_app.route("/Privacy")
def Privacy():
  return render_template("Privacy.html", pagetitle="Privacy" , custom_css="terms_and_Privacy" )


  

if __name__ == "__main__": 
  skills_app.run(debug=True, port=9000) 