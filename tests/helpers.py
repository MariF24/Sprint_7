import faker

def get_creation_courier():
    fake = faker.Faker()
    login = fake.name().lower()
    first_name = fake.first_name().lower()
    return login,first_name