from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    texto_contacto = "Si quieres ponerte en contacto conmigo, bien sea para trabajar juntos, proponerme un proyecto, ofrecerme empleo, comprar alguno de mis libros, o simplemente contarme algo, envíame un correo electrónico:"
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            # Enviar el correo electrónico
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            content = request.POST.get("content", "")
            
            # Aquí puedes agregar la lógica para enviar el correo electrónico
            email = EmailMessage(
                "Mensaje enviado desde la web",
                f"De {name}<{email}>\n\nEscribió:\n\n{content}",
                "zaton81@mailtrap.io",
                ["zaton81@mailtrap.io"],
                reply_to = [email]
            )
            try:
                email.send()
                return redirect(reverse("contact")+"?ok")
            except Exception as e:
                print(f"Error al enviar el correo: {e}")
                return redirect(reverse("contact")+"?fail")
            
            
    return render(request, "contact/contact.html", {
        "texto_contacto": texto_contacto, 
        "form": contact_form})
