from xmlrpc import client

url= 'https://ithamdanhomepro-online-technical-training-15-0-dev-a-6164846.dev.odoo.com/'
db= 'ithamdanhomepro-online-technical-training-15-0-dev-a-6164846'
username = 'admin'
password = 'password'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

#grab all models
models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

#check access right to model sale.order 
model_access = models.execute_kw(db, uid, password,
                                 'sale.order', 'check_access_rights',
                                 ['write'], {'raise_exception': False})

print(model_access)

draft_quotes = models.execute_kw(db, uid, password,
                                 'sale.order', 'search',
                                 [[['state', '=', 'draft']]])

print(draft_quotes)

if_confirmed = models.execute_kw(db, uid, password,
                                 'sale.order', 'action_confirm',
                                 [draft_quotes])

print(if_confirmed)
