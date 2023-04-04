from mongoengine import Document, DENY
from mongoengine.fields import ListField, StringField, ReferenceField


class Author(Document):
    meta = {'collection': 'authors'}
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    meta = {'collection': 'quotes', 'allow_inheritance': True}
    tags = ListField(StringField(max_length=100))
    quote = StringField()
    author = ReferenceField(Author, required=True, reverse_delete_rule=DENY)
