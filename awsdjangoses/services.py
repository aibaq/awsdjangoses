import json

from .models import AwsBlackList, AwsDelivery
from .utils import get_delivery_callback


def handle_bounce(request):
    message_body = json.loads(request.body)
    message = json.loads(message_body['Message'])
    bounce = message['bounce']
    for recipient in bounce['bouncedRecipients']:
        instance, created = AwsBlackList.objects.get_or_create(
            email=recipient['emailAddress'],
            defaults={
                'bounce': True,
            },
        )
        if not created and not instance.bounce:
            instance.bounce = True
            instance.save(update_fields=['bounce'])


def handle_complaint(request):
    message_body = json.loads(request.body)
    message = json.loads(message_body['Message'])
    complaint = message['complaint']
    for recipient in complaint['complainedRecipients']:
        instance, created = AwsBlackList.objects.get_or_create(email=recipient['emailAddress'],
            defaults={
                'complaint': True,
            },
        )
        if not created and not instance.complaint:
            instance.complaint = True
            instance.save(update_fields=['complaint'])


def handle_delivery(request):
    message_body = json.loads(request.body)
    message = json.loads(message_body['Message'])
    delivery_message = AwsDelivery.objects.create(
        mail=message['mail'],
        delivery=message['delivery'],
    )
    if callback := get_delivery_callback():
        callback(delivery_message)
