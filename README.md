A Classified ads website that allows users to: register accounts, post ads, rate ads, comment on ads etc.
Fullstack django-html

Install and run:
- Clone the repo: git clone https://github.com/DarioDidi/Capstone-project.git
- run a virtual environment: virtualenv -p python3 env 
- activate the env: source env/bin/activate 
- install from requirements.txt: pip install -r requirements.txt
- ensure you have postgres installed, if uncomment and use the sqlite settings.
- Run python manage.py migrate to apply database migrations.
- Run python manage.py runserver

Authentication:
- Views use django auth mixins e.g LoginRequiredMixin to ensure a user is logged in for Creating, Updating and Deleting operations.
- To test, create a user at "ads/register/" with username, email, password1,password2 and login at "ads/login/" with username and password. 
- Try creating an ad at "ads/new/" with a title, description, price(2 decimal places) and tag(single word) field. 

Users can request and auth token from "/api-token-auth/", for example:
- endpoint: api-token-auth/      method: POST                                
- ### Request: 
- {
    "username": "johnDoe",
    "password": "password123"
}
- ### Response: 
- {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
}
