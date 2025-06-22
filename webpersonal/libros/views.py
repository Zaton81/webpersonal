from django.shortcuts import render
from .models import Books
# Create your views here.

def libros(request):
    books = Books.objects.all()
    sinopsisQuiza = "Tras un último año en el que pierde a sus padres, su novia lo abandona y ve la relación con su hermano seriamente dañada, Berto se reencuentra con Lisa, un antiguo amor de la infancia. Con miedo y muchas dudas, no tarda en renacer en ellos su amor olvidado, aunque su relación no es precisamente un camino de rosas. En Quizá lo quiso el destino vemos lo más bello y lo más amargo del amor, en una mezcla de sentimientos que cautivarán al lector."
    sinopsisConTodo = "Pablo sueña con ser escritor. Su abuela Julia tiene la historia perfecta. A punto de cumplir los noventa años, Julia relata a su nieto la historia familiar. Juntos recordarán el inicio del siglo XX en una España decadente y dividida entre monárquicos y republicanos y cómo los diferentes acontecimientos marcaron la vida de su familia. Andrés, de familia republicana y María, cuyo padre idolatra al Rey Alfonso XIII, luchan por un amor imposible mientras ven cómo el país pasa por momentos críticos.Mientras narra la historia de sus antepasados, Pablo deja detalles de su vida, de cómo sus radicales ideas republicanas poco a poco van siendo menos fanáticas, el fin de su carrera universitaria, sus primeros trabajos en el mundo editorial, su sueño de convertirse en escritor de éxito y Diana, la joven de la que inevitablemente comienza a enamorarse. ¿Logrará Pablo cumplir sus sueños? ¿Acabarán Andrés y María juntos? ¿Cómo les afectará el inicio de la dictadura y la posterior Segunda República? ¿Y la Guerra Civil? Encuentra las respuestas en esta apasionante historia generacional y recorre el primer tercio del siglo pasado de la mano de Pablo." 
    comprarQuiza = "https://amzn.to/4idT923"
    comprarConTodo = "https://amzn.to/4igAKl8"
    return render(request, "libros/libros.html", {
        "books": books,
        "sinopsisQuiza": sinopsisQuiza, "sinopsisConTodo": sinopsisConTodo, "comprarQuiza": comprarQuiza, "comprarConTodo": comprarConTodo})
