# Awards

# Author
Laurette Mong'ina 
  
# Description  
A Django application that allows users to post their projects and they can be rated by other users based on design, usability, and content. Afterward, an average of the scores is taken and an average score taken.
##  Live Link  
https://gramawards.herokuapp.com/
  


 
## User Story  
  
* Sign in to the application to start using.  
* Upload a projects to the application. 
* Search for different projects using their titles.  
* See your profile.  
* Rate other users projects and be able to see the average scores for each.  
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 bash 
 https://github.com/LauretteMongina/Awards.git

##### Navigate into the folder and install requirements  
 bash 
cd awards
 pip install -r requirements.txt 

##### Install and activate Virtual  
 bash 
- python3 -m venv virtual - source virtual/bin/activate  
  
##### Install Dependencies  
 bash 
 pip install -r requirements.txt 
  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 bash 
python manage.py makemigrations app
  
 Now Migrate  
 bash 
 python manage.py migrate 

##### Run the application  
 bash 
 python manage.py runserver 
 
##### Running the application  
 bash 
 python manage.py server 

##### Testing the application  
 bash 
 python manage.py test 

Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 3.2.7](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* Search function not working.
  
## Contact Information   
If you have any question or contributions, please email me at [monginalaurette@gmail.com]  
  
## License 
MIT  
* Copyright (c) 2021 *Laurette