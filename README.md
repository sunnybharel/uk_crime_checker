# UK Crime Checker
_Check crime statistics in the UK by location_

Checks UK Crime Database for a given location and returns crimes in the area for the time period. Returned format includes following columns:
#### Category     Month    StreetName     OutcomeOfEvent


## Pre-requisites
`
pip install geopy
`  
`
pip install requests
`

## Usage

`
python3 uk_crime_checker.py -y <year_of_crimes> -m <month_of_crimes> -l <street_city_country_to_check>
`
### Example
`
python3 uk_crime_checker.py -y 2019 -m 07 -l pentonville road, london, uk
`

### Sample Output

other-crime $ 2019-07 $ Kings Cross (station) $ {'category': 'Under investigation', 'date': '2019-07'}  
violent-crime $ 2019-07 $ Old Street (lu Station) $ {'category': 'Under investigation', 'date': '2019-07'}  
theft-from-the-person $ 2019-07 $ On or near Crestfield Street $ {'category': 'Under investigation', 'date': '2019-07'}  
shoplifting $ 2019-07 $ St Pancras International (station) $ {'category': 'Under investigation', 'date': '2019-07'}  
shoplifting $ 2019-07 $ On or near Gray's Inn Road $ {'category': 'Under investigation', 'date': '2019-07'}  
shoplifting $ 2019-07 $ On or near Supermarket $ {'category': 'Awaiting court outcome', 'date': '2019-09'}  
shoplifting $ 2019-07 $ St Pancras International (station) $ {'category': 'Under investigation', 'date': '2019-07'}  
public-order $ 2019-07 $ On or near College Cross $ {'category': 'Under investigation', 'date': '2019-07'}  
public-order $ 2019-07 $ On or near Park/open Space $ {'category': 'Under investigation', 'date': '2019-07'}  
public-order $ 2019-07 $ On or near Sherborne Street $ {'category': 'Under investigation', 'date': '2019-07'}  
public-order $ 2019-07 $ On or near Sherborne Street $ {'category': 'Under investigation', 'date': '2019-07'}  
public-order $ 2019-07 $ On or near Florence Street $ {'category': 'Under investigation', 'date': '2019-07'}  

## Improvements
* Try to GUI this up and select location from a map
* Add logging capability for error/info level writing
* Add CSV writing capability for results 
