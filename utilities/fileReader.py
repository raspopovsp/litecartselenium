import csv
import json


class FileReader:

    @staticmethod
    def get_json_data(file):
        with open(file) as json_file:
            data = json.load(json_file)
        return data

    @staticmethod
    def get_csv_data(file):
        data = []
        with open(file, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        return data

    """ парсинг данных пользователей """

    @staticmethod
    def parse_user_data(data):
        users = []
        for x in data:
            user = {
                'username': x[0],
                'password': x[1]
            }
            users.append(user)
        return users
