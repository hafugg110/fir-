from flaskr import db, bcrypt, login

from flask_login import UserMixin


class UserRegister(UserMixin, db.Model):
    """記錄使用者資料的資料表"""
    __tablename__ = 'UserRegister'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return 'name:%s, username:%s, email:%s' % (self.name, self.username, self.email)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(
            password).decode('utf8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


    @login.user_loader
    def load_user(user_id):
        return UserRegister.query.get(int(user_id))
