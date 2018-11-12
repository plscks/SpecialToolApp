# Tables.py?!?!??

from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    partnumber = Col('Tool Number')
    location = Col('Location')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))

class Delete(Table):
    id = Col('Id', show=False)
    partnumber = Col('Tool Number')
    location = Col('Location')
