from flask import Flask, url_for, request, render_template, redirect, abort, session, escape

app = Flask(__name__)

#Set secret key to some random bytes. keep this really secret
app.secret_key = "xyz##$msa"
@app.route('/')
def hello_world():
    return "Hello world"

# @app.route('/hello')
# def hello():
#     return "hi watu wa kenya"

#variable rules
#@app.route('/user/<username>')
#def show_user_profile(username):
    # show the user profile for that user
    #return "User %s" % username  

@app.route('/post/<int:post_id>')
def show_post(post_id):
# show the post with the given id, the id is an integer
    return "post %d" % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return "Subpath %s" % subpath

@app.route('/projects/')
def projects():
    return "The Project Page"

@app.route('/about')
def about():
    return "The about page"

# @app.route('/')
# def index():
#     return "index"

# @app.route('/login')
# def login():
#     return "login"

@app.route('/user/<username>')
def profile(username):
    return "{}\'s profile".format(username)

with app.test_request_context():
    print(url_for('index'))
    # print(url_for('login'))
    # print(url_for('login', next='/'))
    print(url_for('profile', username='Alex korir'))


#HTTP Methods
# @app.route('/login', methods=['GET', 'POST' ])
# def login():
#     if request.method == 'POST':
#         return "do_the_login()"
#     else:
#         return "get_login_form()"

#render templates
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

#context locals 
with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    #end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'

#redirects and errors
@app.route('/redirect')
def one():
    return redirect(url_for('logout'))

# @app.route('/logout')
# def logout():
#     abort(401)
#     this_is_never_executed()

@app.route('/')
def index():
    if "username" in session:
        return "logged in as %s" % escape(session["username"])
    return "you are not logged in"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return
            #  <form method ="post">
            #     <p><input type=text name=username>
            #     <p><input type=submit value=Login>
            #   </form> 
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('profile'))
