This what I did to make it work


docker run -d \          
--name watchtower \
-v /var/run/docker.sock:/var/run/docker.sock \
containrrr/watchtower



I created a python enviroment using the command below 

- python3 -m venv myenv  # This creates a new virtual environment named 'myenv'

It is important note that it import to make sure that the app, which is like a directory template has django installed, when it's installed it is going to give things like the views, init, apps, models, and tests 

Then I activated the virtual environment
- source myenv/bin/activate  # This activates the new virtual environment

Then I used this command to make an, they said in the documentation that django projects have numerous apps, so that what I did 

Then what you're gonna do is make directory called templates and then in that directory you're going to have to make another directory which is the name of the app you're gonna make and then you will make the file called index.html

Make sure that you add, the app into the settings.py where you see installed apps

and in views you need make sure you add the index.html file 

You also want to add the index in the url file


- python manage.py startapp myapp



10/27/23 Instructions 



I set up the crude project as he said and he requested that we all have commits so I am gonna share sum of the commands that are gonna a lot you to make changes to the sql lite file 


this command allows you to run the server: python manage.py runserver(so running the html)





python manage.py shell: this commands allows you to run functions in the terminal

this command allows you to generate a random student object  

from myapp.factories import StudentFactory
students = StudentFactory.create_batch(5)


allows you to delete a student 

student = Student.objects.get()  # Get the student with primary key 1
student.delete()  # Delete that student

