# Wooling Around
Helping grandmothers around the world, buying the right wool, at the right price.


## Try it out 
The website is already live and ready to use!

Please visit  https://wooling-around.herokuapp.com/ to check it out.

## Installation Guide
  1. First clone this repository and move into the cloned directory.

  ```
  git clone https://github.com/sanket-pixel/wooling_around.git
  cd wooling_around
  ```
  Please run `cd wooling_around` only from the folder containing the cloned repo.

  2. Now create a virtual environment 
  ```
  python3 -m venv ./venv
  source ./venv/bin/activate 
  ```
  Note : for Windows run :
  ```
  .\venv\Scripts\activate.bat
  ```
  3. Install the requirements for this project using the `requirements.txt` file in the virtual environment.
  ```
    pip3 install -r requirements.txt
  ```
  Please ensure that all packages in the `requirements.txt` file are successfully installed.
  3. Make migrations for the  Django Models and migrate.
  ```
  python manage.py makemigrations 
  python manage.py migrate
  ```
  4. Finally, start up the local server using `runserver`
  ```
  python manage.py runserver
  ```
  
  ## Tech-Stack
  The project essentially scrapes data from a wool market place, everytime the homepage is loaded. 
  
  The project is entirely based in **Python** and uses the **Django** framework for creating the backend and frontend. For scraping, the python library called **Beautiful soup** is used. And for the front-end basic **html, css and js** template is used. The data after scraping is stored in a **local sqlite database**. The diagram below depicts an overview of the design.
  
<p align="center">
  <img src="https://github.com/sanket-pixel/wooling_around/blob/main/data/Overview.png" />
</p>

# Snapshot
Just for completeness, here is a screenshot of the app after being deployed.
<p align="center">
  <img src="https://github.com/sanket-pixel/wooling_around/blob/main/data/woolling-around.jpg" />
</p>

