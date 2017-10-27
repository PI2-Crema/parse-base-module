import json
import requests
import os.path
import time

def run_observer():
    try:
        while True:
            time.sleep(1)
            observer('node.txt')
    except KeyboardInterrupt:
        print("parei")

def observer(filepath):
    if os.path.isfile(filepath):
        filename = filepath.split('.')
        file = filename[0] + '.txt'
        file_copy = filename[0] + '_copy.txt'
        os.rename(
            file,
            file_copy
            )

        status_code = post_register_data(read_file(file_copy))
        if status_code == 200:
            delete_file(file_copy)

def delete_file(file_name):
    if os.path.isfile(file_name):
        os.remove(file_name)

# ID  HORA MINUTO NIVEL(0/100) BATERIA(0/100) CODE-ERROR  PH TEMPERATURA CODUTIVIDADE
def post_register_data(post_fields):
    url = 'http://192.168.15.151:3000/feeders/register_data'
    post_request = requests.post(url, json=post_fields)
    print(post_fields)
    return post_request.status_code

def read_file(file_name):
    keys = ["network_code",
            "hora",
            "minute",
            "food_level",
            "battery_level",
            "error_code",
            "ph",
            "temperature",
            "conductivity"]
    json_data = {}
    array_data = []
    with open(file_name, "r") as f:
        data = f.readlines()

        for line in data:
            words = line.split()

            for index, value in enumerate(words):
                json_data[keys[index]] = value

            array_data.append(json_data)
            json_data = {}


        f.close()
    request_data = {'data':array_data}
    return request_data

def main():
    run_observer()

if __name__ == "__main__":
    main()
