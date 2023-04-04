import json

from connect import connect
from models import Quote, Author

with open('authors.json', 'r', encoding='utf-8') as fh:
      authors = json.load(fh)
      for a in authors:
        author = Author(fullname=a['fullname'], born_date=a['born_date'],
                        born_location=a['born_location'], description=a['description'])
        author.save()


with open('quotes.json', 'r', encoding='utf-8') as fh:
    quotes = json.load(fh)
    for q in quotes:
        for aq in Author.objects():
            if aq.fullname == q['author']:
               author = aq
               break
        quote = Quote(tags=q['tags'], author=author, quote=q['quote'])
        quote.save()
