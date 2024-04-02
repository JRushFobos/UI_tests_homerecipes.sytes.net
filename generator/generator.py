import os
import random

from data.data import Person
from faker import Faker

faker_en = Faker('En')


def generator_person():
    return Person(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        nickname=faker_en.lexify(text=f"{'?' * 12}"),
        email=faker_en.email(),
        password=faker_en.password(),
        )



def generated_file():
    path = rf'f:\LocalRepository\Dev\UI_tests_homerecipes.sytes.net\test_file{random.randint(10,100)}.txt'
    file = open(path, 'w')
    file.write(f'Hello{random.randint(10,100)}')
    file.close()
    os.remove()
    return path
