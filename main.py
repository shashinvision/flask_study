from flask import Flask, url_for, request, render_template, abort, redirect, url_for
from markupsafe import escape
from werkzeug.utils import secure_filename



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


@app.route('/hello/')
@app.route('/hello/<name>')
def hello_name(name=None):
    return render_template('hello.html', name=name)


#To access parameters submitted in the URL (?key=value) you can use the args attribute:

#searchword = request.args.get('key', '')
@app.route('/login_access', methods=['POST', 'GET'])
def login_access():
    error = None
    if request.method == 'POST':
        if request.form['username'] and request.form['password']:
            return f'Nombre: {request.form["username"]}'

        else:
            error = 'Invalid username/password'
    else:
            error = 'Metodo no valido'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')




@app.route('/upload_secure', methods=['GET', 'POST'])
def upload_file_secure():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"/var/www/uploads/{secure_filename(file.filename)}")




@app.route('/index_error')
def index_error():
    return redirect(url_for('login'))

@app.route('/login_error')
def login_error():
    abort(401)
    #this_is_never_executed()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


# API 
# @app.route("/me")
# def me_api():
#     user = get_current_user()
#     return {
#         "username": user.username,
#         "theme": user.theme,
#         "image": url_for("user_image", filename=user.image),
#     }

# @app.route("/users")
# def users_api():
#     users = get_all_users()
#     return [user.to_json() for user in users]


#SESSIONS

#from flask import session

# Set the secret key to some random bytes. Keep this really secret!
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# @app.route('/')
# def index():
#     if 'username' in session:
#         return f'Logged in as {session["username"]}'
#     return 'You are not logged in'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return '''
#         <form method="post">
#             <p><input type=text name=username>
#             <p><input type=submit value=Login>
#         </form>
#     '''

# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))