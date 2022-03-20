from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, SubmitField, IntegerField, TextAreaField, \
    RadioField, FileField, FloatField
from wtforms.validators import DataRequired


class AddCodeForm(FlaskForm):
    choices = ("авиаперевозки", "авиапочты", "транспортная перевозка", "контейнерная перевозка")
    title = StringField('название', validators=[DataRequired()])
    about = TextAreaField('Описание', validators=[DataRequired()])
    code = StringField('Код клиента', validators=[DataRequired()])
    amount = IntegerField('Количевство', validators=[DataRequired()])
    price = IntegerField('Цена', validators=[DataRequired()])
    delivery_type = RadioField('Label', choices=[(el,) * 2 for el in choices], default=choices[0])
    result = FloatField('Объем', render_kw={'readonly': True})
    weight = IntegerField('Вес', validators=[DataRequired()])
    photos = FileField("Фото", validators=[FileRequired()])
    delivery_price = IntegerField("Цена", render_kw={'readonly': True})
    submit = SubmitField('Submit')


data = ["result", "delivery_type", "price", "amount", "weight"]