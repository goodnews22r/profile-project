import json


def validate_name(name):
    return name.strip() != ""


def validate_age(age):
    return age.isdigit() and 0 < int(age) < 120


def validate_email(email):
    return "@" in email and "." in email


def get_valid_input(prompt, validation_function, error_message):
    while True:
        value = input(prompt)

        if validation_function(value):
            return value

        print(error_message)


def collect_profile():
    print("\n=== User Profile Setup ===\n")

    name = get_valid_input(
        "Enter your name: ",
        validate_name,
        "Name cannot be empty."
    )

    age = get_valid_input(
        "Enter your age: ",
        validate_age,
        "Please enter a valid age."
    )

    email = get_valid_input(
        "Enter your email: ",
        validate_email,
        "Please enter a valid email."
    )

    profile = {
        "name": name,
        "age": int(age),
        "email": email
    }

    return profile


def save_profile(profile, filename="profile.json"):
    with open(filename, "w") as file:
        json.dump(profile, file, indent=4)

    print("\nProfile saved successfully!")


def load_profile(filename="profile.json"):
    try:
        with open(filename, "r") as file:
            profile = json.load(file)

        return profile

    except FileNotFoundError:
        print("Profile file not found.")
        return None


def display_profile(profile):
    if profile:
        print("\n=== Saved Profile ===")
        print(f"Name : {profile['name']}")
        print(f"Age  : {profile['age']}")
        print(f"Email: {profile['email']}")


def main():
    profile = collect_profile()

    save_profile(profile)

    saved_profile = load_profile()

    display_profile(saved_profile)


if __name__ == "__main__":
    main()
