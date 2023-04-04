import redis
from redis_lru import RedisLRU

from connect import connect
from models import Quote

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)

quotes = Quote.objects()


@cache
def find_by_name(value):
    finding_quotes = []
    full_name = value.split(":")[1]
    for quote in quotes:
        if quote.author.fullname.lower() == full_name.lower():
            finding_quotes.append(quote.quote)
    print(finding_quotes)


@cache
def find_by_tag(value):
    finding_quotes = []
    tags = value.split(":")[1].split(",")
    for quote in quotes:
        for tag in tags:
            if tag in quote.tags:
                finding_quotes.append(quote.quote)
    print(finding_quotes)


def main():

    while True:
        command = input("Enter your 'command:value' or 'exit': ")

        if command.startswith("name"):
            find_by_name(command)
        elif command.startswith("tag"):
            find_by_tag(command)
        elif command.startswith("exit"):
            break
        else:
            print("Wrong command. Please, try again.")
            continue


if __name__ == "__main__":
    main()