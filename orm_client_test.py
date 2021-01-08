from orm_client import OdooClient

config  = {
    "url":"localhost",
    "db":"employee",
    "user":"xxxxx@gmail.com",
    "password":"xxxxx",
    "port":8069
}

body = {
    'action': ('create','read', 'write', 'search', 'unlink'),
    'model':'hr.employee'
    # 'model':'res.users'
}


client = OdooClient(config)

client.login()

# print('----------login_response------', login_response)

create_object = { 
    "create_uid": 9, 
    "id": 45, 
    "name": 'Rohit Sharma' 
}

create_response = client.create(create_object)

print('---------create_response-----------', create_response)

# read_response = client.read(body)

# print('----------read_response---------', read_response)

update_object = {
    'name': "Irfan Pathan"
}

# update_response = client.update(body)

# print('-----------update_response----------', update_response)

delete_response = client.delete(body)

print('-----------delete_response-----------', delete_response)
