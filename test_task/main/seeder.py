from django_seed import Seed
import random
from datetime import timedelta
from django.utils import timezone
from main.models import *
from faker import Faker


seeder = Seed.seeder()
fake = Faker("ru_RU")
positions = [
    'системный администратор',
    'модератор форума',
    'программист',
    'тестировщик',
    'системный аналитик',
    'гейм-дизайнер',
    'тимлид',
    'QA-инженер',
]

Employee.objects.create(name='Boss', position='boss', salary=300000)
seeder.add_entity(Employee, 3, {
    'name': lambda x: fake.name(),
    'position': lambda x: random.choice(positions),
    'salary': lambda x: random.randint(250000, 300000),
    'parent_id': 1,
    'level': 1,
    'photo': None,
})
seeder.add_entity(Employee, 9, {
    'name': lambda x: fake.name(),
    'position': lambda x: random.choice(positions),
    'salary': lambda x: random.randint(200000, 250000),
    'parent_id': lambda x: random.randint(2, 4),
    'start_date': lambda x: timezone.now() - timedelta(weeks=random.randint(0, 500)),
    'level': 2,
    'photo': None,
})
seeder.add_entity(Employee, 27, {
    'name': lambda x: fake.name(),
    'position': lambda x: random.choice(positions),
    'salary': lambda x: random.randint(150000, 200000),
    'parent_id': lambda x: random.randint(5, 13),
    'start_date': lambda x: timezone.now() - timedelta(weeks=random.randint(0, 500)),
    'level': 3,
    'photo': None,
})
seeder.add_entity(Employee, 50000, {
    'name': lambda x: fake.name(),
    'position': lambda x: random.choice(positions),
    'salary': lambda x: random.randint(50000, 150000),
    'parent_id': lambda x: random.randint(14, 40),
    'start_date': lambda x: timezone.now() - timedelta(weeks=random.randint(0, 500)),
    'level': 4,
    'photo': None,
})

seeder.execute()
