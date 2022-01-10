from blog.models import Blog,Autor,Categoria

#python manage.py runscript post_test.py
def run():
    titulo="Post Prueba "
    descripcion="Prueba insersion con Scripts"
    imagen="https://i0.wp.com/www.silocreativo.com/wp-content/uploads/2018/01/imagen-aleatoria-destacada.png?fit=666%2C370&quality=100&strip=all&ssl=1"
    autor=Autor.objects.get(id=1)
    categoria=Categoria.objects.get(id=6)
    contenido="<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit.    Nam, cumque ea totam quisquam odit voluptatem in veniam animi, omnis facere iure, sequi officia exercitationem nesciunt eaque consequatur consectetur nemo eveniet</p>"
    for j in range(5,45):
        post_new=Blog(titulo=titulo+str(j),descripcion=descripcion,imagen=imagen,autor=autor,contenido=contenido)
        post_new.save()
        post_new.categoria.add(categoria)
    