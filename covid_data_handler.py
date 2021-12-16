'''Main data handler, takes covid data using uk_covid19 API,
then that data is parsed and processed to generate figures used
in the main interface'''
import csv
import json
from uk_covid19 import Cov19API

with open('config', 'r', encoding='UTF-8')as f:
    config_file = json.load(f)
    filepaths = config_file['filepaths']
    national_path = filepaths["covid-data-national"]
    print(national_path)


def parse_csv_data(csv_filename):
    '''parses csv data '''
    covid_csv_data = []
    with open(csv_filename, 'r', encoding='UTF-8') as covid_data_file:
        csvreader = csv.reader(covid_data_file)
        for row in csvreader:
            covid_csv_data.append(row)
        return covid_csv_data


def process_covid_csv_data(covid_csv_data):
    '''gets cases in last 7 days, hospital cases,
    and total deaths from parsed csv file'''
    for data_line in covid_csv_data[1:2]:
        try:
            hospital_cases = data_line[5:]
            string = [str(i) for i in hospital_cases]
            current_hospital_cases = ''.join(string)
            current_hospital_cases = int(current_hospital_cases)
        except ValueError:
            continue

    last7days_cases = 0
    for data_line in covid_csv_data[3:10]:
        try:
            specimen = data_line[6:]
            string2 = [str(i) for i in specimen]
            string2_joined = ''.join(string2)
            specimen_integer = int(string2_joined)
            last7days_cases += specimen_integer
        except ValueError:
            continue

    for data_line in covid_csv_data[2:]:
        total_deaths = 0
        try:
            cumulative_death_col = data_line[4:5]
            string3 = [str(i) for i in cumulative_death_col]
            string3_joined = ''.join(string3)
            deaths_int = int(string3_joined)
            if isinstance(deaths_int, int):
                total_deaths = deaths_int
                break

        except ValueError:
            continue

    return current_hospital_cases, last7days_cases, total_deaths


def covid_API_request(location='exeter', location_type='ltla'):
    '''takes data from the covid api'''
    exeter_filter = [
        'areaType=' + location_type,
        'areaName=' + location
    ]
    cases_and_deaths = {
        "areaCode": "areaCode",
        "areaName": "areaName",
        "areaType": "areaType",
        "date": "date",
        "cumDailyNsoDeathsByDeathDate": "cumDailyNsoDeathsByDeathDate",
        "hospitalCases": "hospitalCases",
        "newCasesBySpecimenDate": "newCasesBySpecimenDate"
    }

    api = Cov19API(
        filters=exeter_filter,
        structure=cases_and_deaths,
    )

    data = api.get_csv(save_as='covid-data-national.csv')
    return data


def covid_api_request_national(location='england', location_type='nation'):
    '''api request that returns national data only'''
    national_filter = [
        'areaType=' + location_type,
        'areaName=' + location
    ]
    cases_and_deaths = {
        "areaCode": "areaCode",
        "areaName": "areaName",
        "areaType": "areaType",
        "date": "date",
        "cumDailyNsoDeathsByDeathDate": "cumDailyNsoDeathsByDeathDate",
        "hospitalCases": "hospitalCases",
        "newCasesBySpecimenDate": "newCasesBySpecimenDate"
    }

    api = Cov19API(
        filters=national_filter,
        structure=cases_and_deaths,
    )

    data = api.get_csv(save_as=national_path)
    return data


covid_api_request_national()
print(process_covid_csv_data(parse_csv_data('covid_data_national.csv')))
