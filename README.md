# Wooling Around
Helping grandmothers around the world, buying the right wool, at the right price.


# Try it out 
The website is already live and ready to use!

Please visit  https://wooling-around.herokuapp.com/ to check it out.

# Installation Guide
  1. First clone this repository and move into the cloned directory.

  ```
  git clone https://github.com/sanket-pixel/wooling_around.git
  cd wooling_around
  ```
  Please run `cd wooling_around` only from the folder containing the cloned repo.

  2. Now install the requirements for this project using the `requirements.txt` file.
  ```
  pip3 install -r requirements.txt
  ```
  
  3. Make migrations for the  Django Models and migrate.
  ```
  python manage.py makemigrations 
  python manage.py migrate
  ```
  4. Finally, start up the local server using `runserver`
  ```
  python manage.py runserver
  ```
 
