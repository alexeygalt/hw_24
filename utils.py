# payload={
#   'file_name': 'apache_logs.txt',
#   'cmd1': 'filter',
#   'value1': 'GET',
#   'cmd2': 'map',
#   'value2': '0'
# }
import re
from typing import List


def do_command(command: str, value: str, file: List[str]) -> List[str]:
    if command == 'filter':
        file = list(filter(lambda x: value in x, file))

    elif command == 'map':
        file = list(map(lambda x: x.split()[int(value)], file))

    elif command == 'unique':
        file = list(set(file))

    elif command == 'sort':
        if value == 'desc':
            file = sorted(file, reverse=True)
        else:
            file = sorted(file)

    elif command == 'limit':
        file = [item for item in list(file)[:int(value)]]

    elif command == 'regex':
        result = []
        for item in file:
            temp = re.compile(value)
            key = temp.findall(item)
            if key:
                result.append(item)
        file = result
    return file


def get_result(data: dict[str, str], file: List[str]) -> List[str]:
    count = 1
    command = 'cmd' + str(count)
    value = 'value' + str(count)

    while command in data.keys() and value in data.keys():
        if command in data.keys():
            file = do_command(data[command], data[value], file)

        count += 1
        command = 'cmd' + str(count)
        value = 'value' + str(count)

    return list(file)
