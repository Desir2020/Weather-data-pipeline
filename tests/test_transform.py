from app.transform.transform import transform_weather_data
import pytest 

dic_test1 = {
    "name":"Paris",
    "sys" : {
        "country": "France"
    },
   "coord":{
       "lat":22546,
       "lon":57878
   },
    "dt": 15787,
    
    "weather": [
        {
            "main": "Clouds",        # string, pas un dict
            "description": "Nuageux"
        }
    ],
         "main":{
            "temp":15,
            "feels_like":12,
            "temp_min":10,
            "temp_max":17,
            "humidity":12,
            "pressure":20
        },
    "wind": {
        "speed":45203
    }
}

def test_transform_nominal():
    result = transform_weather_data(dic_test1)
    assert result["city"] == "Paris"
    assert result["temperature"] == 15


dic_test2 = {
    "name":"Paris",
   "coord":{
       "lat":22546,
       "lon":57878
   },
    "dt": 15787,
    
    "weather": [
        {
            "main": "Clouds",        # string, pas un dict
            "description": "Nuageux"
        }
    ],
         "main":{
            "temp":15,
            "feels_like":12,
            "temp_min":10,
            "temp_max":17,
            "humidity":12,
            "pressure":20
        }
}

def test_transform_missing_values():
    result = transform_weather_data(dic_test2)
    assert result["country"] is None
    assert result["wind_speed"] is None

