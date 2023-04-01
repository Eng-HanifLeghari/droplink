from django.shortcuts import render

# Create your views here.


def dot_link_pk(request):
    return render(request, 'dotlinkpk/index.html')