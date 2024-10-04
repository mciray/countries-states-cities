import json
import os
from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse

class CountryListView(APIView):
    def get(self, request):
        # JSON dosyasının proje kök dizinindeki yolunu belirleyin
        json_file_path = os.path.join(settings.BASE_DIR, 'countries+states+cities.json')
        
        # Dosyanın varlığını kontrol edin
        if not os.path.exists(json_file_path):
            return JsonResponse({"error": "JSON file not found."}, status=404)

        # JSON dosyasını oku
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Tüm ülkeleri döndür
        return JsonResponse(data, safe=False)

class CountryDetailView(APIView):
    def get(self, request, country_name):
        # JSON dosyasının proje kök dizinindeki yolunu belirleyin
        json_file_path = os.path.join(settings.BASE_DIR, 'countries+states+cities.json')
        
        # Dosyanın varlığını kontrol edin
        if not os.path.exists(json_file_path):
            return JsonResponse({"error": "JSON file not found."}, status=404)

        # JSON dosyasını oku
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Belirli bir ülkeyi adıyla (name) filtrele
        country = next((item for item in data if item["name"].lower() == country_name.lower()), None)
        
        if country:
            return JsonResponse(country, safe=False)
        else:
            return JsonResponse({"error": "Country not found"}, status=404)

class StateListView(APIView):
    def get(self, request, country_name):
        # JSON dosyasının proje kök dizinindeki yolunu belirleyin
        json_file_path = os.path.join(settings.BASE_DIR, 'countries+states+cities.json')
        
        # Dosyanın varlığını kontrol edin
        if not os.path.exists(json_file_path):
            return JsonResponse({"error": "JSON file not found."}, status=404)

        # JSON dosyasını oku
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Ülkeyi adıyla (name) filtrele
        country = next((item for item in data if item["name"].lower() == country_name.lower()), None)
        
        if country:
            states = country.get('states', [])
            return JsonResponse(states, safe=False)
        else:
            return JsonResponse({"error": "Country not found"}, status=404)


class StateDetailView(APIView):
    def get(self, request, country_name, state_name):
        # JSON dosyasının proje kök dizinindeki yolunu belirleyin
        json_file_path = os.path.join(settings.BASE_DIR, 'countries+states+cities.json')
        
        # Dosyanın varlığını kontrol edin
        if not os.path.exists(json_file_path):
            return JsonResponse({"error": "JSON file not found."}, status=404)

        # JSON dosyasını oku
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        country = next((item for item in data if item["name"].casefold() == country_name.casefold()), None)
        for states in country['states']:
            
            if states["name"].casefold() == state_name.casefold():
                print('eşleşiyor')
        if country:
            state = next((state for state in country['states'] if state["name"].casefold() == state_name.casefold()), None)
            if state:
                return JsonResponse(state, safe=False)
            else:
                return JsonResponse({"error": "State not found"}, status=404)
        else:
            return JsonResponse({"error": "Country not found"}, status=404)
        
class HomePageView(APIView):
    def get(self, request):
        return render(request, 'index.html')