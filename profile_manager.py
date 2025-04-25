#starting skeleton

import json

FILENAME = 'profiles.json'

def load_profiles():
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_profiles(profiles):
    with open(FILENAME, 'w') as file:
        json.dump(profiles, file, indent=4)

def add_profile(name, age, job):
    profiles = load_profiles()
    profiles.append({
        "name": name,
        "age": age,
        "job": job
    })
    save_profiles(profiles)
    print(f"Profile for {name} added.")

def list_profiles():
    profiles = load_profiles()
    for person in profiles:
        print(f"Name: {person['name']}, Age: {person['age']}, Job: {person['job']}")

if __name__ == "__main__":
    print("1. Add Profile")
    print("2. List Profiles")
    choice = input("Choose option (1 or 2): ")

    if choice == '1':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        job = input("Enter job: ")
        add_profile(name, age, job)
    elif choice == '2':
        list_profiles()
    else:
        print("Invalid choice.")
