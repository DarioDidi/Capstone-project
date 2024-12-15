A Classified ads website that allows users to: register accounts, post ads, rate ads, comment on ads etc.
Fullstack django-html

Authentication:
views use django auth mixins to ensure a user is logged in for Creating, Updating and Deleting operations.
To test, create a user at "ads/register/" with usename, email, password1,password2 and login at "ads/login/" with username and password. Try creating an ad at "ads/new/" with a title, description, price(2 decimal places) and tag(single word) field. 

Users can request and auth token from "/api-token-auth/", for example:
endpoint: api-token-auth/      method: POST                                
Request: {
    "username": "johnDoe",
    "password": "password123"
}
Response: {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
}
