from django.shortcuts import render
from django.views import generic
from .models import Flat


def index(request):
    template_name = 'homepage/index.html'
    return render(request, template_name)


class FlatView(generic.ListView):
    model = Flat
    template_name = 'homepage/page.html'
    context_object_name = 'Flats'

    def get_queryset(self):
        return Flat.objects.all()

