from django.urls import path
from .views import CountryListView, CountryDetailView, StateListView, StateDetailView

urlpatterns = [
    path('countries/all/', CountryListView.as_view(), name='country-list'),
    path('countries/<str:country_name>/', CountryDetailView.as_view(), name='country-detail'),
    path('countries/<str:country_name>/states/', StateListView.as_view(), name='state-list'),
    path('countries/<str:country_name>/states/<str:state_name>/', StateDetailView.as_view(), name='state-detail'),
]
