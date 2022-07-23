from django.db import models
from django.utils import timezone

from model_utils import FieldTracker
from utils.email import send_email, email_admins


class Contact(models.Model):
    fullname = models.CharField(max_length=128, verbose_name='full name')
    email = models.EmailField()
    title = models.CharField(max_length=75)
    text = models.TextField(verbose_name='your message')
    answer = models.TextField(null=True, blank=True)
    is_answered = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_answered = models.DateTimeField(null=True, blank=True)

    answer_tracker = FieldTracker(fields=['answer'])

    def _is_created(self):
        return not Contact.objects.filter(pk=self.pk).exists()

    def _email_answer(self):
        context = {
            'fullname': self.fullname,
            'title': self.title,
            'answer': self.answer
        }
        send_email(
            f'answer to {self.title} - codingyar',
            [self.email, ],
            'email/contact_us_answer.html',
            context
        )

    def _notify_admins(self):
        context = {
            'created': timezone.now(),
            'title': self.title,
            'fullname': self.fullname
        }
        email_admins(
            f'new message from - {self.fullname}',
            'email/notify_admins_new_contact.html',
            context
        )

    def _is_answered(self):
        return all(
            (self.answer_tracker.has_changed('answer'), self.answer)
        )

    def save(self, **kwargs):
        if self._is_created():
            self._notify_admins()
        else:
            if self._is_answered():
                self._email_answer()
                self.is_answered = True
                self.datetime_answered = timezone.now()
        return super().save(**kwargs)

    def __str__(self):
        return f'{self.fullname} - {self.title}'
