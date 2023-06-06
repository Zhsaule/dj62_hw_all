from django.urls import path
from measurement.views import CreateSensor, SensorMeasurementsView, \
                                ModifySensor, CreateMeasurement, SensorView


urlpatterns = [
    path('sensor/', SensorView.as_view()),
    path('sensor/new/', CreateSensor.as_view()),
    path('sensor/modify/<pk>/', ModifySensor.as_view()),
    path('sensor/measurement/', CreateMeasurement.as_view()),
    path('sensor/all/', SensorMeasurementsView.as_view()),
]
