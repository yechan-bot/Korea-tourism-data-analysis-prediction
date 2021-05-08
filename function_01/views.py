from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from tensorflow.python.keras.preprocessing import image
import numpy as np
from .drop_model import makeModel
from .models import *
from .forms import UploadFileForm
from PIL import Image
from django.views.decorators.csrf import csrf_exempt
import random
#########################

def function_01(request):
    return render(request, 'function_01.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            print(request.FILES['file'].name)
            a = "static/" + str(request.FILES['file'].name)
            b = str(request.FILES['file'].name)
            val = CNN_type(a)
            img = Image.open(a)
            best = sea_mou(val)
            return render(request, 'function_01.html', {"img":img, 'b':b, 'val':val, 'best':best})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open("static/"+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def CNN_type(f):
    img = image.load_img(f, target_size=(150, 150))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.
    model = makeModel()
    model.load_weights("function_01/k_model.h9")
    result = model.predict(img_tensor)
    if result < 0.5:
        img_type = "산"
        print(img_type)
        return img_type

    else :
        img_type = "바다"
        print(img_type)
        return img_type

def sea_mou(val):
    tt = val
    if tt == '산':
        listmou = '계양산', '한라산', '계룡산', '구봉산', '금강산'
        mou = random.sample(listmou, 2)
        return mou
    if tt == '바다':
        listmou = '해운대', '중문색달', '경포대', '강문해변', '상주은모래해변'
        mou = random.sample(listmou, 2)
        return mou