from celery import shared_task
from celery.utils.log import get_task_logger
from .models import Notes
from .services import get_new_random_title


@shared_task(name='update_title')
def update_title():
    logger = get_task_logger(__name__)
    logger.info("ok task run")
    queryset = Notes.objects.all()
    if queryset.exists():
        for obj in queryset:
            obj.title = get_new_random_title()
            obj.save()
    logger.info("task completed")
