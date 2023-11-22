from random_word import RandomWords
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model


def get_new_random_title(max_length=50, word_count=4) -> str:
    title = " ".join(RandomWords().get_random_word() for _ in range(word_count))
    return title[:max_length] if len(title) > max_length else title


def create_user(*, validated_data):
    user = get_user_model().objects.create_user(**validated_data)
    refresh = RefreshToken.for_user(user)
    return {"refresh": str(refresh), "access": str(refresh.access_token)}
