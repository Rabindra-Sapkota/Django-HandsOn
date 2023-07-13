# Django Basic HandsOn
## Features Covered in Code
- Web-development framework &#9745;
- ORM (Object Relational Mapping) &#9745;
- URL Routing &#9745;
- HTML Templating &#9745;
- Form Handling &#9744; 
- Unit Testing &#9744;

## Setup
- Download and install Python
- Create virtual envrionment and setup
  - `python -m venv .venv`
  - Activate virtual environment with crtl+shift+p and choose interpreter
  - `.venv\Scripts\activate`
  - `pip install django`

- Clone repo and Go inside project folder
  - `django-admin startproject basic_django`
  - Above commands creates folders and files in it
    - manage.py &#8594; Used to run command
    - basic_django/\_\_init__.py &#8594; Indicate this folder contain Python code
    - basic_django/wsgi.py &#8594; Hooks for webserver such as Apache or Ngnix
    - basic_django/asi.py &#8594; Hooks for webserver such as Apache or Ngnix
    - basic_django/settings.py &#8594; Configuration
    - basic_django/urls.py &#8594; Routes web-request based on URL

- We can rename parent poject folder as basic_django-project to avoid confusions
- Or we could also go inside our project folder (say: basic_django-project) and create project as :
  - `django-admin startproject basic_django .`
- Run webserver
  - `cd basic_django`
  - `python manage.py runserver`
  - Click on: http://127.0.0.1:8000 to access web page
# Django APP
- Component within Django Project
- Portable unit of website functionality
- It has to be lowercase, no number, dashes or special character and in plular form
- Folder with set of Python files
- Each App has a specific purpose
## Creation
- Code
  - `python manage.py startapp favmusics` or `django-admin startapp favmusics`
  - Go inside basic_django/settings.py & append 'favmusics' (or appname.apps.className) to INSTALLED_APPS list
- Multiple Files will be created after creating app
  - app.py &#8594; Settings specific to app
  - models.py &#8594; Data layer for database schema
  - admin.py &#8594; Administrative interface for app
  - urls.py &#8594; URL routing specific to app
  - views.py &#8594; Logic & Control Flow for handling HTTP request and response
  - test.py &#8594; Unit Test
  - migrations/ &#8594; Changes to database
# Architecture (MVC i.e Model-View-Controller)
#### URL Pattern (basic_django/view.py) &#8594; Views (favmusics/views.py) &#8594; Templates(favmusics/templates)
- Views.py can fetch data from database (favmusics/models.py) before passing to template.

- Browser(url) &#8594; urls.py &#8594; views.py &#8594; template.html &#8594; Browser(html content)

  - When django receives web-request it uses URL pattern to decide which view to pass the request for handling
  - View define logic/control flow for program. It is python callable such as function
  - To perform query in database each view can leverage django models as needed
  - View can leverage template to help presentation layer

# Django Models
- Data layer for Django app
- Define database structure
- Allows us to query the database
- models.py contains set of models for django app
- model is class that is inherited from django.db.models.Model and defines database fields
- Example of code in models.py
  - ```
    from django.db import models
    
    class Customer(models.Model):
        SEX_CHOICES = [('M', 'Male'), ('F','Female')]
        name = models.CharField(max_length=30)
        dob = models.DateTimeField()
        sex = models.CharField(max_length=1, choices=SEX_CHOICES)
        address = models.CharField(blanks=True)
        street_number = models.IntegerField(null=True)
        favourite_music = models.ManyToManyField('music', blanks=True)
        profile_image = models.ImageField(upload_to='images/')
    
    class Music(models.Model):
        name = models.CharField(max_length=30)
  - In choices, first value is stored in Database & second for display
  - In charfield, max_length is required
  - In imagefield, upload_to is path where db images will be stored. Can be uploaded via admin panel
  - ID is created automatically in table
  - ManyToManyField links with another table in many-to-many relation. To solve it, third table will be created automatically
  - blanks and null attribute if field can store blank or null
  - Other Fields
    - Textual Data &#8594; CharField, TextField, EmailField, URLField
    - Numeric &#8594; IntegerField, DecimalField
    - Other &#8594; BooleanField, DateTimeField, ImageField
    - Relational &#8594; ForeignKey, ManyToManyField

# Database
## Setup
- By default our database will be setup in be stored in `db.sqlite3`
- To change the database configuration, goto basic_django/settings.py & make following changes (for postgres):
  ```
  DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': 'DB_NAME',
              'USER': 'DB_USER',
              'PASSWORD': 'DB_PASSWORD',
              'HOST': 'DB_HOST',
              'PORT': 'DB_PORT'
                    }
              }
