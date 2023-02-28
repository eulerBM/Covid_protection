from django.db.models.signals import post_save
from index.models import email
from django.dispatch import receiver
from django.core.mail import send_mail


@receiver(post_save,sender=email)
def send_email(sender, instance, created, **kwargs):
    if created:
        send_mail('Seja bem vindo :D', 'Voce se cadastrou no site do Euler, vlw carinha!', 'eullerborgesdamotta17@gmail.com', [instance])

    else:
        send_mail('Ouve uma alteração no seu email', 'Ola, notamos que ouve uma alteração no seu email!', 'eullerborgesdamotta17@gmail.com', [instance])



        
