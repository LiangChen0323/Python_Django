My first experience of Django  
install:

```
pip3 instal django
django-admin
```

to start a project with name password_generator

```
django-admin startproject password_generator
```

to start the service/server

```
python3 manage.py runserver
```

create an app called: generator  
`Projects vs. apps What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.`

```
python3 manage.py startapp generator

```

```
urls.py: lists urls to different views

views.py defiens request to differnt html pages

```
