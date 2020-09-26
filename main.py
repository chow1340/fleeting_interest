from flask import Flask, render_template, url_for, request, session, redirect
from user.UserController import user_controller, login, register


app = Flask(__name__)
app.register_blueprint(user_controller)

# TODO fix this secret key 
app.secret_key = "xd"

 
@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('logout.html', username=username)

    # return "test"
    return render_template('index.html')
    

if __name__ == '__main__':
    print("RANNNNN")
    app.secret_key = 'mysecret'
    app.run(debug=True, host='192.168.2.40')