# this script is to get the JWT tokens

from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    access = refresh.access_token
    exp_timestamp = access.get("exp")
    exp_date = datetime.fromtimestamp(exp_timestamp).strftime("%Y-%m-%d")

    tokens = {"access": str(refresh.access_token), "exp_date": exp_date}
    return tokens
