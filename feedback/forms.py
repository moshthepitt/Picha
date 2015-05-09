from django import forms
from feedback.tasks import send_feedback_email_task


class ContactForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(label="Message", widget=forms.Textarea())
    honeypot = forms.CharField(widget=forms.HiddenInput(), required=False)

    def send_email(self):
        if self.cleaned_data['honeypot']:
            return False
        send_feedback_email_task.delay(self.cleaned_data['email'], self.cleaned_data['message'])
