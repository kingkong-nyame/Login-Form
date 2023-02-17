from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = "Kingkongnyame"

class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message='name is required'),Length(min=5,max=30, message='Must between 5 and 30')])
    email = EmailField('email', validators=[DataRequired(message='Email is required'),Length(min=15,max=30, message='Must between 5 and 30')])
    password = PasswordField('password', validators=[DataRequired(message="Password is required"), Length(min=6,max=30,message="Must between 6 and 30")])
  






@app.route('/')
@app.route('/form', methods=["GET", "POST"])
def form():
     form = LoginForm()
     if form.validate_on_submit():
        return render_template('results.html', name= form.name.data, email=form.email.data, password=form.password.data)
     return render_template('form.html', form=form)


if __name__== '__main__':
    app.run(debug=False)