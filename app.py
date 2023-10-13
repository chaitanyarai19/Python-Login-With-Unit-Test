from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

# Dummy user data for demonstration
users = {
    'user1': 'password1',
    'user2': 'password2',
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
        return f'Welcome, {username}!'
    else:
        return 'Invalid login credentials. Try again.'

if __name__ == '__main__':
    app.run(debug=True)
