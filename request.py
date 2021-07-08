import json
import requests
import datetime

error_msg = 'Not Found!!'

def get_url(a, b):
	fetch_url = requests.get(
		'https://api.weather.gov/points/'+a+','+b
		)
	re_str = json.dumps(fetch_url.json(),
						sort_keys=True,
						indent=4)
	# print(re_str)
	resp_dict = json.loads(re_str)
	# print(resp_dict)
	final_url=resp_dict['properties']['forecastGridData']
	print(final_url)
	return final_url
	

a = '38.431564011446206'
b = '-92.50262974404667'

data = requests.get(get_url(a,b))

data_str = json.dumps(data.json(),
						sort_keys=True,
						indent=4)
data_dict = json.loads(data_str)
now = datetime.datetime.now()
date = (now.strftime("%Y-%m-%d"))
time = (now.strftime("%H"))
timeVar = "1"
currentTime = date + "T" + time + ":00:00+00:00/PT"+timeVar+"H"
	 

print(currentTime)

valid_temp= dict()

temp_list=(data_dict['properties']['temperature']['values'])
humidity_list=(data_dict['properties']['relativeHumidity']['values'])
print(humidity_list)
keyVal = []
keyVal.append(currentTime)

# temp_val = {'type': 'temperature'}
result_temp = (list(filter(lambda d:d['validTime'] in keyVal, temp_list)))
print(len(result_temp))

while len(result_temp) < 1:
	utime= int(time)
	utime= utime-1
	utimeVar= int(timeVar)
	utimeVar= utimeVar+1
	updateTime = date + "T" + str(utime) + ":00:00+00:00/PT"+str(utimeVar)+"H"
	print(updateTime)
	keyVal.append(updateTime)
	print(keyVal)
	result_temp = (list(filter(lambda d:d['validTime'] in keyVal, temp_list)))
	print(len(result_temp))

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

