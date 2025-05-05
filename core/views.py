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
                                                   
