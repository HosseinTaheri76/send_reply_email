from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email(subject, recipient_list, template_name, context):
    html_message = render_to_string(template_name, context)
    plain_text = strip_tags(html_message)
    send_mail(
        subject=subject,
        recipient_list=recipient_list,
        from_email='test@test.com',
        message=plain_text,
        html_message=html_message
    )
