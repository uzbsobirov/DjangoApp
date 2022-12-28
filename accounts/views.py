from django.shortcuts import render


def signin(request):
    return render(request=request, template_name="signin.html")



def register(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request=request, template_name="signin.html")
