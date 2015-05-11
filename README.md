# Picha
This is a simple Django project meant to demonstrate the use of Celery with Django.

It is made up of two simple apps:
1. Photos - includes a periodic Celery task that gets photos from Flickr using their API
2. Feedback - includes a simple task to process a user submitted form

## How to get it running
1. Clone the repository into some directory
2. Install the Python packages in requirements.txt
3. Run Django

Code to achieve the above (may be different depending on your local set up):

    $ git clone https://github.com/moshthepitt/Picha.git picha
    $ cd picha
    $ mkvirtualenv picha
    $ pip install -r requirements.txt
    $ python manage.py runserver
