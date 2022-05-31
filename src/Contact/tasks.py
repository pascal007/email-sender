from __future__ import absolute_import, unicode_literals

from celery.utils.log import get_task_logger
from django.core.mail import send_mail
from django.template.loader import render_to_string

from inventory_app.celery import app

logger = get_task_logger(__name__)


@app.task()
def send_review_email(subject, email, body):
    context = {
        'subject': subject,
        'email': email,
        'body': body
    }

    email_body = render_to_string('email/mail_content.html', context)

    send_mail(
        subject, email_body, 'test@test.com',
        [email]
    )

    return True


