# Django-HandsOn

- Create virtual envrionment and setup
  - ```python -m venv .venv```
  - Activate virtual environment with crtl+shift+p and choose interpreter
  - ```.venv\Scripts\activate```
  - ```pip install django```
  - ```django-admin startproject django_project```

- Create database
  - ```cd django_project```
  - ```python manage.py makemigrations```
  - ```python manage.py migrate```

- Create Admin Account
  - ```python manage.py createsuperuser```
  - Give username: Admin, Password: Admin@123

- Run webserver
  - ```python manage.py runserver```
  - Click on the link to access web page
  - url/admin to access admin

- App: Portable unit of website functionality
  - Folder in main project folder
  - App name has to be all lowercase, no number, dashes and special character and in plular form
  - ```python manage.py startapp appname [allpages]```
  - Add appname (className from apps.py of app[allpages]) to INSTALLED_APP in settings.py in the form appname.apps.className

- Create static folder
  - Create static folder under app directory
  - Inside static folder create anoth folder with same name as app i.e allpages
  - inside this allpages create folders: images, css, javascript
  - create site-wide css inside css with name stylesheet.css
  - Add Some Google Font
    - Search google font combination for right google font
    - Goto fonts.google.com. Search montserrat (click on it & click + next to style), source sans pro and source code pro
    - Click on top right and @IMPORT
    - Copy code between style tag and paste in style-wide css
    - Copy CSS rule from font.google.com and paste as comment in css
    - Add other rule
  - Prepare Images in images directory
    - Prepare image for logo
    - Decrease opacity and prepare image for background
    - Goto color.adobe.com, upload image and choose the color theme
  
- On allpages app level folder, create a new folder called templates
  - Create a folder called allpages inside it
  - Create common template html as base.html. In base.html press ! and tab. VS code will fill template code
  - Create header, footer and nav tags

- Add bootstrap and font awesome
  - Search google for bootstrap CDN. Expand CSS, Copy link and paste in base.html with comment
  - Search google for font awesome CDN (with bootstrap link). Expand CSS. Copy and paste html in base.html

- Django template code
  - {% template code%}
  - {{ template variable }}
  - {# template comment #}

- In base.html add template code in main section
