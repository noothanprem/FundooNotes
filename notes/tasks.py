from celery.decorators import task
from celery.utils.log import get_task_logger
import os

from django.core.mail import send_mail
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from .models import Note
logger = get_task_logger(__name__)


@periodic_task(run_every=(crontab(minute='*/2')),
               name="send_email_task",
               ignore_result = True)
def reminder_notification_task(user):
    smd_response = {
        'success':False,
        'message':"",
        'data':[]
    }
    """sends an email when feedback form is filled successfully"""
    try:

        logger.info("Sent email")
        subject = "tash_check"
        message = "helloooooo"
        sender = os.getenv('EMAIL_HOST_USER')
        reciever = os.getenv('EMAILID')
        send_mail(subject, message, sender, [reciever])
    except Exception:
        smd_response['message']="Exception occured"
        return smd_response
    smd_response['success']=True
    smd_response['message']="success"
    return smd_response
