# 📚 PythonTrip

## Table of Contents
- [📄 Project Description](#-project-description)
- [🎯 Motivation](#-motivation)
- [🚀 Features](#-features)
- [📅 Project Management](#-project-management)
- [📖 Documentation](#-documentation)
- [🛠 Technologies Used](#-technologies-used)
- [📦 Installation and Configuration](#-installation-and-configuration)
- [🧪 Testing](#-testing)
- [🤝 Contributions](#-contributions)
- [📧 Contact](#-contact)



## 📄 Project Description

**Python Tryp** Pyton Tryp is a mobile travel recommendation application that allows users to select itineraries based on suggestions provided by the app and to generate personalised itineraries. Users will be able to create and manage collections of
their favourite places, view: 

## 🎯 Motivation

Our motivation is to offer a clean and accessible design for the user with the possibility to interact intuitively with the application.

## 🚀 Features

### Python Tryp Users (CRUD Operations)
- **Create**: Register new users in the application
- **Read**: Search and browse itineraries by different criteria
- **Update**: Updates information on itineraries and destinations
- **Delete**: Remove user information
- **Validation**: Ensure there are no duplicates in the itineraries by using appropriate validations. 

### User Preferences (CRUD Operations)
- **Create**: Register preferences of destinations, locations, etc.
- **Read**: View their stored preferences in a profile or settings page.
- **Update**: Enable users to modify their existing trip preferences.
- **Delete**:Allow users to remove specific preferences or reset all preferences.
- **Validation**: Ensure there are no duplicates 

### User Management (CRUD Operations)
- **Create**: Register new users in the application.
- **Read**: The system may use these preferences to suggest itineraries and locations 
- **Update**: The system updates the user's data.
- **Delete**: Remove users from the system.
- **Validation**: Ensure no duplicate users using appropriate validations.

## 📅 Project Management
This project was developed by a team of 5 developers using SCRUM. Tools like Jira were used for backlog management and sprint planning.


## 📖 Documentation
- **[Algorithm Flowchart](https://drive.google.com/file/d/1mAbBGxqN5jEWShzmNyD6wV6rYGYuTjZA/view   )**: A flowchart illustrating the main algorithms implemented in the project
- **[Data Model](https://drawsql.app/teams/lp-11/diagrams/pythontrip)**: A diagram showing the key entities of the system and their relationships, available on DrawSQL.

## 🛠 Technologies Used

- **Language**: Python (v3.12.4)
- **Database**: PostgreSQL (v16.2)
- **Testing**: Pytest (v8.3.2), Unittest (integrated with Python)
- **Version Control**: Git (v2.45.2) with GitFlow
- **psycopg2**
- **Pycharm**
- **Django**
- **Django REST Framework**
- **Drawio**


## 📦 Installation and Configuration

1. **Clone the repository:**
   ```bash
   git clone
   https://github.com/helopgom/PythonTrip_front.git
   ```
2. **Create and activate your virtual enviroment:**
    ```bash
    cd trip_planner_back
    python -m venv env
    source env/bin/activate  # En Windows usa: env\Scripts\activate
    ```
    
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Configure the database:**
 Create a database in PostgreSQL with same name the proyect. Add to settings.py:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nameBBDD',
        'USER': 'your BBDD user',
        'PASSWORD': 'your BBDD password',
        'HOST': 'localhost', #(usually is the same)
        'PORT': '5432' #(usually is the same)
    }
} 
   ```
5. **Perform the migrations and run server:**
    ```bash
   python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
   
## 🧪 Testing

- **Run unit and integration tests:**

    ```bash
    Pytest
    ```
### Types of Tests Performed
- **Integration test**: Check the interaction between different parts of the system, such as the database, views, and authentication. For example, when testing a user's registration (test_register_user), you are checking that the entire system works from start to finish, including creating the user in the database.


## 📧 Contact

For any inquiries, you can reach out to us through our GitHub and LinkedIn profiles:

- [![GitHub Octocat](https://img.icons8.com/ios-glyphs/30/000000/github.png)](https://github.com/Erieltxu)  [![LinkedIn](https://img.icons8.com/ios-glyphs/30/0077b5/linkedin.png)](https://www.linkedin.com/in/leire-del-hoyo-aldecoa) Leire 
- [![GitHub Octocat](https://img.icons8.com/ios-glyphs/30/000000/github.png)](https://github.com/limonadaweb)  [![LinkedIn](https://img.icons8.com/ios-glyphs/30/0077b5/linkedin.png)](https://www.linkedin.com/in/adriana) Adriana  
- [![GitHub Octocat](https://img.icons8.com/ios-glyphs/30/000000/github.png)](https://github.com/Dpoetess)  [![LinkedIn](https://img.icons8.com/ios-glyphs/30/0077b5/linkedin.png)](https://www.linkedin.com/in/lynn-poh/)  Lynn (Scrum Master)
- [![GitHub Octocat](https://img.icons8.com/ios-glyphs/30/000000/github.png)](https://github.com/Belensanchez1989 )  [![LinkedIn](https://img.icons8.com/ios-glyphs/30/0077b5/linkedin.png)](https://www.linkedin.com/in/helena-lopgom/) Belén (Product Owner)  
- [![GitHub Octocat](https://img.icons8.com/ios-glyphs/30/000000/github.png)](https://github.com/helopgom)  [![LinkedIn](https://img.icons8.com/ios-glyphs/30/0077b5/linkedin.png)](https://www.linkedin.com/in/helena-lopgom/)  Helena

## 😊 If you've made it this far, feel free to follow us on GitHub or LinkedIn. We'd love to be in touch!