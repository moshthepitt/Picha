from django.views.generic.edit import FormView
from feedback.forms import ContactForm


class ContactView(FormView):
    template_name = 'feedback/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)
