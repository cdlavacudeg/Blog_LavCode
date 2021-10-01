from blog.models import Blog,Autor,Categoria

#python manage.py runscript post_test.py
def run():
    titulo="Post Prueba"
    descripcion="Prueba insersion con Scripts"
    imagen="https://i0.wp.com/unaaldia.hispasec.com/wp-content/uploads/2019/06/django.png?fit=1200%2C800&ssl=1"
    autor=Autor.objects.get(id=1)
    categoria=Categoria.objects.get(id=3)
    contenido="<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.    Nam, cumque ea totam quisquam odit voluptatem in veniam animi, omnis facere iure, sequi officia exercitationem nesciunt eaque consequatur consectetur nemo eveniet</p>"
    for j in range(100,500):
        print(j)
        
        
        post_new=Blog(titulo=titulo+str(j),descripcion=descripcion,imagen=imagen,autor=autor,contenido=contenido)
        post_new.save()
        post_new.categoria.add(categoria)
    