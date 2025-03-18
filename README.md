**QuizApp Frontend:**
A simple Django-based quiz application. The app allows users to take quizzes, view scores and administrators to manage questions.

**Features**
1. Quiz Taking: Users can view a set of questions and select answers. Upon submission, the app calculates the correct answers.
2. Admin Authentication: Admin users can log in with a username and password to manage quizzes.
3. Rest API : Includes RESTful APIs to create, update, and list quizzes which is integrated with the frontend of the application.

**Requirements**
1. Python
2. Django
3. Django REST Framework (for API functionality)
4. SQLite (database)

**How to run in local?**
<br />
**1. Clone the repository:**
git clone https://github.com/Sushmitha26/QuizApp-Frontend.git

**2. Navigate to the project directory:**
cd QuizApp-Frontend

**3. Install dependencies:**
pip install

**4. Apply migrations:**
python manage.py makemigrations
python manage.py migrate

**6. Create a superuser (for admin access):**
python manage.py createsuperuser

**7. Start the development server:**
python manage.py runserver

8. Visit http://localhost:8000/home to access the app.
