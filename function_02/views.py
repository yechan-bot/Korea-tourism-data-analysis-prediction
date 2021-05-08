from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from keras.preprocessing import image
import numpy as np
from .bm1 import makeModel
from .models import *
from .forms import UploadFileForm
from PIL import Image
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def function_02(request):
    return render(request, 'function_02.html')

def function_02_test(request):
    return render(request, 'function_02_test.html')

def img_check(request):
    posts = BeverageTable.objects.filter(num=0)
    return render(request, 'test.html', {"posts": posts})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            print(request.FILES['file'].name)
            a = "static/" + str(request.FILES['file'].name)
            b = str(request.FILES['file'].name)
            val1, val2, val3 = Predict(a)
            re_con1 = BeverageTable.objects.filter(num=val1)
            re_con2 = BeverageTable.objects.filter(num=val2)
            re_con3 = BeverageTable.objects.filter(num=val3)
            val1 = val1 + 1
            val2 = val2 + 1
            val3 = val3 + 1
            return render(request, 'ok.html', {"re_con1": re_con1, "re_con2": re_con2, "re_con3": re_con3, 'b':b, 'val1': val1,'val2':val2, 'val3':val3})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open("static/"+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def Predict(f):
    img = image.load_img(f, target_size=(150, 150))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.
    model = makeModel()
    model.load_weights("function_02/real.model")
    result = model.predict(img_tensor)
    r1 = np.argmax(result)
    new_result = np.delete(result, r1)
    r2 = np.argmax(new_result)
    new_result2 = np.delete(new_result, r2)
    r3 = np.argmax(new_result2)
    return r1, r2, r3

def recheck():
    return render('ok.html')