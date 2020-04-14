from rest_framework import serializers
from .models import Estimate


class EstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estimate
        fields = ("region", "name", "avgAge", "avgDailyIncomeInUSD", "avgDailyIncomePopulation", "periodType", "timeToElapse", "reportedCases", "population", "totalHospitalBeds")