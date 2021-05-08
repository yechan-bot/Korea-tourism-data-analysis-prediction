from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd
import numpy as np
import plotly.graph_objs as go
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib
# Create your views here.

df = pd.read_csv(r'C:\djangowork\tourist\analysis_02\static\csv\sample4.csv', encoding='utf-8', thousands=',')
df2 = pd.read_csv(r'C:\djangowork\tourist\analysis_02\static\csv\covid_social_dis_2.csv', encoding='utf-8')

df_seoul = df[df['Unnamed: 0'] == '서울특별시']
df_all = df[df['Unnamed: 0'] == '전국']
df_busan = df[df['Unnamed: 0'] == '부산광역시']
df_daegu = df[df['Unnamed: 0'] == '대구광역시']
df_incheon = df[df['Unnamed: 0'] == '인천광역시']
df_gwangju = df[df['Unnamed: 0'] == '광주광역시']
df_daejeon = df[df['Unnamed: 0'] == '대전광역시']
df_ulsan = df[df['Unnamed: 0'] == '울산광역시']
df_sejong = df[df['Unnamed: 0'] == '세종특별자치시']
df_gyeonggi = df[df['Unnamed: 0'] == '경기도']
df_gangwon = df[df['Unnamed: 0'] == '강원도']
df_chungbuk = df[df['Unnamed: 0'] == '충청북도']
df_chungnam = df[df['Unnamed: 0'] == '충청남도']
df_jeonbuk = df[df['Unnamed: 0'] == '전라북도']
df_jeonnam = df[df['Unnamed: 0'] == '전라남도']
df_gyeongbuk = df[df['Unnamed: 0'] == '경상북도']
df_gyeongnam = df[df['Unnamed: 0'] == '경상남도']
df_jeju = df[df['Unnamed: 0'] == '제주특별자치도']

df2_all = df2[df2['Unnamed: 0'] == '전국']
df2_seoul = df2[df2['Unnamed: 0'] == '서울특별시']
df2_busan = df2[df2['Unnamed: 0'] == '부산광역시']
df2_daegu = df2[df2['Unnamed: 0'] == '대구광역시']
df2_incheon = df2[df2['Unnamed: 0'] == '인천광역시']
df2_gwangju = df2[df2['Unnamed: 0'] == '광주광역시']
df2_daejeon = df2[df2['Unnamed: 0'] == '대전광역시']
df2_ulsan = df2[df2['Unnamed: 0'] == '울산광역시']
df2_sejong = df2[df2['Unnamed: 0'] == '세종특별자치시']
df2_gyeonggi = df2[df2['Unnamed: 0'] == '경기도']
df2_gangwon = df2[df2['Unnamed: 0'] == '강원도']
df2_chungbuk = df2[df2['Unnamed: 0'] == '충청북도']
df2_chungnam = df2[df2['Unnamed: 0'] == '충청남도']
df2_jeonbuk = df2[df2['Unnamed: 0'] == '전라북도']
df2_jeonnam = df2[df2['Unnamed: 0'] == '전라남도']
df2_gyeongbuk = df2[df2['Unnamed: 0'] == '경상북도']
df2_gyeongnam = df2[df2['Unnamed: 0'] == '경상남도']
df2_jeju = df2[df2['Unnamed: 0'] == '제주특별자치도']

df_all = df_all.T[2:]
df_all = df_all.reset_index().rename(
    columns={'index': 'date', 0: 'all_local', 1: 'all_out', 2: 'all_fore', 3: 'all_of'})
df_seoul = df_seoul.T[2:]
df_seoul = df_seoul.reset_index().rename(
    columns={'index': 'date', 4: 'seoul_local', 5: 'seoul_out', 6: 'seoul_fore', 7: 'seoul_of'})
df_busan = df_busan.T[2:]
df_busan = df_busan.reset_index().rename(
    columns={'index': 'date', 8: 'busan_local', 9: 'busan_out', 10: 'busan_fore', 11: 'busan_of'})
df_daegu = df_daegu.T[2:]
df_daegu = df_daegu.reset_index().rename(
    columns={'index': 'date', 12: 'daegu_local', 13: 'daegu_out', 14: 'daegu_fore', 15: 'daegu_of'})
