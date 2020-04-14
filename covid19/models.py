from django.db import models

# Create your models here.
class Estimate(models.Model):
    #region
	region = models.CharField(max_length=255)
	# #name
	name = models.CharField(max_length=255, default="region")
	# #average age
	avgAge = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
	# #average daily income in USD
	avgDailyIncomeInUSD = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
	# #average daily income population
	avgDailyIncomePopulation = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
	# #period type
	periodType = models.CharField(max_length=50, default="days")
	# #time to elapse
	timeToElapse = models.CharField(max_length=255, default=0)
	# #reported cases
	reportedCases = models.CharField(max_length=255, default=0)
	# #population
	population = models.CharField(max_length=255, default=0)
	# #total hospital beds
	totalHospitalBeds = models.CharField(max_length=255, default=0)
	def __str__(self):
		return self.name #"{} - {} - {} - {} - {} - {} - {} - {} - {} - {}".format(self.region, self.name, self.avgAge, self.avgDailyIncomeInUSD, self.avgDailyIncomePopulation, self.periodType, self.timeToElapse, self.reportedCases, self.population, self.totalHospitalBeds,)


