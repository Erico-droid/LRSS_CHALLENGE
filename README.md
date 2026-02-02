Leave Management Submission System: Challenge

A Django-based application to submit, list, and update employee leave requests with automatic weekend-adjustment logic.

1. Clone the Repository
Bash
git clone https://github.com/Erico-droid/LRSS_CHALLENGE.git
cd LRSS_CHALLENGE

2. Set Up a Virtual Environment
It is recommended to use a virtual environment to keep your global Python packages clean.

Bash
# Create the environment
virtualenv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate

3. Install Dependencies
Install the required packages using the requirements.txt file.

Bash
pip install -r requirements.txt

4. Database Migrations
Since the project includes a LeaveRequest model, you need to prepare and apply the database schema.

Bash
# Create the migration files based on models.py
python manage.py makemigrations

# Apply the migrations to the database (creates tables)
python manage.py migrate


6. Run the Application
Start the development server:

Bash
python manage.py runserver
The application will be available at http://127.0.0.1:8000/.