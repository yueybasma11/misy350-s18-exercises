from flask import Flask, render_template
app = Flask(__name__)

@app.route("/hello")
def user():
    import random
greeting_list = ['Ciao', 'Hei', 'Salut', 'Hola', 'Nihao']
print random.choice(greeting_list)

@app.route('/')
def index():
    return "hello Yusef Basma"
if __name__ == '__main__':
    app.run()


#@app.route("/user")
#def user():
    #return render_template("index.html")


@app.route("/form")
def form():
    return render_template("index.html")


@app.route('/users/<string:username>')
def users(username):
    #return "<h1>Hello %s<h1>" % username
    return render_template('user.html',username=username)

    if __name__ =='__main__':
        app.run()
