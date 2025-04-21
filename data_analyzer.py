people = [
    {"name": "Alex", "age": 42, "job": "Engineer"},
    {"name": "Bob", "age": 30, "job": "Designer"},
    {"name": "Elena", "age": 35, "job": "Engineer"},
    {"name": "Timur", "age": 28, "job": "Manager"}
]

def get_average_age(data):
    return sum(person["age"] for person in data) / len(data)

def filter_by_job(data, job_title):
    return list(filter(lambda x: x["job"] == job_title, data))

def sort_people(data, by="age"):
    return sorted(data, key=lambda x: x[by])

def get_oldest_person(data):
    return max(data, key=lambda x: x["age"])

if __name__ == "__main__":
    print("Average age:", get_average_age(people))
    print("\nEngineers:")
    for person in filter_by_job(people, "Engineer"):
        print(person)

    print("\nSorted by name:")
    for person in sort_people(people, "name"):
        print(person)

    print("\nOldest person:")
    print(get_oldest_person(people))
