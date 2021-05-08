from django.shortcuts import render
from .models import Pstr19, Pstr20, TourismExpenditure
from django.db.models import Q
######################### 회귀 분석
import pandas as pd
from sklearn.linear_model import LinearRegression
#########################
# Create your views here.

def analysis_03(request):
    posts_20 = Pstr20.objects.all()
    posts_19 = Pstr19.objects.all()
    tourism = TourismExpenditure.objects.filter(~Q(type="총소비") ,area="전국")
    menu = request.POST.get("menu", None)
    year = request.POST.get("menu_year", None)
    tourist = Pstr20.objects.all()
    if year == '2020':
        if menu == '지역별 관광객':
            return render(request, "analysis_03.html", {
                'tourist':tourist,
                'tourism': tourism,
                'posts':posts_20,
           })
        if menu == '지역별 관광수익':
            expend = Pstr20.objects.all()
            return render(request, "analysis_03.html", {
                'expend':expend,
                'tourism': tourism,
                'posts':posts_20,
           })
        if menu == '지역별 건물수':
            building = Pstr20.objects.all()
            return render(request, "analysis_03.html", {
                'building':building,
                'tourism': tourism,
                'posts':posts_20,
           })
    if year == '2019':
        if menu == '지역별 관광객':
            tourist_19 = Pstr19.objects.all()
            return render(request, "analysis_03.html", {
                'tourist':tourist_19,
                'tourism': tourism,
                'posts':posts_19,
           })
        if menu == '지역별 관광수익':
            expend_19 = Pstr19.objects.all()
            return render(request, "analysis_03.html", {
                'expend':expend_19,
                'tourism': tourism,
                'posts':posts_19,
           })
        if menu == '지역별 건물수':
            building_19 = Pstr19.objects.all()
            return render(request, "analysis_03.html", {
                'building':building_19,
                'tourism': tourism,
                'posts':posts_19,
           })


    return render(request, "analysis_03.html", {
        'tourism': tourism,
        'posts':posts_20,
        'tourist': tourist,
    })

