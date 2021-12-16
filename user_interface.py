'''This module handles the user interface, it passes data from the data handlers into
the html template. The module also handles the deletion of toasts'''

import logging
from flask import Flask, render_template, redirect, request
from covid_data_handler import process_covid_csv_data, parse_csv_data
from covid_news_handling import update_news, news_API_request

logging.basicConfig(filename='user_interface.log',
                    level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')

# creates the toast
toast = update_news(news_API_request())

app = Flask(__name__)


@app.route('/')
def goto_index():
    '''This function redirects the default url to /index'''
    return redirect('/index', code=302)


@app.route('/index')
def main_page():
    '''handles the html template and displays data on the main page'''
    delete_toast()
    return render_template('index.html',
                           image='download.jpeg',
                           title='Covid Daily Update',
                           news_articles=toast,
                           location='Exeter',
                           local_7day_infections=
                           process_covid_csv_data(parse_csv_data(
                               r'venv\covid_data\covid_data.csv'))[1],
                           nation_location='England',
                           national_7day_infections=
                           process_covid_csv_data(parse_csv_data(
                               r'venv\covid_data\covid_data_national.csv'))[1],
                           hospital_cases='Total Hospital Cases: ' + str(
                               process_covid_csv_data(parse_csv_data(
                                   r'venv\covid_data\covid_data_national.csv'))[0]),
                           deaths_total='Total Deaths: ' + str(
                               process_covid_csv_data(parse_csv_data(
                                   r'venv\covid_data\covid_data_national.csv'))[2]))


def delete_toast():
    '''allows the user to remove news articles from the main page'''
    remove_toast = request.args.get('notif')
    for dictionary in toast:
        if remove_toast == dictionary['title']:
            toast.remove(dictionary)
            logging.info('Toast Deleted: %s', remove_toast)
            return toast
        return None


if __name__ == '__main__':
    app.run()
