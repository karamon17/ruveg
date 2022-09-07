
from unicodedata import category
from flask import Flask, render_template, url_for, redirect, request, flash, session, abort
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jflaskfdjaksfjlasfkjlk832kj3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reciept.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)


user_reciepts = db.Table('user_reciepts', 
    db.Column('recipe_id', db.Integer, db.ForeignKey('reciept.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)

class Reciept(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    ref = db.Column(db.String(500))
    ingridients = db.Column(db.Text)
    recipe = db.Column(db.Text)
    ref_pic = db.Column(db.String(500))
    category = db.Column(db.String(500))
    author = db.Column(db.String(500))

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(500))
    pas = db.Column(db.String(500))
    reciepts = db.relationship('Reciept', secondary=user_reciepts, backref='users')


'''def __repr__(self):
     return '<%r>' % self.id'''

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        ingridient0 = request.form["ingridient"]
        reciept = Reciept.query.filter(Reciept.title.like(f"%{ingridient0}%") | Reciept.ingridients.like(f"%{ingridient0}%") 
            | Reciept.title.like(f"%{str.capitalize(ingridient0)}%") | Reciept.ingridients.like(f"%{str.capitalize(ingridient0)}%")
            | Reciept.title.like(f"%{str.upper(ingridient0)}%") | Reciept.ingridients.like(f"%{str.upper(ingridient0)}%")).all()  
        dlina = len(reciept)
        return render_template("search.html", reciept=reciept, ingridient0=ingridient0, dlina=dlina)
    else:
        reciept = Reciept.query.all()
        dlina = len(reciept)
        #print(dlina) #{{dlina}}
        return render_template("index.html", reciept=reciept, dlina=dlina)


@app.route("/about")
def about():
    return render_template("about.html")    


@app.route("/sauces")
def sauces():
    category = 'Соусы'
    reciept = Reciept.query.filter(Reciept.category.like('соус')).all()
    dlina = len(reciept)
    return render_template("category.html", reciept=reciept, category=category, dlina=dlina)   


@app.route("/dishes")
def dishes():
    category = 'Горячие блюда'
    reciept = Reciept.query.filter(Reciept.category.like('второе')).all()
    dlina = len(reciept)
    return render_template("category.html", reciept=reciept, category=category, dlina=dlina)     


@app.route("/drinks")
def drinks():
    category = 'Напитки'
    reciept = Reciept.query.filter(Reciept.category.like('напитки')).all()
    dlina = len(reciept)
    return render_template("category.html", reciept=reciept, category=category, dlina=dlina)   


@app.route("/soup")
def soup():
    category = 'Супы'
    reciept = Reciept.query.filter(Reciept.category.like('суп')).all()
    dlina = len(reciept)
    return render_template("category.html", reciept=reciept, category=category, dlina=dlina)   


@app.route("/snacks")
def snacks():
    category = 'Закуски'
    reciept = Reciept.query.filter(Reciept.category.like('закуска')).all()
    dlina = len(reciept)
    return render_template("category.html", reciept=reciept, category=category, dlina=dlina)   


@app.route("/salads")
def salads():
    category = 'Салаты'
    reciept = Reciept.query.filter(Reciept.category.like('салат')).all()
    dlina = len(reciept)
    return render_template("category.html", reciept=reciept, category=category, dlina=dlina)     


@app.route("/desserts")
def desserts():
    category = 'Десерты'
    reciept = Reciept.query.filter(Reciept.category.like('десерт')).all()
    dlina = len(reciept)
    return render_template("category.html", reciept=reciept, category=category, dlina=dlina)       


@app.route("/bakery")
def bakery():
    category = 'Выпечка'
    reciept = Reciept.query.filter(Reciept.category.like('выпечка')).all()
    dlina = len(reciept)
    return render_template("category.html", reciept=reciept, category=category, dlina=dlina)


@app.route("/Михаил Веган")
def mikhail():
    category = 'Рецепты Михаила Вегана'
    reciept = Reciept.query.filter(Reciept.author.like('Михаил Веган')).all()
    dlina = len(reciept)
    return render_template("category.html", reciept=reciept, category=category, dlina=dlina)


@app.route("/Vegan Family")
def VeganFamily():
    category = 'Рецепты Vegan Family'
    reciept = Reciept.query.filter(Reciept.author.like('Vegan Family')).all()
    dlina = len(reciept)
    return render_template("category.html", reciept=reciept, category=category, dlina=dlina)         


@app.route("/Инди Синди")
def indisindi():
    category = 'Рецепты Инди Синди'
    reciept = Reciept.query.filter(Reciept.author.like('Инди Синди')).all()
    dlina = len(reciept)
    return render_template("category.html", reciept=reciept, category=category, dlina=dlina)


@app.route("/Веганская Домохозяйка")
def domohoz():
    category = 'Рецепты Веганской Домохозяйки'
    reciept = Reciept.query.filter(Reciept.author.like('Веганская Домохозяйка')).all()
    dlina = len(reciept)
    return render_template("category.html", reciept=reciept, category=category, dlina=dlina)  


@app.route("/Александра Андерссон")
def anderson():
    category = 'Рецепты Александры Андерссон'
    reciept = Reciept.query.filter(Reciept.author.like('Александра Андерссон')).all()
    dlina = len(reciept)
    return render_template("category.html", reciept=reciept, category=category, dlina=dlina)


@app.route("/Yulia Kurkuma")
def kurkuma():
    category = 'Рецепты Yulia Kurkuma'
    reciept = Reciept.query.filter(Reciept.author.like('Yulia Kurkuma')).all()
    dlina = len(reciept)
    return render_template("category.html", reciept=reciept, category=category, dlina=dlina)  


@app.route("/Веганки")
def veganki():
    category = 'Рецепты Веганки'
    reciept = Reciept.query.filter(Reciept.author.like('Веганки')).all()
    dlina = len(reciept)
    return render_template("category.html", reciept=reciept, category=category, dlina=dlina)  


@app.route("/EUGE")
def EUGE():
    category = 'Рецепты EUGE'
    reciept = Reciept.query.filter(Reciept.author.like('EUGE')).all()
    dlina = len(reciept)
    return render_template("category.html", reciept=reciept, category=category, dlina=dlina) 


@app.route("/Anastasia Solo")
def Solo():
    category = 'Рецепты Anastasia Solo'
    reciept = Reciept.query.filter(Reciept.author.like('Anastasia Solo')).all()
    dlina = len(reciept)
    return render_template("category.html", reciept=reciept, category=category, dlina=dlina)


@app.route("/login", methods=["GET", "POST"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', user=session['userLogged']))
    if request.method == 'POST':
        email = request.form["email"]
        pas = request.form["pas"]
        if email == '':
            return ("<h1>Пустой email</h1>")
        if pas == '':
            return ("<h1>Пароль пустой</h1>")
        users_db = Users.query.all()
        for i in range(len(users_db)):         
            if email == users_db[i].email and check_password_hash(users_db[i].pas, pas):
                session['userLogged'] = email
                return redirect(url_for('profile', user=session['userLogged']))            
        return ("<h1>Пароль или логин неверный</h1>")
    return render_template("login.html") 


@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()
    return redirect("/")


@app.route("/profile/<user>")    
def profile(user):
    if 'userLogged' not in session or session['userLogged'] != user:
        abort(401)
    user=session['userLogged']
    user_db = Users.query.filter_by(email = user).all()
    favorite = user_db[0].reciepts
    #print(favorite[0].title)
    return render_template("profile.html", user=user, favorite=favorite) 


@app.route("/favorite<int:id>")
def addfavorite(id):
    user=session['userLogged']
    user_db = Users.query.filter_by(email = user).all()
    #print(user_db)
    reciept_db = Reciept.query.get(id)
    #print(reciept_db)
    user_db[0].reciepts.append(reciept_db)
    db.session.commit()
    return redirect(url_for('profile', user=user))


@app.route("/favorite_del<int:id>")
def delfavorite(id):
    user=session['userLogged']
    user_db = Users.query.filter_by(email = user).all()
    #print(user_db)
    reciept_db = Reciept.query.get(id)
    #print(reciept_db)
    user_db[0].reciepts.remove(reciept_db)
    db.session.commit()
    return redirect(url_for('profile', user=user))


@app.route("/<int:id>")
def recipt(id):
    reciept = Reciept.query.get(id)
    return render_template("reciept.html", reciept=reciept, id = id)    


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        pas = request.form["pas"]
        pas1 = request.form["pas1"]
        if email == '':
            return ("<h1>Пустой email</h1>")
        if pas != pas1 or pas == '':
            return ("<h1>Пароли не совпадают</h1>")
        if pas == '':
            return ("<h1>Пароль пустой</h1>")
        hash = generate_password_hash(pas)
        user = Users(email=email, pas=hash)
        users_db = Users.query.all()
        for i in range(len(users_db)):         
            if email == users_db[i].email:
                return ("<h1>That email is already exist</h1>")
        try:
            db.session.add(user)
            db.session.commit()
            return redirect("login")
        except:
            return "Получилась ошибка"
    else:
        return render_template("register.html")


@app.errorhandler(404)
def pageNotFound(error):
    return render_template("page404.html")
