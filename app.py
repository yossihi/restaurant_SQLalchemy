from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, request, session, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = '24'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mj47TWMJ@localhost/restaurants'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Models
class Restaurant(db.Model):
    recepies = db.Column(db.String(100),nullable=False)
    ingridients = db.Column(db.String(100))
    prepering_time = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), unique=True)
    password = db.Column(db.String(1000))

#routes
@app.route("/")
def main():
    my_restaurants = Restaurant.query.all()
    return render_template("index.html", my_restaurants=my_restaurants)
    

@app.route('/add', methods=['GET', 'POST'])
def add_rest():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        recepies = request.form['recepies']
        ingridients = request.form['ingridients']
        prepering_time = request.form['prepering_time']
        
        new_rest = Restaurant(recepies=recepies, ingridients=ingridients, prepering_time=prepering_time)
        
        db.session.add(new_rest)
        db.session.commit()

        flash('Restaurant added successfully', 'success')
        return redirect(url_for('main'))
    return render_template('add_rest.html')


@app.route('/edit/<int:restaurant_id>', methods=['GET', 'POST'])
def edit_restaurant(restaurant_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    restaurant = Restaurant.query.get_or_404(restaurant_id)

    if request.method == 'POST':
        restaurant.recepies = request.form['recepies']
        restaurant.ingridients = request.form['ingridients']
        restaurant.prepering_time = request.form['prepering_time']

        db.session.commit()

        flash('Restaurant updated successfully', 'success')
        return redirect(url_for('main'))

    return render_template('edit_rest.html', restaurant=restaurant)

@app.route('/delete/<int:restaurant_id>', methods=['POST'])
def delete_restaurant(restaurant_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    restaurant = Restaurant.query.get_or_404(restaurant_id)
    db.session.delete(restaurant)
    db.session.commit()

    flash('Restaurant deleted successfully', 'success')
    return redirect(url_for('main'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['logged_in'] = True
            flash('Logged in successfully', 'success')
            return redirect(url_for('main'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        hashed_password = generate_password_hash(password)
        
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('main'))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)