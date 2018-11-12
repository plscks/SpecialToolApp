# forms.py

from wtforms import Form, StringField, SelectField

class ToolSearchForm(Form):
    choices = [('Tool Number', 'Tool Number'), ('Location', 'Location')]
    select = SelectField('Search for Special Tools:', choices=choices)
    search = StringField('')

class ToolForm(Form):
    toolnumber = StringField('Tool Number:')
    location = StringField('Location:')
