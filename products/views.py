from django.shortcuts import render

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        username_is = "Francis Xavier using context"
        context = {"username_is": username_is}
    else:
        context = {"username_is": "Unknown"}
    template = 'base.html'
    return render(request, template, context)