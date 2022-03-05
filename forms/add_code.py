from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired


class AddCodeForm(FlaskForm):
    title = StringField('название', validators=[DataRequired()])
    about = TextAreaField('Описание', validators=[DataRequired()])
    code = StringField('Track Code', validators=[DataRequired()])
    price = IntegerField('Цена', validators=[DataRequired()])
    submit = SubmitField('Submit')