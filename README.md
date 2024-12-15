A Classified ads website that allows users to: register accounts, post ads, rate ads, comment on ads etc.
Fullstack django-html

Authentication:
views use django auth mixins to ensure a user is logged in for Creating, Updating and Deleting operations.
to test, create a user at "ads/register/", login at "ads/login/" and try creating an ad at "ads/new/" with a title, description, price(2 decimal places) and tag(single word) field.
