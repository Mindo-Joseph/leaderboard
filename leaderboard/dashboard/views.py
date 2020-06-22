from django.shortcuts import render
import csv, io
from django.contrib import messages
from dashboard.models import Details
from django.contrib.auth.decorators import permission_required

@permission_required('admin.can_add_log_entry')

def details_upload(request):
    template = "upload.html"
    prompt = {
        'order': 'Input your csv in the following order: fullname, username,email,points'
    }
    if request.method == 'GET':
        return render(request,template,prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Only upload csv document')
    dataset = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(dataset)
    next(io_string)

    for column in csv.reader(io_string,delimiter = ',', quotechar = "|"):
        _, created = Details.objects.update_or_create(
            full_name = column[0],
            user_name = column[1],
            email = column[2],
            total_points = column[3]
        )
    context = {}
    return render(request,template,context)

def dashboard(request):
    all_details = Details.objects.all().order_by('-total_points')
    context = {
        'object_list':all_details
    }
    return render(request,'dashboard.html',context)