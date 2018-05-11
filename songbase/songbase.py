import os
from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLAlchemy_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir,'data.sqlite')
db = SQLAlchemy(app)


#define database tables
class Artist(db.Model):
    __tablename__ ='artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)

@app.route('/artists')
def all_artists():
    artists = Artist.query.all()
    return_template('all-artists.html', artists = artists)

@app.route('/artist/edit/<int:id>')
def artist_edit(id):
    artist = Artist.query.filter_by(name="coldplay").first()
    artist.about = "this is Yusef Basma"
    db.session.commit()
    return_template('all-artists.html')
    #return "this is artist %" % id
    #return render_template('user.html',username=username)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == "GET":
        first_name = request.args.get('first_name')
        if first_name:
            return render_template('form.html', first_name=first_name)
        else:
            return render_template('form.html', first_name=session.get('first_name'))
    if request.method =="POST":
        session['first_name'] = request.form['first_name']
        return render_template('form.html',first_name = first_name)

@app.route("/user")
def user():
    return "this is the page for users"


@app.route('/users/<string:username>')
def users(username):
    #return "<h1>Hello %s<h1>" % username
    return render_template('user.html',username=username)

    if __name__ =='__main__':
        app.run()
