'''Requests news data from news api, it then formats the news
into toasts which are sent to the user interface'''
import json
import logging
import sched
import time
import requests

with open('config', 'r', encoding='UTF-8')as f:
    config_file = json.load(f)
    api_keys = config_file['api-keys']

scheduler = sched.scheduler(time.time,
                            time.sleep)

logging.basicConfig(filename='covid_news_handling.log', level=logging.INFO,
                    format='%(levelname)s:%(name)s:%(message)s')


def news_API_request(covid_terms=['Covid', 'COVID-19', 'coronavirus']) -> dict:
    '''Gets news data from news api'''
    url = 'https://newsapi.org/v2/top-headlines?'
    for val in covid_terms:
        parameters = {'q': val,
                      'sort_by': 'relevancy',
                      'country': 'gb',
                      'apiKey': api_keys['news']}
        response = requests.get(url, params=parameters)
        response_json = response.json()
        logging.info('News requested from NEWS API')
        return response_json


def update_news(data) -> dict:
    '''creates toasts from news data'''
    title_list = []
    content_list = []
    new_toast = []
    article_list = (data['articles'])

    for dictionaries in article_list:
        for keys, values in dictionaries.items():
            if keys == 'title':
                title_list.append(values)

            if keys == 'content':
                content_list.append(values)

        for title in title_list:
            for content in content_list:
                content = {'title': title,
                           'content': content}

        new_toast.append(content)
    logging.info('New Toast created')
    return new_toast


def update_sched():
    toast = {'title': 'Select title',
            'content': 'Select time'}
    return toast
