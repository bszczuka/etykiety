from django.shortcuts import render, get_object_or_404
from .models import Label


def label_list(request):
    labels = Label.objects.all()
    return render(request, 'app/label/list.html', {'labels': labels})


def label(request, slug):
    label_details = get_object_or_404(Label, slug=slug)
    return render(request, 'app/label/show.html', {'label': label_details})
