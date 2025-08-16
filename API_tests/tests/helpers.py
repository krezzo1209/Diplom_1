import requests
import random
import string


def generate_user_data():
    """Генерирует уникальные email, пароль и имя."""
    email = f"{''.join(random.choices(string.ascii_lowercase, k=8))}@ya.ru"
    return {
        "email": email,
        "password": "password123",
        "name": "Test User"
    }


def register_user(payload):
    """Регистрирует пользователя и возвращает токен авторизации."""
    response = requests.post("https://stellarburgers.nomoreparties.site/api/v2/auth/register", json=payload)
    if response.status_code == 200:
        return response.json()["accessToken"]
    return None


def delete_user(token):
    """Удаляет пользователя по токену."""
    if token:
        requests.delete(
            "https://stellarburgers.nomoreparties.site/api/v2/auth/user",
            headers={"Authorization": token}
        )


def get_ingredients():
    """Получает список доступных ингредиентов."""
    response = requests.get("https://stellarburgers.nomoreparties.site/api/v2/ingredients")
    if response.status_code == 200:
        return response.json()["data"]
    return []