from django.contrib.auth.backends import ModelBackend
from .models import AdvUser


class EmailAuthBackend(ModelBackend):
    def authenticate(self,request, username=None, password=None,**kwargs):
        try:
            user = AdvUser.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                return None
        except AdvUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return AdvUser.objects.get(pk=user_id)
        except AdvUser.DoesNotExist:
            return None
