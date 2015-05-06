from django.views.generic.list import ListView

from photos.models import Photo


class PhotoView(ListView):
    model = Photo
