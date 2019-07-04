from db import db_session, User

authors = [
    {
        'first_name': 'Vasiliy',
        'last_name': 'Petrov',
        'email': 'vasya@example.com'
    },
    {
        'first_name': 'Masha',
        'last_name': 'Ivanova',
        'email': 'mari@example.com'
    },
    {
        'first_name': 'Poluect',
        'last_name': 'Nevstruyev',
        'email': 'p@example.com'
    }
]


for a in authors:
    author = User(a['first_name'], a['last_name'], a['email'])
    db_session.add(author)

db_session.commit()
