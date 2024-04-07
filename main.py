from flask import Flask, url_for, request
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/index')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/profile/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


@app.route('/login_req', methods=['GET', 'POST'])
def login_req():
    if request.method == 'POST':
        return 'Login from req'
    else:
        return 'Show Login from req'
    

@app.get('/login_get')
def login_get():
    return 'login_get()'

@app.post('/login_post')
def login_post():
    return 'login_post()'