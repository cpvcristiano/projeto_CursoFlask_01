from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

class FormsCadastro(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    telefone = StringField('telefone', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])
    enviar = SubmitField('Enviar')
    
