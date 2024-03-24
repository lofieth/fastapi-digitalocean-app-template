from database.database import database


def hello_world(text):
    hello_world = database("hello_world " + text)
    return hello_world
