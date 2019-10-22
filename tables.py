from flask_table import Table, Col, LinkCol
 
class Results(Table):
    user_id = Col('Id', show=False)
    user_name = Col('First Name')
    other_name = Col('Middle Name')
    surname = Col('Surname')
    user_email = Col('Email')
    phone = Col('Phone')
    address = Col('Address')
    ec_number = Col('EC Number')
    role = Col('Role')
    user_password = Col('Password', show=False)
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='user_id'))
    delete = LinkCol('Delete', 'delete_user', url_kwargs=dict(id='user_id'))