def Building_Area(request):
    posts_20 = Pstr20.objects.all()
    tourism = TourismExpenditure.objects.filter(~Q(type="총소비") ,area="전국")
    tourist = Pstr20.objects.all()
    area = request.POST.get("area", None)
    if area == '서울':
        seoul = Pstr20.objects.filter(area="서울")
        return render(request, 'analysis_03.html', {
            'tourism': tourism,
            'posts':posts_20,
            'tourist': tourist,
            'this_area':seoul,
            })
    if area == '부산':
        seoul = Pstr20.objects.filter(area="부산")
        return render(request, 'analysis_03.html', {
            'tourism': tourism,
            'posts':posts_20,
            'tourist': tourist,
            'this_area':seoul,
            })
    if area == '대구':
        seoul = Pstr20.objects.filter(area="대구")
        return render(request, 'analysis_03.html', {
            'tourism': tourism,
            'posts':posts_20,
            'tourist': tourist,
            'this_area':seoul,
            })
    if area == '인천':
        seoul = Pstr20.objects.filter(area="인천")
        return render(request, 'analysis_03.html', {
            'tourism': tourism,
            'posts':posts_20,
            'tourist': tourist,
            'this_area':seoul,
            })
    if area == '광주':
        seoul = Pstr20.objects.filter(area="광주")
        return render(request, 'analysis_03.html', {
            'tourism': tourism,
            'posts':posts_20,
            'tourist': tourist,
            'this_area':seoul,
            })
    if area == '대전':
        seoul = Pstr20.objects.filter(area="대전")
        return render(request, 'analysis_03.html', {
            'tourism': tourism,
            'posts':posts_20,
            'tourist': tourist,
            'this_area':seoul,
            })
    if area == '울산':
        seoul = Pstr20.objects.filter(area="울산")
        return render(request, 'analysis_03.html', {
            'tourism': tourism,
            'posts':posts_20,
            'tourist': tourist,
            'this_area':seoul,
            })
    if area == '세종':
        seoul = Pstr20.objects.filter(area="세종")
        return render(request, 'analysis_03.html', {
            'tourism': tourism,
            'posts':posts_20,
            'tourist': tourist,
            'this_area':seoul,
            })
    if area == '경기':
        seoul = Pstr20.objects.filter(area="경기")
        return render(request, 'analysis_03.html', {
            'tourism': tourism,
            'posts':posts_20,
            'tourist': tourist,
            'this_area':seoul,
            })
    if area == '강원':
        seoul = Pstr20.objects.filter(area="강원")
        return render(request, 'analysis_03.html', {
            'tourism': tourism,
            'posts':posts_20,
            'tourist': tourist,
            'this_area':seoul,
            })
    if area == '충북':
        seoul = Pstr20.objects.filter(area="충북")
        return render(request, 'analysis_03.html', {
            'tourism': tourism,
            'posts':posts_20,
            'tourist': tourist,
            'this_area':seoul,
            })
    if area == '충남':
        seoul = Pstr20.objects.filter(area="충남")
        return render(request, 'analysis_03.html', {
            'tourism': tourism,
            'posts':posts_20,
            'tourist': tourist,
            'this_area':seoul,
            })
    if area == '전북':
        seoul = Pstr20.objects.filter(area="전북")
        return render(request, 'analysis_03.html', {
            'tourism': tourism,
            'posts':posts_20,
            'tourist': tourist,
            'this_area':seoul,
            })
    if area == '전남':
        seoul = Pstr20.objects.filter(area="전남")
        return render(request, 'analysis_03.html', {
            'tourism': tourism,
            'posts':posts_20,
            'tourist': tourist,
            'this_area':seoul,
            })
    if area == '경북':
        seoul = Pstr20.objects.filter(area="경북")
        return render(request, 'analysis_03.html', {
            'tourism': tourism,
            'posts':posts_20,
            'tourist': tourist,
            'this_area':seoul,
            })
    if area == '경남':
        seoul = Pstr20.objects.filter(area="경남")
        return render(request, 'analysis_03.html', {
            'tourism': tourism,
            'posts':posts_20,
            'tourist': tourist,
            'this_area':seoul,
            })
    if area == '제주':
        seoul = Pstr20.objects.filter(area="제주")
        return render(request, 'analysis_03.html', {
            'tourism': tourism,
            'posts':posts_20,
            'tourist': tourist,
            'this_area':seoul,
            })


def result(request):
    df = pd.read_csv("C:/djangowork/tourist/analysis_03/static/pstr_20.csv", encoding='cp949')
    posts_20 = Pstr20.objects.all()
    tourism = TourismExpenditure.objects.filter(~Q(type="총소비") ,area="전국")
    tourist = Pstr20.objects.all()
    n1 = request.POST.get("n1")
    n = int(n1)
    x = df[['Building']]
    y = df[['Tourist']]
    model = LinearRegression()
    model = model.fit(x, y)
    result = int(model.predict([[n]]))
    Accuracy = model.score(x, y)
    dfX = pd.DataFrame(df[['Building', 'Tourist']])
    dfy = pd.DataFrame(df[['Expenditure']])
    dff = pd.concat([dfX, dfy], axis=1)
    data = dff[["Building", "Tourist"]]
    label = dff["Expenditure"]
    model = LinearRegression()
    model = model.fit(data, label)
    result2 = int(model.predict([[n, result]]))
    Accuracy2 = model.score(data, label)
    # if n1 == "":
    #
    #     return render(request, 'analysis_03.html', {
    #         'result': result,
    #         'Accuracy': Accuracy,
    #         'tourism': tourism,
    #         'posts': posts_20,
    #         'tourist': tourist,
    #         'result2': result2,
    #         'Accuracy2': Accuracy2,
    #     })

    return render(request, 'analysis_03.html', {
            'result': result,
            'Accuracy': Accuracy,
            'tourism': tourism,
            'posts':posts_20,
            'tourist': tourist,
            'result2': result2,
            'Accuracy2': Accuracy2,
            })