from crypt import methods
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, url_for,request,jsonify
import os
from forms import *
from flask_migrate import Migrate
import json
from flask_marshmallow import Marshmallow
from flask import(
Flask,g,redirect,render_template,request,session,url_for,flash,jsonify
)
from flask_cors import CORS




app=Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] =" thisismysecretkey"


db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

''''''
#login for admin
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='mills', password='password'))
users.append(User(id=2, username='likem', password='likem'))
users.append(User(id=3, username='john', password='some'))



@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

#DATABASE MODEL
#person table
class Person(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200), nullable=True, unique=True)
    gender= db.Column(db.String(10), nullable=True)
    age = db.Column(db.Integer(),nullable = True)  
    primary_phone_number= db.Column(db.Integer(),nullable = True)
    secondary_phone_number= db.Column(db.Integer(),nullable = True)
    next_of_kin= db.Column(db.String(),nullable = True)
    marital_status= db.Column(db.String(),nullable = True)
    class_designaiton= db.Column(db.String(),nullable = True)
    home_address= db.Column(db.String(),nullable = True)
    current_place_of_work= db.Column(db.String(),nullable = True)
    health_status= db.Column(db.String(),nullable = True)
    nationality= db.Column(db.String(100),nullable = True)
    picture= db.Column(db.String(),nullable = True)
    brithdate= db.Column(db.String(),nullable = True)
    guardian= db.Column(db.String(),nullable = True)
    status_doa= db.Column(db.String(),nullable = True)
    extra_curriculum_activities= db.Column(db.String(),nullable = True)
  
    def __repr__(self):
        return f"Person('{self.id}', {self.name}', {self.age})"



#yeargroup table
class YearGroup(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200), nullable=True)
    program= db.Column(db.String(200), nullable=True)
    total_number= db.Column(db.Integer(), nullable=True)
    people_completed= db.Column(db.Integer(),nullable = True)
    people_admitted= db.Column(db.Integer(),nullable = True)

    def __repr__(self):
        return f"Course('{self.id}', {self.name}',)"
    
    
    
    
#department table
class School(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200), nullable=True)
    name_of_school= db.Column(db.String(200), nullable=True)
    programs= db.Column(db.String(), nullable=True)
    total_number = db.Column(db.Integer(),nullable = True)
    
    def __repr__(self):
        return f"Course('{self.id}', {self.name}',)"
    
    
    
    
       
#programs table
class Program(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200), nullable=True)
    program_name= db.Column(db.String(200), nullable=True)
    program_department= db.Column(db.String(), nullable=True)
    program_code= db.Column(db.Integer(),nullable = True)
    
    def __repr__(self):
        return f"Course('{self.id}', {self.name}',)"



#postman  
    class ProductSchema(ma.Schema):
        class Meta:
            fields = ("id","name", "age", "gender")
    product_schema = ProductSchema()
    products_schema = ProductSchema(many =True)


#routes 
#GET and POST method is working
''''
@app.route('/',methods=['GET','POST'])
def index():
    persons=Person.query.all() 
    if request.method=='POST':
        print(request.json['name'])
        print(request.json['age'])
        print(request.json['gender'])
        newentry=Person(name=request.json['name'], age=request.json['age'], gender=request.json['gender'])
        db.session.add(newentry)
        db.session.commit()
        return redirect(url_for('base'))
    return render_template('base.html')
'''

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/newforms')
def newforms():
    form=RegistrationForm()
    if form.validate_on_submit():
        print(form.lastname.data)
    
    return render_template("newforms.html", form=form)
    

@app.route('/members')
def members():
    return render_template('members.html')

@app.route('/form')
def form():
    form=RegistrationForm()
    if form.validate_on_submit():
        print(form.lastname.data)
        print(form.Othername.data)
        print(form.Gender.data)
        print(form.BirthDate.data)
        print(form.Age.data)
        print(form.Age.data)
        print(form.Primary.data)
        print(form.Other.data)
        print(form.Relationship.data)
        print(form.Home.data)
        print(form.Current.data)
        print(form.Nationality.data)
        print(form.Guardian.data)
        print(form.Year.data)
        print(form.Marital.data)
        print(form.Health.data)
        print(form.Extra.data)
        new=Person(lastname=form.lastname.data, Othername=form.Othername.data)
        
        db.session.add(new)
        db.session.commit()
        return redirect(url_for("form"))
    return render_template("form.html", form=form)

@app.route('/information')
def information():
    name=Person.query.all()
    print(name)
    return render_template("information.html", name=name)
   # print(product_schema)
 
''''
#post method is not working.
@app.route('/product',methods=['POST'])
def products():
    persons=request.get_json()
    name=persons['name']
    age=persons['age']
    gender=persons['gender']
    
    
    newentry = Person(name=name,age=age,gender=gender)
    db.session.add(newentry)
    db.session.commit()
    
    class ProductSchema(ma.Schema):
        class Meta:
            fields = ("id","name", "age", "gender")
    product_schema = ProductSchema()
    print(product_schema)
    
    return product_schema.jsonify(newentry)
'''

#upgrade method 
@app.route("//<int:id>", methods=['PUT'])
def update(id):
    user=Person.query.get_or_404(id)
    if request.method== 'POST':
        print(user.name)
        user.name=request.form['name']
        try:
            db.session.commit()
            return redirect('/') 
        except:
            return"errrrror"
    else:
        return render_template('home.html', user=user)
    
    
    
#delete method
@app.route("//<int:id>",methods=['DELETE'])
def delete(id):
    delete=Person.query.get_or_404(id)
    try:
            db.session.delete(delete)
            db.session.commit()
            return redirect('/') 
    except: 
        return "errrrrorrr"
    

@app.route('/home',methods=['GET','POST'])
def home():
    persons=Person.query.all()  
    print(persons)
    return render_template('home.html',persons=persons)




#login routes for admin
#login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('index'))
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('profile.html' )


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host='0.0.0.0', port=8080,debug=True)
    
    
