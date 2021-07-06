import json
import requests
import datetime

error_msg = 'Not Found!!'

def get_url():
	fetch_url = requests.get(
		'https://api.weather.gov/points/39.7456,-97.0892'
		)
	re_str = json.dumps(fetch_url.json(),
						sort_keys=True,
						indent=4)
	# print(re_str)
	resp_dict = json.loads(re_str)
	# print(resp_dict)
	final_url=resp_dict['properties']['forecastGridData']

	return final_url


data = requests.get(get_url())

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

valid_temp= dict()

temp_list=(data_dict['properties']['temperature']['values'])
humidity_list=(data_dict['properties']['relativeHumidity']['values'])
print(humidity_list)
keyVal = []
keyVal.append(currentTime)

# temp_val = {'type': 'temperature'}
result_temp = (list(filter(lambda d:d['validTime'] in keyVal, temp_list)))
print(result_temp)
temperature = [item['value'] for item in result_temp]
print(temperature)
# result_temp.update(temp_val)

# humid_val = {'type': 'humidity'}
result_humidity = (list(filter(lambda d:d['validTime'] in keyVal, humidity_list)))
print(result_humidity)
humidity = [item['value'] for item in result_humidity]
print(humidity)

# result_humidity.update(humid_val)

# final_result = result_temp, result_humidity
# json_data = json.dumps(final_result, indent=4)

