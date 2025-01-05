import requests

api_key = '433b04e10a9dee397ebc4ce932c8b0b4'

def get_data(place, forecast_days):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    
    #fetches all the complete data 
    total_data = data['list']
    
    
    values = forecast_days * 8
    
    #fetches the data for required forecast days
    required_data = total_data[:values]
    
    return required_data
    

if __name__ == '__main__':
    print(get_data(place="Delhi", forecast_days=2))
