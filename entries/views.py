from multiprocessing import context
from django.shortcuts import redirect, render

from .forms import EntryForm

from .models import Entry

# Create your views here.


def index_view(request):
    entries = Entry.objects.order_by('-date_posted')
    context = {'entries': entries}
    return render(request, 'entries/index.html', context)


def add_view(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntryForm()
    
    context = {'form': form}
    return render(request, 'entries/add.html', context)