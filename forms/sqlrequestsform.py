from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class SQLRequestsForm(FlaskForm):
    request = StringField('Введите SQL-запрос: ', validators=[DataRequired()])