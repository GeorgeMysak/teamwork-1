from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators
from wtforms.fields import DateField


class FestForm(FlaskForm):
    fest_name = StringField("Name: ", [
        validators.DataRequired("Please enter name of the event"),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])

    fest_date = DateField("Date: ", [validators.DataRequired("Please, enter the date of the event")])

    people_email = StringField("Email: ", [
        validators.Length(3, 20, "Name should be from 3 to 20 symbols"),
        validators.Email("Wrong email format")
    ])

    submit = SubmitField("Save")

    def validate_date(self):
        return bool(self.fest_date.data.year > 2020)