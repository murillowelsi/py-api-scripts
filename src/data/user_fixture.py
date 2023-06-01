from faker import Faker

fake = Faker()

users = []
for i in range(20):
    user = {
        "name": fake.first_name(),
        "gender": fake.random_element(elements=("male", "female")),
        "email": fake.email(),
        "status": "active",
    }
    users.append(user)
