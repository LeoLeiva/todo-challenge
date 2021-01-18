from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from task.models import InveraTask, TaskLogs
from datetime import datetime
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed

@receiver(pre_delete, sender=InveraTask)
def audit_log_delete(sender, instance, **kwargs):
    TaskLogs.objects.create(date_log=datetime.now(), action_log='Elimino la tarea: %s' % (instance.title))


@receiver(pre_save, sender=InveraTask)
def audit_pre_save_task(sender, instance, **kwargs):
    if instance._state.adding:
        TaskLogs.objects.create(date_log=datetime.now(), action_log='Creo una tarea nueva')
    else:
        TaskLogs.objects.create(date_log=datetime.now(), action_log='Modifico la tarea: %s' % (instance.title))


@receiver(user_logged_in)
def user_logged_in_callback(sender, user, request, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    TaskLogs.objects.create(date_log=datetime.now(), action_log='El usuario %s se logueo correctamente desde: %s' % (user, ip))


@receiver(user_logged_out)
def log_logged_out(sender, user, request, **kwargs):
    TaskLogs.objects.create(date_log=datetime.now(), action_log='El usuario %s cerro su sesion' % (user))


@receiver(user_login_failed)
def log_login_failed(sender, request, credentials, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    TaskLogs.objects.create(date_log=datetime.now(), action_log='Intentaron loguearse con el username %s desde: %s' % (credentials['username'], ip))