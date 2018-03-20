import sqlite3 as sql

def insert_users(username, password):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES(?, ?)",(username, password))
        con.commit()

def insert_data(triptitle, destination, creator, friend):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO trips (triptitle, destination, creator, friend) VALUES(?, ?, ?, ?)",(triptitle, destination, creator, friend))
        con.commit()

def insert_friends(triptitle, destination):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO trips (triptitle, destination) VALUES(?, ?)",(triptitle, destination))
        con.commit()


def retrieve_trips(currentuser):
    # SQL statement to query database goes here
    with sql.connect("app.db") as con:

    	# this makes it so that everything is a row
    	con.row_factory = sql.Row
    	cur = con.cursor()
    	# get all the results and assign it to a variable
    	# no need to commit because you're just fetching data. not changing anything
        # trips MATCH 'creator:'"+currentuser+"' AND friend:'"+currentuser+"''
    	result = cur.execute("SELECT * FROM trips WHERE trips.creator == '"+currentuser+"' OR trips.friend == '"+currentuser+"'").fetchall()
    	print (result)
    return result

def fetch_friends(currentuser):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute("SELECT username FROM users WHERE username != '"+currentuser+"'")
        return cur.fetchall()

# def retrieve_orders():
#     # SQL statement to query database goes here
#     with sql.connect("app.db") as con:

#     	# this makes it so that everything is a row
#     	con.row_factory = sql.Row
#     	cur = con.cursor()
#     	# get all the results and assign it to a variable
#     	# no need to commit because you're just fetching data. not changing anything
#     	result = cur.execute("select * from orders"). fetchall()
#     	print (result)
#     return result

# def insert_orders(name_of_part, manufacturer_of_part, customer_id):
#     with sql.connect("app.db") as con:
#     	cur = con.cursor()
#     	cur.execute("INSERT INTO orders (name_of_part, manufacturer_of_part, customer_id) VALUES(?, ?, ?)",(name_of_part, manufacturer_of_part, customer_id))
#     	con.commit()
#     	return cur.lastrowid
# ##You might have additional functions to access the database

# def insert_customers_orders(customer_id,order_id):
#     # SQL statement to insert into database goes here
#     with sql.connect("app.db") as con:
#         cur = con.cursor()
#         cur.execute("INSERT INTO orders_customers (customer_id, order_id) VALUES (?,?)", (customer_id, order_id))
#         con.commit()


# def insert_data(first_name, last_name, company, email, phone, street_address, city, state, country, zip_code):
#     # SQL statement to insert into database goes here
#     with sql.connect("app.db") as con:
#       cur = con.cursor()
#       cur.execute("INSERT INTO customers (first_name, last_name, company, email, phone) VALUES(?, ?, ?, ?, ?)",(first_name, last_name, company, email, phone))
#       cur.execute("INSERT INTO address (street_address, city, state, country, zip_code) VALUES(?, ?, ?, ?, ?)",(street_address, city, state, country, zip_code))
#       con.commit()

# def checkuser(username, password):
#     with sql.connect("app.db") as con:
#         cur = con.cursor()
#         error = None
#     try:
#         cur.execute("SELECT COUNT(1) FROM users WHERE username = 'ass'")

#         if not cur.fetchone()[0]:
#             raise ServerError('Invalid username')

#             cur.execute("SELECT password FROM users WHERE username = 'ass'")

#             for row in cur.fetchall():
#                 if password == row[0]:
#                     session['username'] = request.form['username']
#                     session['password'] = request.form['password']
#                     return redirect(url_for('index'))

#             raise ServerError('Invalid password')
#     except ServerError as e:
#         error = str(e)

#     return render_template('login.html', error=error)
