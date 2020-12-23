from django.urls import path
from .views import RoomView  #see views.py and #serializers.py for reference

urlpatterns = [
    path('room', RoomView.as_view()),   #.as_view (take this class and show me)
]




"""
::::::Instructions:::::

# Use this only if class changes

python3 manage.py makemigrations
python3 manage.py migrate

# else run directly

python3 manage.py runserver
"""