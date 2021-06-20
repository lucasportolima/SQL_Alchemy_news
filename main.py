from asyncio import run

from models.Person import Person
from models.Post import Post
from services.Service import Service


service = Service()
run(service.create_database())
person = run(service.create(
    Person, {'name': "Lucas Porto", 'email': "lucasportolima@live.com"}))
run(service.create(Post, {
    'title': 'SqlAlchemy',
    'content': 'testing new features',
    'person': person,
}))
result = run(service.search(Person, 'name', 'Lucas Porto'))
print(result)
run(service.update(Person, 'name', 'Fulano', 'Lucas Porto'))
result = run(service.search(Person, 'name', 'Fulano'))
print(result)
result = run(service.join_search(Post, Person, 'id', 'posts', 1))
print(result)
run(service.delete(Person, 'name', 'Fulano'))
