Flask-Pytest example

Flask server runs at http://127.0.0.1:8080

Files:
1) app.py - Flask server file
2) app_test.py - Pytest file that tests the API endpoints
3) requirements.txt - contains the required dependencies which are to be installed by Docker
4) Dockerfile - docker file which containerizes the flask-pytest app

Commands:
1) python app.py = runs the flask app and creates a localhost
2) pytest = runs the tests made for the API endpoints

APIs:
1) http://127.0.0.1:8080
   Greets the user
2) http://127.0.0.1:8080/fruits
   Returns the json list of the fruits

Screenshots:
