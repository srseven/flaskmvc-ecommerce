from flask_wtf import Form
from wtforms import TextField, SubmitField, validators, PasswordField
from wtforms.validators import DataRequired
from models import Customer
# Set your classes here.


class RegisterForm(Form):
    firstname = TextField("First name",  [DataRequired()])
    lastname = TextField("Last name",  [DataRequired()])
    email = TextField("Email",  [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField("Create account")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if Customer.query.filter_by(EMAIL=self.email.data.lower()).first() is not None:
            obj1 = ()
            self.email.errors = list(obj1)
            self.email.errors.append('That email is already taken')  # .append("That email is already taken")
            return False
        else:
            return True


class LoginForm(Form):
    name = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])