df_incheon = df_incheon.T[2:]
df_incheon = df_incheon.reset_index().rename(
    columns={'index': 'date', 16: 'incheon_local', 17: 'incheon_out', 18: 'incheon_fore', 19: 'incheon_of'})
df_gwangju = df_gwangju.T[2:]
df_gwangju = df_gwangju.reset_index().rename(
    columns={'index': 'date', 20: 'gwangju_local', 21: 'gwangju_out', 22: 'gwangju_fore', 23: 'gwangju_of'})
df_daejeon = df_daejeon.T[2:]
df_daejeon = df_daejeon.reset_index().rename(
    columns={'index': 'date', 24: 'daejeon_local', 25: 'daejeon_out', 26: 'daejeon_fore', 27: 'daejeon_of'})
df_ulsan = df_ulsan.T[2:]
df_ulsan = df_ulsan.reset_index().rename(
    columns={'index': 'date', 28: 'ulsan_local', 29: 'ulsan_out', 30: 'ulsan_fore', 31: 'ulsan_of'})
df_sejong = df_sejong.T[2:]
df_sejong = df_sejong.reset_index().rename(
    columns={'index': 'date', 32: 'sejong_local', 33: 'sejong_out', 34: 'sejong_fore', 35: 'sejong_of'})
df_gyeonggi = df_gyeonggi.T[2:]
df_gyeonggi = df_gyeonggi.reset_index().rename(
    columns={'index': 'date', 36: 'gyeonggi_local', 37: 'gyeonggi_out', 38: 'gyeonggi_fore', 39: 'gyeonggi_of'})
df_gangwon = df_gangwon.T[2:]
df_gangwon = df_gangwon.reset_index().rename(
    columns={'index': 'date', 40: 'gangwon_local', 41: 'gangwon_out', 42: 'gangwon_fore', 43: 'gangwon_of'})
df_chungbuk = df_chungbuk.T[2:]
df_chungbuk = df_chungbuk.reset_index().rename(
    columns={'index': 'date', 44: 'chungbuk_local', 45: 'chungbuk_out', 46: 'chungbuk_fore', 47: 'chungbuk_of'})
df_chungnam = df_chungnam.T[2:]
df_chungnam = df_chungnam.reset_index().rename(
    columns={'index': 'date', 48: 'chungnam_local', 49: 'chungnam_out', 50: 'chungnam_fore', 51: 'chungnam_of'})
df_jeonbuk = df_jeonbuk.T[2:]
df_jeonbuk = df_jeonbuk.reset_index().rename(
    columns={'index': 'date', 52: 'jeonbuk_local', 53: 'jeonbuk_out', 54: 'jeonbuk_fore', 55: 'jeonbuk_of'})
df_jeonnam = df_jeonnam.T[2:]
df_jeonnam = df_jeonnam.reset_index().rename(
    columns={'index': 'date', 56: 'jeonnam_local', 57: 'jeonnam_out', 58: 'jeonnam_fore', 59: 'jeonnam_of'})
df_gyeongbuk = df_gyeongbuk.T[2:]
df_gyeongbuk = df_gyeongbuk.reset_index().rename(
    columns={'index': 'date', 60: 'gyeongbuk_local', 61: 'gyeongbuk_out', 62: 'gyeongbuk_fore', 63: 'gyeongbuk_of'})
df_gyeongnam = df_gyeongnam.T[2:]
df_gyeongnam = df_gyeongnam.reset_index().rename(
    columns={'index': 'date', 64: 'gyeongnam_local', 65: 'gyeongnam_out', 66: 'gyeongnam_fore', 67: 'gyeongnam_of'})
df_jeju = df_jeju.T[2:]
df_jeju = df_jeju.reset_index().rename(
    columns={'index': 'date', 68: 'jeju_local', 69: 'jeju_out', 70: 'jeju_fore', 71: 'jeju_of'})

