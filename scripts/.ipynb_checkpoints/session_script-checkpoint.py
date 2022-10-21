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
                                 'academy.session', 'check_access_rights',
                                 ['write'], {'raise_exception': False})

print(model_access)

#get courses
courses = models.execute_kw(db, uid, password,
                            'academy.course', 'search_read',
                            [[['level', 'in', ['intermediate', 'beginner']]]])

print(courses)

#get the id to create a session
course = models.execute_kw(db, uid, password,
                           'academy.course', 'search',
                           [[['name', '=', 'Accounting 200']]])
print('============================\nCourse id:', course)

session_fields = models.execute_kw(db, uid, password,
                                   'academy.session', 'fields_get',
                                    [], {'attributes': ['string', 'type', 'required']})

print(session_fields)
print('***************************')

#create a new session
new_session = models.execute_kw(db, uid, password,
                                'academy.session', 'create',
                                [
                                    {
                                        'course_id': course[0],
                                        'state': 'open',
                                        'duration': 5,
                                    }
                                 ]
                                )
print(new_session)
