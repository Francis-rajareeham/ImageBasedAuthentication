from flask import Flask, request, render_template, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, current_user, login_required
import json
from PIL import Image
from flask_wtf.csrf import CSRFProtect


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mLucuZZJJV8eMM5y aAvZOvckiVkaigJL'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    csrf = CSRFProtect(app)

    from .auth import auth

    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note, random_obj, interestsimg, userinterests
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.session_protection = "strong"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))



    @app.route('/', methods=['GET','POST'])
    @login_required
    def home():
        if request.method == 'POST':
            note = request.form.get('note')
            if len(note) <1:
                flash('Note can not be empty!', category='error')
            else:
                new_note = Note(data=note, user_id=current_user.id)
                db.session.add(new_note)
                db.session.commit()
                flash('Note added successfully!', category='success')

        return render_template("home.html", user= current_user)

    @app.route('/delete-note', methods=['POST'])
    @csrf.exempt
    def delete_note():
        note = json.loads(request.data)
        noteId = note['noteId']
        note = Note.query.get(noteId)
        if note:
            if note.user_id == current_user.id:
                db.session.delete(note)
                db.session.commit()

        return jsonify({})
        
    return app

    
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Database created!')
