from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {"insert_content": "Go to /user to see user list"}
    return render(request, "AppTwo/index.html", context=my_dict)
