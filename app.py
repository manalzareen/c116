#Importing flask module in the project
from flask import Flask, render_template

#Create an object of the Flask class
app = Flask(__name__)


@app.route("/")
def firstFlask():
     return "first flask program......"

@app.route("/contact")
def contactpage():
    return "contact us..."

@app.route("/index")
def first_webpage():  
    name ="manal"  
    return render_template("index.html" ,index_var=name )

#run using debug argument
app.run( debug = True)
#app.run( debug = True , port = 8000)