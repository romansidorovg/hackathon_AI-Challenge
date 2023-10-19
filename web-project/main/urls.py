from django.urls import path

from main.views import MainView, GetFormData, AIView

app_name = 'main'


urlpatterns = [
    path('', MainView.as_view(), name='main_page'),
    path('form/', GetFormData.as_view(), name='form_data'),
    path('ai/', AIView.as_view(), name='ai'),
]