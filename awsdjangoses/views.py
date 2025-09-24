import json
import requests

from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from . import services



class AmazonSesViewSet(ViewSet):
    permission_classes = [AllowAny]

    @staticmethod
    def confirm_subscription(request):
        message_body = json.loads(request.body)
        url = message_body['SubscribeURL']
        requests.get(url)
        return Response()

    @action(methods=['post'], detail=False)
    def bounces(self, request):
        if request._request.META[
            'HTTP_X_AMZ_SNS_MESSAGE_TYPE'] == 'SubscriptionConfirmation':
            return self.confirm_subscription(request)
        elif request._request.META['HTTP_X_AMZ_SNS_MESSAGE_TYPE'] == 'Notification':
            services.handle_bounce(request)
        return Response()

    @action(methods=['post'], detail=False)
    def complaints(self, request):
        if request._request.META[
            'HTTP_X_AMZ_SNS_MESSAGE_TYPE'] == 'SubscriptionConfirmation':
            return self.confirm_subscription(request)
        elif request._request.META['HTTP_X_AMZ_SNS_MESSAGE_TYPE'] == 'Notification':
            services.handle_complaint(request)
        return Response()

    @action(methods=['post'], detail=False)
    def delivery(self, request):
        if request._request.META[
            'HTTP_X_AMZ_SNS_MESSAGE_TYPE'] == 'SubscriptionConfirmation':
            return self.confirm_subscription(request)
        elif request._request.META['HTTP_X_AMZ_SNS_MESSAGE_TYPE'] == 'Notification':
            services.handle_delivery(request)
        return Response()