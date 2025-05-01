from django.shortcuts import render, HttpResponse
from .links import *

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    head1 = "💻 Habilidades técnicas"
    head2 = "📚 Filosofía"
    texto1= "Mi nombre es Jorge Zatón, un apasionado programador junior en busca de una nueva oportunidad laboral en este “mundillo”."
    texto2 = "Desde 2011, cuando di mis primeros pasos en el desarrollo web con HTML, CSS y PHP en la Universidad de Deusto, supe que la programación sería mi lenguaje universal. Hoy, como estudiante del Máster en Programación Python en Tokio School (2023-2025), combino mi pasión por el código con el análisis de datos y la inteligencia artificial."
    texto3 = "Me apasiona crear soluciones donde el backend robusto (con Django/Flask) se alíe con el análisis de datos estratégico. Por ejemplo, automatización de informes con Python + Power BI para optimizar procesos empresariales, modelos predictivos entrenados con Scikit-learn' para análisis de tendencias, desarrollo ágil usando Git para mantener un código limpio y colaborativo."
    texto4 = "Creo en la programación como un puente entre la lógica y la creatividad. Por eso, cuando no estoy escribiendo código:"
    lista1 = "Colaboro en proyectos open source."
    lista2= "Exploro aplicaciones de IA en sectores como salud o sostenibilidad."
    lista3 = "Comparto conocimientos en comunidades tech."
    cita = "Los datos bien interpretados son la brújula; el código, el camino."
    certificaciones = "Certificaciones destacadas: ▶︎ IBM SkillsBuild: Artificial Intelligence y Data Science Professional."
    texto5 = "En mi tiempo libre, disfruto de la lectura. Además, he escrito dos libros: Quizá lo quiso el destino y Con todo en contra. También he colaborado en diversas antologías de carácter benéfico, como Mil hstorias y 7 vidas de un gato."
    return render(request, "core/about.html", {"texto1": texto1, 
                                               "texto2": texto2, 
                                               "texto3": texto3, 
                                               "head1": head1, 
                                               "certificaciones": certificaciones,
                                                "head2": head2,
                                                "texto4": texto4,
                                                "lista1": lista1,
                                                "lista2": lista2,
                                                "lista3": lista3,
                                                "cita": cita,
                                                "texto5": texto5,
                                                })



def contact(request):
    texto_contacto = "Si quieres ponerte en contacto conmigo, bien sea para trabajar juntos, proponerme un proyecto, ofrecerme empleo, comprar alguno de mis libros, o simplemente contarme algo, envíame un correo electrónico:"
    email = "zaton81@hotmail.com"
    envio_mail = "zaton81@hotmail.com?subject=Contacto desde la web&amp;body=Hola Jorge, me gustaría ponerme en contacto contigo."
    return render(request, "core/contact.html", {"texto_contacto": texto_contacto, "email": email, "envio_mail": envio_mail})

def portfolio(request):
    texto_tareas = "Realizada con Flask, este es el primer proyecto que he realizado con Python, junto con HTML, CSS y Bootstrap con el que comencé a familiarizarme con las bases de datos, para las que utilicé SQLite y el ORM SQLAlchemy. Un clásico que permite añadir, eliminar y modificar tareas."
    texto_productos = "Otro clásico. En esta ocasión, realicé una aplicación de escritorio con TKinter, SQLite y el ORM SQLAlchemy, permite añadir productos, modificarlos, modificar su precio y/o stock o eliminarlos. Indispensable para cualquier tienda o almacén, dispone de un diseño sencillo e intuitivo."
    texto_videoflix = "Videoflix ha sido el trabajo de fin de Máster. Realizado con el framework Reflex, es una aplicación web que permite a los usuarios registrarse, buscar películas y series, añadirlas a favoritos y verlas en streaming. Además, cuenta con un panel de administración para gestionar usuarios y contenido. Con ella ahondé en las bases de datos relacionales y mejoré mi capacidad para afrontar proyectos de manera más eficiente. Además, me inicié el el webscrapping y fue una primera toma de contacto con proyectos de mayor envergadura, con múltiples archivos y directorios. Un reto apasionante con el que he logrado una fabulosa experiencia."
    texto_web_reflex = "Mi web personal, realizada con Reflex, es un proyecto en constante evolución. En ella muestro mi trayectoria profesional, mis proyectos y mis redes sociales. Además, próximamente contará con un blog en el que comparto mis experiencias en el mundo de la programación y la literatura. Aunque la web definitiva es esta que estás viendo, esta es una secundaria que seguiré perfeccionando ¡No dudes en echar un vistazo! "
    return render(request, "core/portfolio.html", {"texto_tareas": texto_tareas, 
                                                   "repo_gestor_tareas": repo_gestor_tareas,
                                                   "texto_productos": texto_productos,
                                                    "repo_productos": repo_productos,
                                                    "texto_videoflix": texto_videoflix,
                                                    "repo_videoflix": repo_videoflix,
                                                    "texto_web_reflex": texto_web_reflex,
                                                    "repo_web_reflex": repo_web_reflex,
                                                    "web_reflex": web_reflex,
                                                    })
                                                   

def libros(request):
    sinopsisQuiza = "Tras un último año en el que pierde a sus padres, su novia lo abandona y ve la relación con su hermano seriamente dañada, Berto se reencuentra con Lisa, un antiguo amor de la infancia. Con miedo y muchas dudas, no tarda en renacer en ellos su amor olvidado, aunque su relación no es precisamente un camino de rosas. En Quizá lo quiso el destino vemos lo más bello y lo más amargo del amor, en una mezcla de sentimientos que cautivarán al lector."
    sinopsisConTodo = "Pablo sueña con ser escritor. Su abuela Julia tiene la historia perfecta. A punto de cumplir los noventa años, Julia relata a su nieto la historia familiar. Juntos recordarán el inicio del siglo XX en una España decadente y dividida entre monárquicos y republicanos y cómo los diferentes acontecimientos marcaron la vida de su familia. Andrés, de familia republicana y María, cuyo padre idolatra al Rey Alfonso XIII, luchan por un amor imposible mientras ven cómo el país pasa por momentos críticos.Mientras narra la historia de sus antepasados, Pablo deja detalles de su vida, de cómo sus radicales ideas republicanas poco a poco van siendo menos fanáticas, el fin de su carrera universitaria, sus primeros trabajos en el mundo editorial, su sueño de convertirse en escritor de éxito y Diana, la joven de la que inevitablemente comienza a enamorarse. ¿Logrará Pablo cumplir sus sueños? ¿Acabarán Andrés y María juntos? ¿Cómo les afectará el inicio de la dictadura y la posterior Segunda República? ¿Y la Guerra Civil? Encuentra las respuestas en esta apasionante historia generacional y recorre el primer tercio del siglo pasado de la mano de Pablo." 
    comprarQuiza = "https://amzn.to/4idT923"
    comprarConTodo = "https://amzn.to/4igAKl8"
    return render(request, "core/libros.html", {"sinopsisQuiza": sinopsisQuiza, "sinopsisConTodo": sinopsisConTodo, "comprarQuiza": comprarQuiza, "comprarConTodo": comprarConTodo})
