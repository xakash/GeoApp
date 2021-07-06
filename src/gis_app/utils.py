import json
import requests as req
import datetime


def get_url(lat, lon):
    print(lat, lon)
    # EP = 'https://api.weather.gov/points/'+lat+','+lon
    api_response = req.get(
            'https://api.weather.gov/points/'+lon+','+lat
            )

    if(api_response.ok):
        print(api_response)
        re_str = json.dumps(api_response.json(),
                        sort_keys=True,
                        indent=4)
        resp_dict = json.loads(re_str)
    else:
        api_response.raise_for_status()
    
    final_url=resp_dict['properties']['forecastGridData']
    # data = req.get(final_url)
    # print(final_url)
    return final_url

def get_temperature(lat, lon):
    url = get_url(lat, lon)
    print('get temp url is:'+url)

    data = req.get(str(url))
    # data = get_url(lat, lon)
    print('data is:'+ str(data))
    data_str = json.dumps(data.json(),
                            sort_keys=True,
                            indent=4)
    data_dict = json.loads(data_str)
    now = datetime.datetime.now()
    date = (now.strftime("%Y-%m-%d"))
    time = (now.strftime("%H"))
    if time == '23' or time == '22':
        time = '22'
        currentTime = date + "T" + time + ":00:00+00:00/PT2H"

    else:
        currentTime = date + "T" + time + ":00:00+00:00/PT1H"
        
    print(currentTime)

    temp_list=(data_dict['properties']['temperature']['values'])
    keyVal = []
    keyVal.append(currentTime)

    # temp_val = {'type': 'temperature'}
    result_temp = (list(filter(lambda d:d['validTime'] in keyVal, temp_list)))
    print(result_temp)
    temperature = [item['value'] for item in result_temp]
    print(temperature)

    return temperature


def get_humidity(self):
    data = req.get(get_url())

    data_str = json.dumps(data.json(),
                            sort_keys=True,
                            indent=4)
    data_dict = json.loads(data_str)
    now = datetime.datetime.now()
    date = (now.strftime("%Y-%m-%d"))
    time = (now.strftime("%H"))
    
    currentTime = date + "T" + time + ":00:00+00:00/PT1H"
    print(currentTime)
    humidity_list=(data_dict['properties']['relativeHumidity']['values'])

    keyVal = []
    keyVal.append(currentTime)
    
    result_humidity = (list(filter(lambda d:d['validTime'] in keyVal, humidity_list)))
    print(result_humidity)
    humidity = [item['value'] for item in result_humidity]
    print(humidity)

    return humidity