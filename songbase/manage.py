from flask_script import Manager
from songbase import app, db, Artist

manager = Manager(app)

@manager.command
def deploy():
    print "database reset" #resets database, anything added is removed and anyhing that was deleted is added back
    db.drop_all()
    db.create_all()

    print "inserting initial data"
    coldplay = Artist(name="coldplay",about="this is coldplay")
    m5= Artist(name="Maroon 5", about="This is Maroon 5")

    db.session.add(coldplay)
    db.session.add(m5)

    db.session.commit()


if __name__ == '__main__':
    manager.run()