df2_all = df2_all.T[2:]
df2_all = df2_all.reset_index().rename(columns={'index': 'date', 0: 'rate'})
df2_seoul = df2_seoul.T[2:]
df2_seoul = df2_seoul.reset_index().rename(columns={'index': 'date', 1: 'rate'})
df2_busan = df2_busan.T[2:]
df2_busan = df2_busan.reset_index().rename(columns={'index': 'date', 2: 'rate'})
df2_daegu = df2_daegu.T[2:]
df2_daegu = df2_daegu.reset_index().rename(columns={'index': 'date', 3: 'rate'})
df2_incheon = df2_incheon.T[2:]
df2_incheon = df2_incheon.reset_index().rename(columns={'index': 'date', 4: 'rate'})
df2_gwangju = df2_gwangju.T[2:]
df2_gwangju = df2_gwangju.reset_index().rename(columns={'index': 'date', 5: 'rate'})
df2_daejeon = df2_daejeon.T[2:]
df2_daejeon = df2_daejeon.reset_index().rename(columns={'index': 'date', 6: 'rate'})
df2_ulsan = df2_ulsan.T[2:]
df2_ulsan = df2_ulsan.reset_index().rename(columns={'index': 'date', 7: 'rate'})
df2_sejong = df2_sejong.T[2:]
df2_sejong = df2_sejong.reset_index().rename(columns={'index': 'date', 8: 'rate'})
df2_gyeonggi = df2_gyeonggi.T[2:]
df2_gyeonggi = df2_gyeonggi.reset_index().rename(columns={'index': 'date', 9: 'rate'})
df2_gangwon = df2_gangwon.T[2:]
df2_gangwon = df2_gangwon.reset_index().rename(columns={'index': 'date', 10: 'rate'})
df2_chungbuk = df2_chungbuk.T[2:]
df2_chungbuk = df2_chungbuk.reset_index().rename(columns={'index': 'date', 11: 'rate'})
df2_chungnam = df2_chungnam.T[2:]
df2_chungnam = df2_chungnam.reset_index().rename(columns={'index': 'date', 12: 'rate'})
df2_jeonbuk = df2_jeonbuk.T[2:]
df2_jeonbuk = df2_jeonbuk.reset_index().rename(columns={'index': 'date', 13: 'rate'})
df2_jeonnam = df2_jeonnam.T[2:]
df2_jeonnam = df2_jeonnam.reset_index().rename(columns={'index': 'date', 14: 'rate'})
df2_gyeongbuk = df2_gyeongbuk.T[2:]
df2_gyeongbuk = df2_gyeongbuk.reset_index().rename(columns={'index': 'date', 15: 'rate'})
df2_gyeongnam = df2_gyeongnam.T[2:]
df2_gyeongnam = df2_gyeongnam.reset_index().rename(columns={'index': 'date', 16: 'rate'})
df2_jeju = df2_jeju.T[2:]
df2_jeju = df2_jeju.reset_index().rename(columns={'index': 'date', 17: 'rate'})

