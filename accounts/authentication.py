import sys
from accounts.models import DatasetUser, Token

class PasswordlessAuthenticationBackend(object):

    def authenticate(self, uid):
        print('uid', uid, file=sys.stderr)
        if not Token.objects.filter(uid=uid).exists():
            print('no token found', file=sys.stderr)
            return None
        token = Token.objects.get(uid=uid)
        print('got token', file=sys.stderr)
        try:
            user = DatasetUser.objects.get(email=token.email)
            print('got user', file=sys.stderr)
            return user
        except DatasetUser.DoesNotExist:
            print('new user', file=sys.stderr)
            return DatasetUser.objects.create(email=token.email)

    def get_user(self, email):
        return DatasetUser.objects.get(email=email)
