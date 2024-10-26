import requests

# category descriptions
category_1 = "Details: Air Quality is considered satisfactory."
category_2 = "Details: Air Quality is acceptable."
category_3 = "Details: Members of sensitive groups may experience health effects."
category_4 = "Details: Everyone may begin to experience health effects."
category_5 = "Details: Health warnings of emergency conditions."
category_6 = "Details: Health alert: everyone may experience more serious health effects."
source_info = "\nSource: World Air Quality Index Project and originating EPA"

# return category descriptions depending on the AQI
def category_name(aqi):
    if aqi <= 50:
        return "good.\n" + category_1 + source_info 
    elif 50 < aqi <= 100:
        return "moderate.\n" + category_2 + source_info
    elif 100 < aqi <= 150:
        return "Unhealthy for sensitive groups.\n" + category_3 + source_info
    elif 150 < aqi <= 200:
        return "Unhealthy.\n" + category_4 + source_info 
    elif 200 < aqi <= 300:
        return "Very Unhealthy.\n" + category_5 + source_info 
    else:
        return "hazardous.\n" + category_6 + source_info

# Fetch API data and return it as a string
def check_api(city):
    api_key = "7602a164990d0380c56392c79445aa864e63784f"
    url = f"https://api.waqi.info/feed/{city}/?token={api_key}"
    
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        json_data = response.json()
        
        # Check if 'data' and 'aqi' keys are present
        if 'data' in json_data and 'aqi' in json_data['data']:
            aqi = json_data['data']['aqi']
            return f"The Air Quality Index (AQI) in {city} is {aqi}, which is " + category_name(aqi)
        else:
            return "Error: Could not retrieve AQI data for this location."
    else:
        return "Error: Failed to fetch data. Please check your internet connection or try another city."

# Enter Location and print AQI information
city = input("Enter your city: ")
print(check_api(city))
