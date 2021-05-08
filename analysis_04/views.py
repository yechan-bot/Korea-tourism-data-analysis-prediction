from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def analysis_04(request):
    return render(request, 'analysis_04.html')

def result(request):
    import pandas as pd
    import matplotlib.pyplot as plt
    df = pd.read_csv('C:/djangowork/tourist/analysis_04/templates/traveler.csv', thousands=',')
    df
    import matplotlib.font_manager as fm
    from matplotlib import rc
    font_name = fm.FontProperties(fname="C:/djangowork/tourist/analysis_04/templates/a뉴고딕M.ttf").get_name()
    rc('font', family=font_name)

    year = request.GET.get("year", None)
    month = request.GET.get("year", None)

    if year == '2020년':
        if month == '2월':
            if year2 == '2020년':
                if month2 == '3월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render (request, 'analysis_04.html',{
                        'graph':plt })

        if month == '2월':
            if year2 == '2020년':
                if month2 == '4월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render (request, 'analysis_04.html',{
                        'graph':plt })

        if month == '2월':
            if year2 == '2020년':
                if month2 == '5월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render (request, 'analysis_04.html',{
                        'graph':plt })

        if month == '2월':
            if year2 == '2020년':
                if month2 == '6월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render (request, 'analysis_04.html',{
                        'graph':plt })

        if month == '2월':
            if year2 == '2020년':
                if month2 == '7월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render (request, 'analysis_04.html',{
                        'graph':plt })

        if month == '2월':
            if year2 == '2020년':
                if month2 == '8월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render (request, 'analysis_04.html',{
                        'graph':plt })

        if month == '2월':
            if year2 == '2020년':
                if month2 == '9월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render (request, 'analysis_04.html',{
                        'graph':plt })

        if month == '2월':
            if year2 == '2020년':
                if month2 == '10월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render (request, 'analysis_04.html',{
                        'graph':plt })

        if month == '2월':
            if year2 == '2020년':
                if month2 == '11월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render (request, 'analysis_04.html',{
                        'graph':plt })

        if month == '2월':
            if year2 == '2020년':
                if month2 == '12월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render (request, 'analysis_04.html',{
                        'graph':plt })

        if month == '2월':
            if year2 == '2021년':
                if month2 == '1월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render (request, 'analysis_04.html',{
                        'graph':plt })

        if month == '2월':
            if year2 == '2021년':
                if month2 == '2월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render (request, 'analysis_04.html',{
                        'graph':plt })


    if year == '2020년':
        if month == '3월':
            if year2 == '2020년':
                if month2 == '4월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '3월':
            if year2 == '2020년':
                if month2 == '5월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '3월':
            if year2 == '2020년':
                if month2 == '6월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '3월':
            if year2 == '2020년':
                if month2 == '7월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '3월':
            if year2 == '2020년':
                if month2 == '8월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '3월':
            if year2 == '2020년':
                if month2 == '9월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '3월':
            if year2 == '2020년':
                if month2 == '10월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '3월':
            if year2 == '2020년':
                if month2 == '11월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '3월':
            if year2 == '2020년':
                if month2 == '12월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '3월':
            if year2 == '2021년':
                if month2 == '1월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '3월':
            if year2 == '2021년':
                if month2 == '2월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})


    if year == '2020년':
        if month == '4월':
            if year2 == '2020년':
                if month2 == '5월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '4월':
            if year2 == '2020년':
                if month2 == '6월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '4월':
            if year2 == '2020년':
                if month2 == '7월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '4월':
            if year2 == '2020년':
                if month2 == '8월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '4월':
            if year2 == '2020년':
                if month2 == '9월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '4월':
            if year2 == '2020년':
                if month2 == '10월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '4월':
            if year2 == '2020년':
                if month2 == '11월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '4월':
            if year2 == '2020년':
                if month2 == '12월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '4월':
            if year2 == '2021년':
                if month2 == '1월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '4월':
            if year2 == '2020년':
                if month2 == '2월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

    if year == '2020년':
        if month == '5월':
            if year2 == '2020년':
                if month2 == '6월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '5월':
            if year2 == '2020년':
                if month2 == '7월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '5월':
            if year2 == '2020년':
                if month2 == '8월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '5월':
            if year2 == '2020년':
                if month2 == '9월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '5월':
            if year2 == '2020년':
                if month2 == '10월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '5월':
            if year2 == '2020년':
                if month2 == '11월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '5월':
            if year2 == '2020년':
                if month2 == '12월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '5월':
            if year2 == '2021년':
                if month2 == '1월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '5월':
            if year2 == '2020년':
                if month2 == '2월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})


    if year == '2020년':
        if month == '6월':
            if year2 == '2020년':
                if month2 == '7월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '6월':
            if year2 == '2020년':
                if month2 == '8월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '6월':
            if year2 == '2020년':
                if month2 == '9월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '6월':
            if year2 == '2020년':
                if month2 == '10월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '6월':
            if year2 == '2020년':
                if month2 == '11월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '6월':
            if year2 == '2020년':
                if month2 == '12월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '6월':
            if year2 == '2021년':
                if month2 == '1월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '6월':
            if year2 == '2021년':
                if month2 == '2월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})


    if year == '2020년':
        if month == '7월':
            if year2 == '2020년':
                if month2 == '8월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '7월':
            if year2 == '2020년':
                if month2 == '9월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '7월':
            if year2 == '2020년':
                if month2 == '10월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '7월':
            if year2 == '2020년':
                if month2 == '11월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '7월':
            if year2 == '2020년':
                if month2 == '12월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '7월':
            if year2 == '2021년':
                if month2 == '1월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '7월':
            if year2 == '2021년':
                if month2 == '2월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

    if year == '2020년':
        if month == '8월':
            if year2 == '2020년':
                if month2 == '9월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '8월':
            if year2 == '2020년':
                if month2 == '10월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '8월':
            if year2 == '2020년':
                if month2 == '11월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '8월':
            if year2 == '2020년':
                if month2 == '12월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '8월':
            if year2 == '2021년':
                if month2 == '1월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '8월':
            if year2 == '2021년':
                if month2 == '2월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})


    if year == '2020년':
        if month == '9월':
            if year2 == '2020년':
                if month2 == '10월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '9월':
            if year2 == '2020년':
                if month2 == '11월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '9월':
            if year2 == '2020년':
                if month2 == '12월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '9월':
            if year2 == '2021년':
                if month2 == '1월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '9월':
            if year2 == '2021년':
                if month2 == '2월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})


    if year == '2020년':
        if month == '10월':
            if year2 == '2020년':
                if month2 == '11월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '10월':
            if year2 == '2020년':
                if month2 == '11월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '10월':
            if year2 == '2020년':
                if month2 == '11월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '10월':
            if year2 == '2020년':
                if month2 == '11월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '10월':
            if year2 == '2020년':
                if month2 == '11월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})


    if year == '2020년':
        if month == '11월':
            if year2 == '2020년':
                if month2 == '12월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '11월':
            if year2 == '2021년':
                if month2 == '1월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

        if month == '11월':
            if year2 == '2021년':
                if month2 == '2월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})


    if year == '2021년':
        if month == '1월':
            if year2 == '2021년':
                if month2 == '2월':
                    plt.figure(figsize=(15, 7))
                    plt.bar(df['y/m'].iloc[0:2], df['personnel'].iloc[0:2])
                    plt.xlabel('날짜')
                    plt.ylabel('방한관광객 수')
                    return render(request, 'analysis_04.html', {
                        'graph': plt})

    return render(request, 'analysis_04.html',{"graph":'good'})




