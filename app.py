from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('login.html')

@app.route('/home')
def home():
   return render_template('home.html')



@app.route('/about')
def about():
   return render_template('about.html')


if __name__ == '__main__':
   app.run(debug = True)