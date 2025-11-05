from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    weather_data = None
    if request.method == "POST":
        city = request.POST.get("city")
        API_KEY = "d1520102d88a25039a63971a2a02a03c"  # Replace with your key
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") == 200:
            weather_data = {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"].title(),
            }
        else:
            weather_data = {"error": "City not found!"}

    return render(request, "weather.html", {"weather": weather_data})