def button1(request):

    btn = request.GET.get('btn1', None)

    if btn == '전국':
        fig1 = plot([Scatter(x=df_all['date'], y=df_all['all_fore'],
                                 mode='lines',
                                 opacity=0.8, marker_color='green')],
                        output_type='div')

        fig2 = plot([go.Bar(x=df2_all['date'], y=df2_all['rate'],
                             opacity=0.8, name='거리두기 단계',
                            marker_color='red')],
                    output_type='div')

        return render(request, 'analysis_02.html', context={'graph1':fig1, 'graph2':fig2, 'sa':btn})

    if btn == '서울특별시':
        fig1 = plot([Scatter(x=df_seoul['date'], y=df_seoul['seoul_fore'],
                             mode='lines',
                             opacity=0.8, marker_color='green')],
                    output_type='div')

        fig2 = plot([go.Bar(x=df2_seoul['date'], y=df2_seoul['rate'],
                            opacity=0.8, marker_color='red')],
                    output_type='div')

        return render(request, 'analysis_02.html', context={'graph1': fig1, 'graph2': fig2, 'sa':btn})
    if btn == '부산광역시':
        fig1 = plot([Scatter(x=df_busan['date'], y=df_busan['busan_fore'],
                                 mode='lines',
                                 opacity=0.8, marker_color='green')],
                        output_type='div')

        fig2 = plot([go.Bar(x=df2_busan['date'], y=df2_busan['rate'],
                             opacity=0.8, name='거리두기 단계',
                            marker_color='red')],
                    output_type='div')

        return render(request, 'analysis_02.html', context={'graph1':fig1, 'graph2':fig2, 'sa':btn})
    if btn == '대구광역시':
        fig1 = plot([Scatter(x=df_daegu['date'], y=df_daegu['daegu_fore'],
                             mode='lines',
                             opacity=0.8, marker_color='green')],
                    output_type='div')

        fig2 = plot([go.Bar(x=df2_daegu['date'], y=df2_daegu['rate'],
                            opacity=0.8, name='거리두기 단계',
                            marker_color='red')],
                    output_type='div')

        return render(request, 'analysis_02.html', context={'graph1': fig1, 'graph2': fig2, 'sa': btn})
    if btn == '인천광역시':
        fig1 = plot([Scatter(x=df_incheon['date'], y=df_incheon['incheon_fore'],
                             mode='lines',
                             opacity=0.8, marker_color='green')],
                    output_type='div')

        fig2 = plot([go.Bar(x=df2_incheon['date'], y=df2_incheon['rate'],
                            opacity=0.8, name='거리두기 단계',
                            marker_color='red')],
                    output_type='div')

        return render(request, 'analysis_02.html', context={'graph1': fig1, 'graph2': fig2, 'sa': btn})
    if btn == '광주광역시':
        fig1 = plot([Scatter(x=df_gwangju['date'], y=df_gwangju['gwangju_fore'],
                             mode='lines',
                             opacity=0.8, marker_color='green')],
                    output_type='div')

        fig2 = plot([go.Bar(x=df2_gwangju['date'], y=df2_gwangju['rate'],
                            opacity=0.8, name='거리두기 단계',
                            marker_color='red')],
                    output_type='div')

        return render(request, 'analysis_02.html', context={'graph1': fig1, 'graph2': fig2, 'sa': btn})
    if btn == '대전광역시':
        fig1 = plot([Scatter(x=df_daejeon['date'], y=df_daejeon['daejeon_fore'],
                             mode='lines',
                             opacity=0.8, marker_color='green')],
                    output_type='div')

        fig2 = plot([go.Bar(x=df2_daejeon['date'], y=df2_daejeon['rate'],
                            opacity=0.8, name='거리두기 단계',
                            marker_color='red')],
                    output_type='div')

        return render(request, 'analysis_02.html', context={'graph1': fig1, 'graph2': fig2, 'sa': btn})
    if btn == '울산광역시':
        fig1 = plot([Scatter(x=df_ulsan['date'], y=df_ulsan['ulsan_fore'],
                             mode='lines',
                             opacity=0.8, marker_color='green')],
                    output_type='div')

        fig2 = plot([go.Bar(x=df2_ulsan['date'], y=df2_ulsan['rate'],
                            opacity=0.8, name='거리두기 단계',
                            marker_color='red')],
                    output_type='div')

        return render(request, 'analysis_02.html', context={'graph1': fig1, 'graph2': fig2, 'sa': btn})
    if btn == '세종특별자치시':
        fig1 = plot([Scatter(x=df_sejong['date'], y=df_sejong['sejong_fore'],
                             mode='lines',
                             opacity=0.8, marker_color='green')],
                    output_type='div')

        fig2 = plot([go.Bar(x=df2_sejong['date'], y=df2_sejong['rate'],
                            opacity=0.8, name='거리두기 단계',
                            marker_color='red')],
                    output_type='div')

        return render(request, 'analysis_02.html', context={'graph1': fig1, 'graph2': fig2, 'sa': btn})
    if btn == '경기도':
        fig1 = plot([Scatter(x=df_gyeonggi['date'], y=df_gyeonggi['gyeonggi_fore'],
                             mode='lines',
                             opacity=0.8, marker_color='green')],
                    output_type='div')

        fig2 = plot([go.Bar(x=df2_gyeonggi['date'], y=df2_gyeonggi['rate'],
                            opacity=0.8, name='거리두기 단계',
                            marker_color='red')],
                    output_type='div')

        return render(request, 'analysis_02.html', context={'graph1': fig1, 'graph2': fig2, 'sa': btn})
    if btn == '강원도':
        fig1 = plot([Scatter(x=df_gangwon['date'], y=df_gangwon['gangwon_fore'],
                             mode='lines',
                             opacity=0.8, marker_color='green')],
                    output_type='div')

        fig2 = plot([go.Bar(x=df2_gangwon['date'], y=df2_gangwon['rate'],
                            opacity=0.8, name='거리두기 단계',
                            marker_color='red')],
                    output_type='div')

        return render(request, 'analysis_02.html', context={'graph1': fig1, 'graph2': fig2, 'sa': btn})
    if btn == '충청북도':
        fig1 = plot([Scatter(x=df_chungbuk['date'], y=df_chungbuk['chungbuk_fore'],
                             mode='lines',
                             opacity=0.8, marker_color='green')],
                    output_type='div')

        fig2 = plot([go.Bar(x=df2_chungbuk['date'], y=df2_chungbuk['rate'],
                            opacity=0.8, name='거리두기 단계',
                            marker_color='red')],
                    output_type='div')

        return render(request, 'analysis_02.html', context={'graph1': fig1, 'graph2': fig2, 'sa': btn})
    if btn == '충청남도':
        fig1 = plot([Scatter(x=df_chungnam['date'], y=df_chungnam['chungnam_fore'],
                             mode='lines',
                             opacity=0.8, marker_color='green')],
                    output_type='div')

        fig2 = plot([go.Bar(x=df2_chungnam['date'], y=df2_chungnam['rate'],
                            opacity=0.8, name='거리두기 단계',
                            marker_color='red')],
                    output_type='div')

        return render(request, 'analysis_02.html', context={'graph1': fig1, 'graph2': fig2, 'sa': btn})
    if btn == '전라북도':
        fig1 = plot([Scatter(x=df_jeonbuk['date'], y=df_jeonbuk['jeonbuk_fore'],
                             mode='lines',
                             opacity=0.8, marker_color='green')],
                    output_type='div')

        fig2 = plot([go.Bar(x=df2_jeonbuk['date'], y=df2_jeonbuk['rate'],
                            opacity=0.8, name='거리두기 단계',
                            marker_color='red')],
                    output_type='div')

        return render(request, 'analysis_02.html', context={'graph1': fig1, 'graph2': fig2, 'sa': btn})
    if btn == '전라남도':
        fig1 = plot([Scatter(x=df_jeonnam['date'], y=df_jeonnam['jeonnam_fore'],
                             mode='lines',
                             opacity=0.8, marker_color='green')],
                    output_type='div')

        fig2 = plot([go.Bar(x=df2_jeonnam['date'], y=df2_jeonnam['rate'],
                            opacity=0.8, name='거리두기 단계',
                            marker_color='red')],
                    output_type='div')

        return render(request, 'analysis_02.html', context={'graph1': fig1, 'graph2': fig2, 'sa': btn})
    if btn == '경상북도':
        fig1 = plot([Scatter(x=df_gyeongbuk['date'], y=df_gyeongbuk['gyeongbuk_fore'],
                             mode='lines',
                             opacity=0.8, marker_color='green')],
                    output_type='div')

        fig2 = plot([go.Bar(x=df2_gyeongbuk['date'], y=df2_gyeongbuk['rate'],
                            opacity=0.8, name='거리두기 단계',
                            marker_color='red')],
                    output_type='div')

        return render(request, 'analysis_02.html', context={'graph1': fig1, 'graph2': fig2, 'sa': btn})
    if btn == '경상남도':
        fig1 = plot([Scatter(x=df_gyeongnam['date'], y=df_gyeongnam['gyeongnam_fore'],
                             mode='lines',
                             opacity=0.8, marker_color='green')],
                    output_type='div')

        fig2 = plot([go.Bar(x=df2_gyeongnam['date'], y=df2_gyeongnam['rate'],
                            opacity=0.8, name='거리두기 단계',
                            marker_color='red')],
                    output_type='div')

        return render(request, 'analysis_02.html', context={'graph1': fig1, 'graph2': fig2, 'sa': btn})
    if btn == '제주특별자치도':
        fig1 = plot([Scatter(x=df_jeju['date'], y=df_jeju['jeju_fore'],
                             mode='lines',
                             opacity=0.8, marker_color='green')],
                    output_type='div')

        fig2 = plot([go.Bar(x=df2_jeju['date'], y=df2_jeju['rate'],
                            opacity=0.8, name='거리두기 단계',
                            marker_color='red')],
                    output_type='div')

        return render(request, 'analysis_02.html', context={'graph1': fig1, 'graph2': fig2, 'sa': btn})

    # return render(request, 'analysis_02.html', {'graph': None})

