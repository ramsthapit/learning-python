from django.shortcuts import render

# Create your views here.


def index(request):
    my_dict = {"insert_content": "Hello, Im from first app"}
    return render(request, "first_app/index.htm", context=my_dict)
