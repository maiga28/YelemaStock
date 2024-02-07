from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def contact(request):
    return render(request, 'contact.html')



from django.test import SimpleTestCase, override_settings

def custom_page_not_found(request, unknown_path):
    return render(request, 'gestion/404.html', {'unknown_path': unknown_path}, status=404)



