import csv
from uk_covid19 import Cov19API
import scheduler


def parse_csv_data(csv_filename):
    covid_csv_data = []
    with open(csv_filename, 'r') as covid_data_file:
        csvreader = csv.reader(covid_data_file)
        for row in csvreader:
            covid_csv_data.append(row)
        return covid_csv_data


def process_covid_csv_data(covid_csv_data):
    for data_line in covid_csv_data[1:2]:
        try:
            hospital_cases = data_line[5:]
            string = [str(i) for i in hospital_cases]
            string_joined = ''.join(string)
            current_hospital_cases = int(string_joined)
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

    data = api.get_csv(save_as='venv\covid_data\covid_data.csv')


def covid_api_request_national(location='england', location_type='nation'):
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

    data = api.get_csv(save_as='venv\covid_data\covid_data_national.csv')


covid_api_request_national()
