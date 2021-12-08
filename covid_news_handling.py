import requests
import pprint


def news_API_request(covid_terms=['Covid', 'COVID-19', 'coronavirus']):
    url = 'https://newsapi.org/v2/top-headlines?'
    for val in covid_terms:
        parameters = {'q': val,
                      'sort_by': 'relevancy',
                      'country': 'gb',
                      'apiKey': 'a89c7a9fc4ed4d03bddb136f115f3d27'}
        response = requests.get(url, params=parameters)
        response_json = response.json()
        return response_json


def update_news(data):
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

    return new_toast


pprint.pprint(update_news(news_API_request()))
