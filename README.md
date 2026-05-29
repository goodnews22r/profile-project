# User Profile Manager

A reusable Python program that interactively collects user profiles, validates inputs, saves profiles into a JSON file, and displays saved profiles.


## Features
* Collects user profile information
* Validates:

  * Name
  * Age
  * Email
* Saves multiple profiles to `profile.json`
* Reads and displays saved profiles
* Pretty-printed JSON formatting
* Error handling for missing files

---

## Technologies Used
* Python 3
* JSON file handling

---

Project Structure
profile-project/
│
├── profile_manager.py
├── profile.json
├── README.md
└── requirements.txt

---

## How to Run

### 1. Clone the repository


git clone https://github.com/goodnews22r/profile-project.git


### 2. Navigate into the folder


cd profile-project

### 3. Run the program


python profile_manager.py


## Example Output
=== User Profile Setup ===
Enter your name: Goodnews Okoro
Enter your age: 30
Enter your email: goodnews@gmail.com


Profile saved successfully!


=== Saved Profiles ===
Profile 1
Name : Goodnews Okoro
Age  : 30
Email: goodnews@gmail.com

