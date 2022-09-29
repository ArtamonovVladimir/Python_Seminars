from datetime import datetime
import json

path = "7_Seminar\log.txt"
path_r = "7_Seminar\phones.json"

# , encoding='UTF-8'


def log_record(phones):
    with open(path, 'a+') as files:
        files.write(f'{phones}  --- {datetime.now()}\n')


def recording(phones):
    # with open(path_r, 'w') as files:
    #     for key, value in phones.items():
    #         files.write(f'{key}~{value}~')
    with open(path_r, 'w') as f:
        f.write(json.dumps(phones))
    # return (phones)


def opens(phones):
    # with open(path_r) as files:
    #     phones = exec(files.read())
    #     for line in files:
    #         key, value = line.split('~')
    #         phones[key] = value
    with open(path_r, 'r') as f:
        phones = json.loads(str(f.read()))

    return (phones)
