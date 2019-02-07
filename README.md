<img src='https://img.shields.io/badge/Python3-Django2-yellowgreen.svg'/><img src='https://img.shields.io/badge/Javascript-json-yellowgreen.svg'/><img src='https://img.shields.io/badge/Without-DRF-green.svg'/>
# Django Chart without django rest framework
In this project I develop an application which shows a in chart the objects inserted in the database. Even I haven't been used django rest framework to serialize into a json, in the views I use json lib to render it in a json format.    

## Getting Started
* $ git clone https://github.com/victor-s-santos/django-chart-without-drf.git # to clone the repository
* cd django-authentication # to get in the new directory
* python -m venv .venv # to create the virtual environment
* python manage.py migrate # to migrate the models to database
* python manage.py runserverver # to run your local server

* As this repository don't use any additional lib, only pure django, don't be necessary to install anything with pip.

### Prerequisites
Python 3.X
Django 2.X #even this could be do with another previous django version, there are some fix to do in this case.

##Comments
Even the fact that I haven't been used a rest api to do this make it easier, it isn't the better idea. As I am not using a rest api, the system has been lost many functionalities like the authentication system, as well as it makes more difficult to use http methods. But I think at least for learning, it might be a good idea.

## Author
* **Victor Santos Silva** 

## Thank You. I hope it would be good for you!