## Migration
- To add model, add field, remove field, change field
- Code
  - Create python class in models.py
  - `python manage.py makemigrations` &#8594; Generate migration file
  - `python manage.py showmigrations` &#8594; Show migrations & which are applied seggregated by app
  - `python manage.py migrate` &#8594; Apply changes in database
  - `python manage.py migrate favmusics 2` &#8594; Apply only two changes of favmusics app in database
# Run Custom Script
- Create a folder `favmusics/management/commands` & add two files inside it
  - \_\_init__.py
  - load_data.py &#8594; Custom Script
- To run custom script enter below command
  - `python manage.py load_data`
# Create Admin Account
  - Run migration to make tables
    - `python manage.py makemigrations`
    - `python manage.py showmigrations`
    - `python manage.py migrate`
  - Create Superuser
    - `python manage.py createsuperuser`
    - Give username: Admin, Password: Admin@123
    - Email can be skipped.
    - Bypass validation as we are just testing
  - Start server and Login
    - `python manage.py runserver`
    - Click: http://127.0.0.1:8000/admin to access admin
## Configure table in Admin
- On favmusics/admin.py, add below code for admin
- Sample
  ```
  from .models import Customer
  
  @admin.register(Customer)
  class CustomerAdmin(admin.ModelAdmin):
      pass
- Pass shows id/repr of class. On clicking that we can see form with all fields
- If we want to see actual tabular representation in admin, instead of pass use below code
    - `list_display = ['name', 'song']`
    - To display song name instead of id use str in its model to say what to display
      - ```
        def __str__(self):
            return self.name
    - `list_filter` is used to control which fields can be used as filter in admin
    - `search_fields` can be used to control on which fields search applies to
    - `verbose_name` in models.py controls what to display as table name and field name in admin

  - Functions `has_delete_permission`, `has_add_permission`, `has_change_permission` as used to control if user can delete, add or modify records in admin
