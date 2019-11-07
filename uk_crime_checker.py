from geopy.geocoders import Nominatim
import sys
import requests
import datetime
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-y", "--year", required=True, help="Year of data required. Eg. 2019")
ap.add_argument("-m", "--month", required=True, help="Month of data required. Eg. 09")
ap.add_argument("-l", "--location", nargs = '*', required=True, help="Location for required data. Eg. Pentonville Road, London UK")
args = vars(ap.parse_args())
input_location = str(args['location'])
year = args['year']
month = args['month']
data_police_uk_base_url = 'https://data.police.uk/api/crimes-street/all-crime?' 
geolocator = Nominatim(user_agent="uk_crime_checker")
location = geolocator.geocode(input_location)

try:
    lat = location.latitude
    long = location.longitude
    
except AttributeError as err: 
    print("Unable to retrieve location.\nExiting with error: {}".format(err))
    sys.exit(1)


formed_url = data_police_uk_base_url+'lat='+str(lat)+'&'+'lng='+str(long)+'&'+'date='+str(year)+'-'+str(month)
print ("Fetching URL {}".format(formed_url))
resp = requests.get(formed_url)
if resp.status_code is not  200:
  raise ApiError('GET {}'.format(resp.status_code))

print ("CATEGORY\t MONTH\t STREET_NAME\t OUTCOME_STATUS")
for item in resp.json():
    print("{} $ {} $ {} $ {}".format(item['category'], item['month'], item['location']['street']['name'], item['outcome_status']))

