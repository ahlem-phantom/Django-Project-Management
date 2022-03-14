# Project Management Workshop

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/ahlem-phantom/Django-Workshop.git
$ cd Django-Workshop
```

Create a virtual environment and activate it:

```sh
$ virtualenv env 
$ .\scripts\activate
```


Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Install django for the first time if you don't have it :
```sh
$ pip install django==3.2
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
