from flask import Flask, render_template, request


app = Flask(__name__) #Create an instance of the app, in this case "app"


@app.route("/form") #define a url as a decorator, in this case "/"
def index(): #define a control function for url - in this case function returns a greeting
    return render_template('form.html') #Renders template file 'form.html' as form for user input



@app.route("/data/", methods = ['POST', 'GET']) #this control method must check to see if it is get or post method
def data():
    if request.method =='GET': 
        return render_template("form2.html") #if it is get method: tell the user to return to /form
    if request.method == 'POST':
        form_data = request.form 
        return render_template('data.html', form_data = form_data)




