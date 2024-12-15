import functools
import os
import sqlite3
from flask import Flask, request, render_template, redirect, url_for, session
import pickle
import numpy as np  # Import numpy for prediction

app = Flask(__name__)
app.secret_key = '1234'
model = pickle.load(open('model/SepsisRF.sav', 'rb'))
model_severe = pickle.load(open('model/SevereRF.sav', 'rb'))
model_shock = pickle.load(open('model/Shock.sav', 'rb'))

# Define the path to the SQLite database file
DATABASE_PATH = 'user.db'  # Replace 'user.db' with the desired database file path

# Function to create the 'users' table
@app.route('/')
def root():
    return redirect(url_for('login'))
def create_users_table():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Create the 'users' table
#create_users_table()

# Fetch valid users from SQLite database
def get_valid_users():
    create_users_table()
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM users")
    users = {username: password for username, password in cursor.fetchall()}
    conn.close()
    return users

valid_users = get_valid_users()

# Decorator function to check if the user is logged in
def login_required(route_function):
    @functools.wraps(route_function)
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return route_function(*args, **kwargs)
    return wrapper

@app.route('/home')
@login_required
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    valid_users = get_valid_users()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in valid_users and valid_users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html', error='')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    create_users_table()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    if prediction[0] == 1:
        output = "the sepsis symptoms detected"
        return redirect(url_for('sever_sepsis'))
    else:
        output = "its normal"
    return render_template('index.html', prediction_text='This given details show {}'.format(output))

@app.route('/sever_sepsis', methods=['GET', 'POST'])
@login_required
def sever_sepsis():
    return render_template('SEVERE_SEPSIS.html')

@app.route('/predict1', methods=['GET', 'POST'])
@login_required
def predict1():
    int_severe = [float(x) for x in request.form.values()]
    final_severe = [np.array(int_severe)]
    prediction_severe = model_severe.predict(final_severe)
    if prediction_severe[0] == 2:
        output1 = 'that severe sepsis symptoms have been detected'
        return redirect(url_for('shock'))
    else:
        output1 = 'only sepsis symptoms'
    return render_template('SEVERE_SEPSIS.html', prediction_severe='This given details show {}'.format(output1))

@app.route('/shock', methods=['GET', 'POST'])
@login_required
def shock():
    return render_template('SHOCK.html')

@app.route('/predict2', methods=['GET', 'POST'])
@login_required
def predict2():
    int_shock = [float(x) for x in request.form.values()]
    final_shock = [np.array(int_shock)]
    prediction_shock = model_shock.predict(final_shock)
    if prediction_shock[0] == 3:
        output2 = 'Septic Shock may occur.'
    else:
        output2 = 'that there are no chances for septic shock'
    return render_template('SHOCK.html', prediction_severe='This given details show {}'.format(output2))


if __name__ == "__main__":
    app.run(debug=True)
