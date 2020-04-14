from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from rest_framework import generics
from .models import Estimate
from .serializers import EstimateSerializer



from django.views.decorators.csrf import csrf_exempt

import json

from covid19.models import Estimate


class ListEstimateView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer



def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

def get_data(request, data_name):
    if request.method == 'GET':
        try:
            data = Data.objects.get(name=data_name)
            response = json.dumps([{'region': data.region, 'name': data.name, 'avgAge': data.avgAge, 'avgDailyIncomeInUSD': data.avgDailyIncomeInUSD, 'avgDailyIncomePopulation': data.avgDailyIncomePopulation, 'periodType': data.periodType, 'timeToElapse': data.timeToElapse, 'reportedCases': data.reportedCases, 'population': data.population , 'totalHospitalBeds': data.totalHospitalBeds}])
        except:
            response = json.dumps([{ 'Error': 'No data with that name'}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def add_data(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        car_name = payload['car_name']
        region = payload['region']
        name = payload['name']
        avgAge = payload['avgAge']
        avgDailyIncomeInUSD = ['avgDailyIncomeInUSD']
        avgDailyIncomePopulation = ['avgDailyIncomePopulation']
        periodType = ['periodType']
        timeToElapse = ['timeToElapse']
        reportedCases = [reportedCases]
        population = [population]
        totalHospitalBeds = [totalHospitalBeds]
        data = Data(region=region, name=name, avgAge=avgAge, avgDailyIncomeInUSD=avgDailyIncomeInUSD, avgDailyIncomePopulation=avgDailyIncomePopulation, periodType=periodType, timeToElapse=timeToElapse, reportedCases=reportedCases, population=population, totalHospitalBeds=totalHospitalBeds)
        try:
            data.save()
            response = json.dumps([{ 'Success': 'data added successfully!'}])
        except:
            response = json.dumps([{ 'Error': 'data could not be added!'}])
    return HttpResponse(response, content_type='text/json')
