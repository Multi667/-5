import random
import string
def get_random_password() -> str:  # TODO написать функцию генерации случайных паролей
    rand = random.sample(string.ascii_letters + string.digits, 8)
    return ''.join(rand)
print(get_random_password())
