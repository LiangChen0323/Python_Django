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

after adding app to the project, need to add app name to setting.py file

```

```
kill all the process associated with port 8000 on Linux
sudo fuser -k 8000/tcp
sudo lsof -t -i tcp:8000 | xargs kill -9 on Mac
sudo lsof -i tcp:8000
```

```
urls.py: lists urls to different views

views.py defiens request to differnt html pages

in html files
use "{% xxx %}" to navigate betwwen html files
xxx needs to be defined in urls.py file urlpatterns section

```

views.py

```
def home(request):

request has all the arguments pass from html files where it was triggered

request.GET.get("xxx")
xxx is the name of the element in html file
```

urls.py

```
defines urls and names which can be used in html files

in abc.html: <a href="{% url `xxx`%}">About</a>
where xxx is the name which was defined in urls.py

```

---

```
in models.py model is class for database
register at admin.py with object name
python3 manage.py makemigrations
python3 manage.py migrate
```

```
pip3 install Pillow if use models.ImageField
You have 17 unapplied migration(s). mean models have changed -> 'python manage.py migrate'
```

```
in settings.py define where to store image, video...
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
`media` will be the name of the folder under BASE_DIR where all the media resources go
```

```
in settings.py
MEDIA_URL = "/media/"    -> media can be changed to anything, only shows on weburl
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

in urls.py
from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

after create object and upload pic, can download pic from website
```

```
Problem:
“no such column” after adding a field to the model
apply python manage.py migrate my-app-name zero
to drop the table


```
