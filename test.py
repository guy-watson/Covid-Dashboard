from covid_data_handler import parse_csv_data
from covid_data_handler import process_covid_csv_data
from covid_news_handling import news_API_request
from covid_news_handling import update_news


def test_news_API_request():
    assert news_API_request()


def test_update_news():
    update_news(news_API_request())


def test_parse_csv_data():
    data = parse_csv_data('nation_2021-10-28.csv')
    assert len(data) == 639

def test_process_covid_csv_data():
    current_hospital_cases, last7days_cases, total_deaths = process_covid_csv_data(parse_csv_data('nation_2021-10-28.csv'))
    assert last7days_cases == 240_299
    assert current_hospital_cases == 7_019
    assert total_deaths == 141_544



test_process_covid_csv_data()
test_parse_csv_data()
test_update_news()
test_news_API_request()