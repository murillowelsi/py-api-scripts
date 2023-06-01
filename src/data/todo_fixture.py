from faker import Faker

fake = Faker()

todo_fixture = {
    "user_id": fake.random_int(min=1000000, max=9999999),
    "title": fake.sentence(),
    "due_on": fake.date_time_this_month(
        before_now=False, after_now=True, tzinfo=None
    ).isoformat(),
    "status": fake.random_element(elements=("completed", "pending")),
}

print(todo_fixture)
