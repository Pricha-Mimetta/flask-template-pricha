from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Home Page'
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    title = 'About Page'
    name = 'Pricha Mimetta'
    email = 'std.68122420109@ubru.ac.th'
    mobile = '0855183314'
    age = 50

    return render_template('about.html',title=title, name=name, 
                           email=email, mobile=mobile, age=age)

@app.route('/favorite/foods')
def favorite_foods():
    title = 'Favorite Foods Page'
    foods = ['ข้าวไข่เจียว','คะน้าหมูกรอบ','ข้าวผัด','ข้าวแกงกะหรี่หมูทอด']
    return render_template('favorite_foods.html',title=title,
                           foods=foods)

@app.route('/favorite/sports')
def favorite_sports():
    title = 'Sport Page'
    sports = ['บอลเล่','บาส','ฟุตบอล']
    return render_template('favorite_sports.html',title=title,sports=sports)