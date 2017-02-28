import csv
from collections import namedtuple

import os
import requests


# input csv file name
FILE_NAME = "word_list.csv"

BASE_URL = 'https://www.bing.com/translator/api/language/Speak'
GET_PARAMS = '?locale={locale}&gender={gender}&media=audio/mp3&text={text}'

# bing translator cookies for mp3 requests
BING_COOKIES = requests.get('https://www.bing.com/translator').cookies

# define LOCALE named tuple
LOCALE = namedtuple('LOCALE', 'country locale_code gender')

# locales and preset genders
usa = LOCALE('USA', 'en-US', 'male')
great_britain = LOCALE('Great Britain', 'en-GB', 'female')
india = LOCALE('India', 'en-IN', 'male')
australia = LOCALE('Australia', 'en-AU', 'female')


def make_mp3_file_name(name, sex, country_name):
    return name.replace(" ", "_") + '_' + sex + '_' + country_name.lower() + '.mp3'


def save_mp3(csv_row, response_mp3, country):
    mp3_file_name = make_mp3_file_name(csv_row[0], country.gender, country.country)
    directory = os.path.dirname(os.getcwd() + '/audio/' + mp3_file_name)
    # make a directory if doesn't exist
    os.makedirs(directory, exist_ok=True)
    with open(directory + '/' + mp3_file_name, 'bw+') as audio_file:
        audio_file.write(response_mp3.content)
        print(mp3_file_name + " saved")


def make_request_for_mp3(country, txt):

    url = BASE_URL + GET_PARAMS.format(locale=country.locale_code,
                                       gender=country.gender,
                                       text=txt)
    return requests.get(url, cookies=BING_COOKIES)


if __name__ == '__main__':
    try:
        with open(FILE_NAME, newline='') as csv_file:
            word_reader = csv.reader(csv_file)
            for row in word_reader:
                # spaces in text have to be substituted for + (pluses)
                text = row[0].strip().replace(" ", "+")

                response_mp3_usa = make_request_for_mp3(country=usa, txt=text)
                save_mp3(row, response_mp3_usa, country=usa)

                response_mp3_australia = make_request_for_mp3(country=australia, txt=text)
                save_mp3(row, response_mp3_australia, country=australia)

    except Exception as error:
        print("OOPS! NO FILE NAMED {}".format(FILE_NAME))
        save_mp3(["OOPS"], make_request_for_mp3(india, 'oops!'), country=india)
