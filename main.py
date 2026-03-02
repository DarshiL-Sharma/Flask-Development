from flask import Flask
import random

app = Flask(__name__)
print(random.__name__)
print(__name__)




@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello,World!</h1>'\
            '<p>This is the para </p>'\
            '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTJ2YXlqdnhsMW9uZmc5bGpnZnZ1M3VjOHA1NGl4NGRoOGp5ZXV3ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QveTUJwyl3KeSEUR6X/giphy.gif"width=500px>'

@app.route('/bye')
def bye():
    return 'Hey'

@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f"Hello! {name}, you are {number}"
