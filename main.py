from asyncio import run

from models.Person import Person
from models.Post import Post
from services.Service import Service


service = Service()
run(service.create_database())
person = run(service.create(Person, {'name': "aas", 'email': "asdasda"}))
run(service.create(Post, {
            'title':'Live de python foda',
            'content':'ai papai',
            'person':person,
                   }))
result = run(service.search(Person, 'name', 'aas'))
print(result)
run(service.update(Person, 'name', 'LucãoPapai', 'aas'))
result = run(service.search(Person, 'name', 'LucãoPapai'))
print(result)
#run(service.delete(Person, 'name', 'LucãoPapai'))
#result = run(service.search(Person, 'name', 'LucãoPapai'))
#print(result)
# print(run(deletar_pessoa('Gabriel')))
#print(run(buscar_post_por_autor('Thiago')))
result = run(service.join_search(Post, Person, 'id', 'posts', 1))
print(result)
