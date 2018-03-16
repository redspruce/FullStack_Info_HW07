from flask import render_template, redirect, request, session, url_for, escape
from app import app, models, db
#from .forms import CustomerForm
#from .forms import OrderForm
# Access the models file to use SQL functions
from .models import *

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
        session['username'] = request.form['username']
        session['email'] = request.form['email']
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('email', None)
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
def create_customer():
    form = CreateTrip()
    # if form is validated when user presses submit
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        first_name = form.first_name.data
        last_name = form.last_name.data
        company = form.company.data
        email = form.email.data
        phone = form.phone.data

        street_address = form.street_address.data
        city = form.city.data
        state = form.state.data
        country = form.country.data
        zip_code = form.zip_code.data
        insert_data(first_name, last_name, company, email, phone, street_address, city, state, country, zip_code)

        return redirect('/customers')
    return render_template('customer.html', form=form)

@app.route('/trips')
def display_trips():
    # Retreive data from database to display
    trips = retrieve_trips()
    return render_template('home.html',
                            trips=trips)

# @app.route('/create_order/<value>', methods=['GET', 'POST'])
# def create_order(value):
#     form = OrderForm()
#     # if form is validated when user presses submit
#     if form.validate_on_submit():
#         # Get data from the form
#         # Send data from form to Database
#         name_of_part = form.name_of_part.data
#         manufacturer_of_part = form.manufacturer_of_part.data

#         order_id = insert_orders(name_of_part, manufacturer_of_part, value)
#         insert_customers_orders(value, order_id)

#         return redirect('/customers')
#     return render_template('orders.html', form=form)
