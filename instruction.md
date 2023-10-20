This what I did to make it work



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
