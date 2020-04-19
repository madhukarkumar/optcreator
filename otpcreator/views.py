from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage


class Home(TemplateView):
    template_name = 'home.html'


# Create your views here.
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        file_data = uploaded_file.read().decode("utf-8")
        lines = file_data.split("\n")
        for line in lines:
            print(line.split(","))
        # store the uploaded file in media directory
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)



