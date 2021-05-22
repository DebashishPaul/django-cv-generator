
from django.urls import path, include
from django.contrib import admin
from pdf.views import FormView, resume

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FormView , name='accept'),
    path('<int:id>/',resume, name="resume")
]
