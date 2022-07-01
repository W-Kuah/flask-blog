import os
from config import db
from models import Person

# Data to initialise database with
PEOPLE = [
    {'fname': 'Warren', 'lname': 'Kuah'},
    {'fname': 'Richard', 'lname': 'Pie'},
    {'fname': 'Ted', 'lname': 'Guna'},
]

# Delete database file if it exists currently
if os.path.exists('people.db'):
    os.remove('people.db')

# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = Person(lname=person.get('lname'), fname=person.get('fname'))
    db.session.add(p)

db.session.commit()
