from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators


class ContestForm(FlaskForm):
    contest_name = StringField("Name: ", [
        validators.DataRequired("Please, enter the description of the event"),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])

    submit = SubmitField("Save")