# Query data with ORM
  - `python manage.py shell`  &#8594;  Open Interactive shell
  - ```
    shell> from favmusics.models import Customer
    shell> Customer.objects.all()
    shell> customers = Customer.objects.all()
    shell> first_customer = customers[0]
    shell> first_customer.name
    shell> first_customer = Customer.objects.get(id=1)
    shell> first_customer.name
    shell> first_customer = Customer.objects.get(id=99999)
    shell> first_customer.name --> DoesnotExistError
    shell> first_customer = Customer.objects.get(age=23)  --> Get return more than 1 error
    shell> first_customer.name
  - To solve get return more than 1 error, we can use .filter() instead of .get() method
    - `Customer.objects.filter(age=23)`
  - Other filter options are .exclude(), .__starts_with(), .__icontains etc
    - ```
      Customer.objects.filter(age=23).exclude(name='rabi')
      Customer.objects.filter(name__icontains='ab')
      Customer.objects.filter(name__startswith='ru').exclude(age=23)  
    - To seach in foreign key within object use object_name.column and append select method to it
      ```
      shell> first_customer = Customer.objects.get(id=1)
      shell> first_customer.songs.all()
    - Shows all song associated with customer
    - Possible due to ManyToMany relation. (work in ForeignKey as well)

# URL Handler
  - Used for routing traffic from web-page to function with help of url pattern
  - url pattern is defined in file `basic_django/urls.py`
  - To add pattern, define path and add in urlpatterns variable
  - Has three argument: Pattern String, target view and name (optional field used in url tag)
  - When url is navigated in browser, it checks pattern in top down order until found. If not found it will return HTTP 404
  - For pattern <> is called capture group to capture value. We can cast and assign value to variable
  - Sample
    - ```
      from favmusics import views
      urlpatterns = [path('', views.home, name='home'), path('favouritemusic/<int:customer_id>/', views.favourite_music, name='favourite_music')]
      
  - When user navigate to /favouritemusic/1 (api endpoint), 1 is captured & store in customer_id then favourite_music view and called
  - Goto views file of favmusics and define function there
    - 
      ```
      from .models import Customer
      from django.http import HttpResponse, Http404
      
      def home(request):
          return HttpResponse('<p>Home<\p>')
          # customers = Customer.objects.all()
          # return render(request, 'home.html', {'customers': customers})
          # second is template, third is dict parameter to it.
          # Key will be utilized as variable
      
      def favourite_music(request, customer_id):
          return HttpResponse(f'<p>CustomerID: {customer_id}<\p>')

          '''
          try:
              customer = Customer.objects.get(id=customer_id)
          except Customer.DoesNotExist:
              raise Http404('Customer Not Found')
              return render(request, 'customer_details.html', {'customer': customer})
          '''
# Django Template
  - Generate dynamic html pages utilizing variables and template
  - Defined inside app
  - Sample
    - Create `templates` folder inside favmusic app
    - Create `home.html` & `customer_details.html` inside it as request are being passed to these templates from view.
    - For testing assign unique dummy value and see in browser
## Syntax
  - {{ variable }} &#8594;  Variable value is shown
  - {% tag %} &#8594;     loop, conditional & control logic
  - {{ variable|filter }} &#8594; Change format of variable before display

## Example
  - `<h3> {{ customer.name }} </h3>` # customer is obtained as variable from view
  - `<h3> {{ customer.name|capfirst }} </h3>` # Display making first letter capital
  - ```
    {% for customer in customers %}
        <li> {{ customer.name }} </li>
    {% endfor %}

## URL Pattern
  - Used to call api(view) from within code of html
  - Syntax:
    - `{% url 'home' %}`  # home is the name defined in path of urlpatterns
    - `{% url 'favourite_music' customer.id %}` # This view also has a parameter
  - Example:
    - ```
      <ul>
          {% for customer in customers %}
              <li> <a href="{% url 'favourite_music' customer.id %}"> {{ customer.name|capfirst}} </a> </li>
              {% endfor %}
      </ul>

## Inheritence
  - With inheritence, we can define base html and extend it to change only the dynamic part in it
  - base html defines which can be dynamic
  - Other code inherit base html and customize the dynamic part
  - All head, customization contents can be added in base template
  - Example:
    - In base html:<br>
    ```
    <!DOCTYPE HTML>
    <html>
        <head>
        </head>

        <body>
            <h1>From base</h1>
                {% block content %}
                {% endblock content %}
        </body>
    </html>

  - In inherited html
      ```
      {% extends "base.html" %}
      {% block content %}
  
      <h2>From template</h3>
      {% endblock content %}

## Integrate JS and CSS
  - Javascript, CSS, Logo & Images can be added in HTML
  - These files are called static files in django and added in staticfolder
  - static folder should be in top level of project where manage.py is located (static &#8594; main.js, style.css, images/)
  - On settings.py of project add
    - ```
      STATIC_URL = static/
      STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    - List of directory that django looks for serving static assets
    - BASE_DIR is directory where manage.py is located
  - To add static file goto top of base.html and add template
    - ```
      {% load static %}
        .........
        .........
      <image src="{% static 'images/logo.png' %}">
    - After static just add the path of file where it is present
# Desiging Project
  - Get Appriopriate theme from bootstrap. Example: https://getbootstrap.com/docs/5.3/examples/album/
  - Rightclick & view page source
  - Copy the source and paste in home.html
  - Remove href pointing to local. Add below code in head section:
    - `    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">`
  - Modify html to keep desired thing only
  - Keep single album as a template as other will be filled with django html template
# Project Flow
- Create project
- Create App
- Create Model for app & run migrations
- Run custom script to load data
- Create superuser
- Configure admin to validate data is loaded
- Work with fetching data from table
- Present data with django template
- Apply CSS, JS to webpage with static
