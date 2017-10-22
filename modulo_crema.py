import os.path
import io, json

def observer(filepath):
    if os.path.isfile(filepath):
        filename = filepath.split('.')
        file = filename + '.txt'
        file_copy = filename + '_copy.txt'
        os.rename(
            file,
            file_copy
            )

        start_read(file_copy)

def start_read(file_name):
    with open(file_name) as file:
        for line in file:
            parametros = line.split(' ')
            json_request = (json.dumps(
                {
                    'network_code': parametros[0],
                    'hora': parametros[1],
                    'minute': parametros[2],
                    'food_level': parametros[3],
                    'battery_level': parametros[4],
                    'error_code': parametros[5],
                    'ph': parametros[6],
                    'temperature': parametros[7],
                    'conductivity': parametros[8],
                }, ensure_ascii=True).encode('utf8'))

def main():
    filepath = 'nodes.txt'
    observer(filepath)

if __name__ == "__main__":

# ID  HORA MINUTO NIVEL(0/100) BATERIA(0/100) CODE-ERROR  PH TEMPERATURA CODUTIVIDADE

# POST
# http://localhost:3000/feeders/register_data
# [
# {
#   network_code:
#   hora:
#   minute:
#   food_level:
#   battery_level:
#   error_code:
#   ph:
#   temperature:
#   conductivity:
# }
# ]