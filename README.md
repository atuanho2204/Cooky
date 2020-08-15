# Cooky
 A Django web app for college students to help them for weekly meals planning and provide cooking instructions.
 It collects user's BMI information, analyzes and stores in database.
 Calculate the nutritional value of the recipe. 
## Installation:
### 1. Clone Repo
    git clone https://github.com/atuanho2204/Cooky.git
### 2. Install requirements
    cd requirements.txt
    pip install -r requirements.txt
### 3. Migrate Database
    python3 manage.py makemigrations
    python3 manage.py migrate
### 4. Create User
    python3 manage.py createsuperuser
### 5. Run Server
    python3 manage.py runserver


## Built with
    Django ^8.0.20
    python3 ^3.8.1
    Nutritionix API
    
    