def analysis_02(request):
    return render(request, 'analysis_02.html')

def result(request):

    seoul_rate_data = df2_seoul['rate']
    seoul_fore_target = df_seoul['seoul_fore']

    x_train_seoul_fore, x_test_seoul_fore, y_train_seoul_fore, y_test_seoul_fore = \
        train_test_split(seoul_rate_data, seoul_fore_target,\
                         test_size=0.2, shuffle=True, random_state=2019)

    def fit_polynomial(x, y, degree):
        model = LinearRegression()
        model.fit(np.vander(x, degree + 1), y)
        return model

    def apply_polynomial(model, x):
        degree = model.coef_.size - 1
        y = model.predict(np.vander(x, degree + 1))
        return y

    model_seoul_fore = fit_polynomial(x_train_seoul_fore, y_train_seoul_fore, 6)

    p_seoul_fore = apply_polynomial(model_seoul_fore, x_test_seoul_fore)

    nat = request.GET.get("nat", None)
    type = request.GET.get("type", None)
    dis = request.GET.get("dis", None)

    if nat == '전국':
        #if type == '외국인':
            if dis == '1단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\all_fore.pkl")
                result = np.around(apply_polynomial(model, [1]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '2단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\all_fore.pkl")
                result = np.around(apply_polynomial(model, [2]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '3단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\all_fore.pkl")
                result = np.around(apply_polynomial(model, [3]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
    if nat == '서울특별시':
        #if type == '외국인':
            if dis == '1단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\seoul_fore.pkl")
                result = np.around(apply_polynomial(model, [1]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '2단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\seoul_fore.pkl")
                result = np.around(apply_polynomial(model, [2]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '3단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\seoul_fore.pkl")
                result = np.around(apply_polynomial(model, [3]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
    if nat == '부산광역시':
        #if type == '외국인':
            if dis == '1단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\busan_fore.pkl")
                result = np.around(apply_polynomial(model, [1]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '2단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\busan_fore.pkl")
                result = np.around(apply_polynomial(model, [2]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '3단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\busan_fore.pkl")
                result = np.around(apply_polynomial(model, [3]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
    if nat == '대구광역시':
        #if type == '외국인':
            if dis == '1단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\daegu_fore.pkl")
                result = np.around(apply_polynomial(model, [1]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '2단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\daegu_fore.pkl")
                result = np.around(apply_polynomial(model, [2]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '3단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\daegu_fore.pkl")
                result = np.around(apply_polynomial(model, [3]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
    if nat == '인천광역시':
        #if type == '외국인':
            if dis == '1단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\incheon_fore.pkl")
                result = np.around(apply_polynomial(model, [1]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '2단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\incheon_fore.pkl")
                result = np.around(apply_polynomial(model, [2]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '3단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\incheon_fore.pkl")
                result = np.around(apply_polynomial(model, [3]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
    if nat == '광주광역시':
        #if type == '외국인':
            if dis == '1단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\gwangju_fore.pkl")
                result = np.around(apply_polynomial(model, [1]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '2단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\gwangju_fore.pkl")
                result = np.around(apply_polynomial(model, [2]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '3단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\gwangju_fore.pkl")
                result = np.around(apply_polynomial(model, [3]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
    if nat == '대전광역시':
        #if type == '외국인':
            if dis == '1단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\daejeon_fore.pkl")
                result = np.around(apply_polynomial(model, [1]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '2단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\daejeon_fore.pkl")
                result = np.around(apply_polynomial(model, [2]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '3단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\daejeon_fore.pkl")
                result = np.around(apply_polynomial(model, [3]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
    if nat == '울산광역시':
        #if type == '외국인':
            if dis == '1단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\ulsan_fore.pkl")
                result = np.around(apply_polynomial(model, [1]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '2단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\ulsan_fore.pkl")
                result = np.around(apply_polynomial(model, [2]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '3단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\ulsan_fore.pkl")
                result = np.around(apply_polynomial(model, [3]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
    if nat == '세종특별자치시':
        #if type == '외국인':
            if dis == '1단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\sejong_fore.pkl")
                result = np.around(apply_polynomial(model, [1]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '2단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\sejong_fore.pkl")
                result = np.around(apply_polynomial(model, [2]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '3단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\sejong_fore.pkl")
                result = np.around(apply_polynomial(model, [3]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
    if nat == '경기도':
        #if type == '외국인':
            if dis == '1단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\gyeonggi_fore.pkl")
                result = np.around(apply_polynomial(model, [1]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '2단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\gyeonggi_fore.pkl")
                result = np.around(apply_polynomial(model, [2]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '3단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\gyeonggi_fore.pkl")
                result = np.around(apply_polynomial(model, [3]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
    if nat == '강원도':
        #if type == '외국인':
            if dis == '1단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\gangwon_fore.pkl")
                result = np.around(apply_polynomial(model, [1]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '2단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\gangwon_fore.pkl")
                result = np.around(apply_polynomial(model, [2]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '3단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\gangwon_fore.pkl")
                result = np.around(apply_polynomial(model, [3]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
    if nat == '충청북도':
        #if type == '외국인':
            if dis == '1단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\chungbuk_fore.pkl")
                result = np.around(apply_polynomial(model, [1]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '2단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\chungbuk_fore.pkl")
                result = np.around(apply_polynomial(model, [2]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '3단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\chungbuk_fore.pkl")
                result = np.around(apply_polynomial(model, [3]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
    if nat == '충청남도':
        #if type == '외국인':
            if dis == '1단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\chungnam_fore.pkl")
                result = np.around(apply_polynomial(model, [1]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '2단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\chungnam_fore.pkl")
                result = np.around(apply_polynomial(model, [2]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '3단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\chungnam_fore.pkl")
                result = np.around(apply_polynomial(model, [3]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
    if nat == '전라북도':
        #if type == '외국인':
            if dis == '1단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\jeonbuk_fore.pkl")
                result = np.around(apply_polynomial(model, [1]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '2단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\jeonbuk_fore.pkl")
                result = np.around(apply_polynomial(model, [2]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '3단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\jeonbuk_fore.pkl")
                result = np.around(apply_polynomial(model, [3]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
    if nat == '전라남도':
        #if type == '외국인':
            if dis == '1단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\jeonnam_fore.pkl")
                result = np.around(apply_polynomial(model, [1]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '2단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\jeonnam_fore.pkl")
                result = np.around(apply_polynomial(model, [2]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '3단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\jeonnam_fore.pkl")
                result = np.around(apply_polynomial(model, [3]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
    if nat == '경상북도':
        #if type == '외국인':
            if dis == '1단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\gyeongbuk_fore.pkl")
                result = np.around(apply_polynomial(model, [1]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '2단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\gyeongbuk_fore.pkl")
                result = np.around(apply_polynomial(model, [2]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '3단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\gyeongbuk_fore.pkl")
                result = np.around(apply_polynomial(model, [3]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
    if nat == '경상남도':
        #if type == '외국인':
            if dis == '1단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\gyeongnam_fore.pkl")
                result = np.around(apply_polynomial(model, [1]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '2단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\gyeongnam_fore.pkl")
                result = np.around(apply_polynomial(model, [2]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '3단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\gyeongnam_fore.pkl")
                result = np.around(apply_polynomial(model, [3]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
    if nat == '제주특별자치도':
        #if type == '외국인':
            if dis == '1단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\jeju_fore.pkl")
                result = np.around(apply_polynomial(model, [1]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '2단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\jeju_fore.pkl")
                result = np.around(apply_polynomial(model, [2]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})
            if dis == '3단계':
                model = joblib.load(filename=r"C:\djangowork\tourist\analysis_02\static\csv\jeju_fore.pkl")
                result = np.around(apply_polynomial(model, [3]))
                return render(request, 'analysis_02.html', {
                    'dd':dis,
                    'nn':nat,
                    'result2':result})

    return render(request, 'analysis_02.html', {"result2":1})



# def analysis_02_1(request):
#     return render(request, 'analysis_02_1.html')
#
# def analysis_02_2(request):
#     return render(request, 'analysis_02_2.html')
#
# def analysis_02_3(request):
#     return render(request, 'analysis_02_3.html')