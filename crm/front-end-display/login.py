from flask import Flask, request, redirect, render_template, session, url_for
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong secret key

# Read all users from users.txt
def get_all_users():
    users_file = "/srv/mod2group/users.txt" #wherever the usernames are beign kept
    if not os.path.exists(users_file):
        return []
    with open(users_file, "r") as file:
        return [line.strip() for line in file]

@app.route('/')
def index():
    return render_template('login-page.html')  

@app.route('/login', methods=['POST'])
def login():
    all_users = get_all_users()
    user = request.form.get('user', '')

    #validate username
    if not user or not user.isalnum():
        return "Invalid username, try again."

    if user in all_users:
        #Admin login
        if user == "ADMIN":
            session['admin'] = True
            session['login'] = True
            session['user'] = user
            return redirect(url_for('admin_login'))

        #regular user login
        session['login'] = True
        session['user'] = user
        return redirect(url_for('files'))

    return "Not a registered user, try again."

@app.route('/admin-login')
def admin_login():
    if 'admin' in session and session['admin']:
        return "Welcome, Admin!"  #replace with admin login page rendering
    return redirect(url_for('index'))

@app.route('/files')
def files():
    if 'login' in session and session['login']:
        user = session.get('user', '')
        return f"Welcome, {user}!"  #replace with user's file page rendering
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
