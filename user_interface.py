from flask import Flask, render_template, redirect, request
from covid_data_handler import process_covid_csv_data, parse_csv_data
from covid_news_handling import update_news, news_API_request
import sched

toast = update_news(news_API_request())
news_deleted_list = []

app = Flask(__name__)


@app.route('/')
def goto_index():
    return redirect('/index', code=302)


@app.route('/index')
def main_page():
    delete_toast()
    return render_template('index.html',
                           image='download.jpeg',
                           title='Covid Daily Update',
                           news_articles=toast,
                           location='Exeter',
                           local_7day_infections=
                           process_covid_csv_data(parse_csv_data('venv\covid_data\covid_data.csv'))[1],
                           nation_location='England',
                           national_7day_infections=
                           process_covid_csv_data(parse_csv_data('venv\covid_data\covid_data_national.csv'))[1],
                           hospital_cases='Total Hospital Cases: ' + str(
                               process_covid_csv_data(parse_csv_data('venv\covid_data\covid_data_national.csv'))[0]),
                           deaths_total='Total Deaths: ' + str(
                               process_covid_csv_data(parse_csv_data('venv\covid_data\covid_data_national.csv'))[2]))


def delete_toast():
    remove_toast = request.args.get('notif')
    for dictionary in toast:
        if remove_toast == dictionary['title']:
            news_deleted_list.append(dictionary)
            toast.remove(dictionary)
            return toast


if __name__ == '__main__':
    app.run()
