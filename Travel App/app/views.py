from flask import render_template, redirect, request, session, url_for, escape
from app import app, models, db
#from .forms import CustomerForm
from .forms import CreateTrip
# Access the models file to use SQL functions
from .models import *
import sqlite3 as sql

# added login page
@app.route('/')
def index():
    username = ''
    if 'username' in session:
        username = escape(session['username'])
        return redirect(url_for('display_trips'))
    else:
        return render_template('login.html')

# added login page posting
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']

        with sql.connect("app.db") as con:
            cur = con.cursor()

            user = cur.execute("SELECT * FROM users WHERE username = '"+username+"'").fetchone()
            if user is not None:
                user = user[1]
            else:
                user = ''
            # if user != username:
            #     error = 'Wrong username'
            pw = cur.execute("SELECT password FROM users WHERE username = '"+username+"'").fetchone()  # if pw != password:
            #     error = 'Wrong password'
            if pw is not None:
                pw = pw[0]
            else:
                pw = ''

            if user == username and pw == password:
                session['username'] = request.form['username']
                session['password'] = password
                return redirect(url_for('index'))
            else:
                error = 'Wrong credentials'
                return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']

        insert_users(username,password)

        session['username'] = username
        session['password'] = password
        return redirect(url_for('index'))
    return render_template('signup.html')

@app.route('/create_trip', methods=['GET', 'POST'])
def create_trip():
    form = CreateTrip()

    form.friends.choices = []        
    
    for row in fetch_friends(session['username']):
        friend = str(row[0])
        form.friends.choices += [(friend, friend)]

    # if form is validated when user presses submit
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        triptitle = form.triptitle.data
        destination = form.destination.data
        creator = session['username']
        friend = form.friends.data

        insert_data(triptitle, destination, creator, friend)

        return redirect(url_for('index'))
    return render_template('trips.html', form=form)

@app.route('/trips')
def display_trips():
    # Retreive data from database to display
    username = ''
    if 'username' in session:
        trips = retrieve_trips(session['username'])
        return render_template('home.html', trips=trips)
    else:
        return render_template('login.html')


# with sql.connect("app.db") as con:
#     cur = con.cursor()
#     error = None
# try:
#     cur.execute("SELECT FROM users WHERE username = 'ass'")

#     if not cur.fetchone()[0]:
#         raise ServerError('Invalid username')

#         cur.execute("SELECT password FROM users WHERE username = 'lol'")

#         for row in cur.fetchall():
#             if password == row[0]:
#                 session['username'] = request.form['username']
#                 session['password'] = request.form['password']
#                 return redirect(url_for('index'))

#         raise ServerError('Invalid password')
# except ServerError as e:
#     error = str(e)
# return render_template('login.html', error=error)

@app.route('/remove_trip/<value>')
def remove_trip(value):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM trips WHERE trip_id = '"+value+"'")
    return redirect(url_for('index'))