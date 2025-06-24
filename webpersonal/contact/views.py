from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.contrib import messages

class ContactView(FormView):
    """Vista de formulario de contacto con envío de email y mensajes de éxito/error."""
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['texto_contacto'] = "Si quieres ponerte en contacto conmigo, bien sea para trabajar juntos, proponerme un proyecto, ofrecerme empleo, comprar alguno de mis libros, o simplemente contarme algo, envíame un correo electrónico:"
        return context

    def form_valid(self, form):
        name = form.cleaned_data.get("name", "")
        email = form.cleaned_data.get("email", "")
        content = form.cleaned_data.get("content", "")
        email_message = EmailMessage(
            "Mensaje enviado desde la web",
            f"De {name}<{email}>\n\nEscribió:\n\n{content}",
            "zaton81@mailtrap.io",
            ["zaton81@mailtrap.io"],
            reply_to=[email]
        )
        try:
            email_message.send()
            messages.success(self.request, "Gracias por tu mensaje. Te contestaré lo antes posible.")
            return super().form_valid(form)
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
            messages.error(self.request, "Hubo un error al enviar el mensaje. Inténtalo de nuevo más tarde.")
            return self.form_invalid(form)
