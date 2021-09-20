from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__) #Create an instance of the app, in this case "app"



@app.route("/meme") #define a url as a decorator, in this case "/"
def who():
    return redirect(url_for('greet')) 

@app.route("/hi/<username>") #define a url as a decorator, in this case "/hi/<username>". The <> around username allows it to be passed to control function as parameter
def greeting(username): #Control function recieves username from url to use in greeting
    return f"Hello, {username}!"

@app.route("/jimbo/hello")
def greet():
    return "Hello me boy"


@app.route("/form") #define a url as a decorator, in this case "/"
def index(): #define a control function for url - in this case function returns a greeting
    return render_template('form.html')



@app.route("/data/", methods = ['POST', 'GET'])
def data():
    if request.method =='GET':
        return "Go to /form to submit data."
    if request.method == 'POST':
        form_data = request.form 
        return render_template('data.html', form_data = form_data)




