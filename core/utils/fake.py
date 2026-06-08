import random
import uuid
from faker import Faker

fake = Faker()

def generate_random_value(field_type):
    if field_type == 'CharField':
        return fake.text(30)
    elif field_type == 'TextField':
        return fake.text(max_nb_chars=100)
    elif field_type == 'IntegerField':
        return random.randint(1, 100)
    elif field_type == 'FloatField':
        return round(random.uniform(1.0, 100.0), 2)
    elif field_type == 'UUIDField':
        return str(uuid.uuid4())
    elif field_type == 'DateField':
        return fake.date_this_decade().isoformat()
    elif field_type == 'DateTimeField':
        return fake.date_time_this_decade().isoformat()
    elif field_type == 'BooleanField':
        return random.choice([True, False])
    elif field_type == 'EmailField':
        return fake.email()
    elif field_type == "BinaryField":
        return fake.binary(length=128)
    elif field_type == "JSONField":
        return fake.json()
    elif field_type == "FileField":
        return fake.file_path()
    elif field_type == "URLField":
        return fake.url()
    elif field_type == "TimeField":
        return fake.time()
    return None
