import requests
from datetime import datetime
from pprint import pprint


def get_data(url):
    reply = requests.get(url)
    return reply.json()


def get_filtered(data, from_none=False):
    data = [i for i in data if "state" in i and i["state"] == "EXECUTED"]
    if from_none:
        data = [i for i in data if "from" in i]
    return data


def get_last_operations(data, last_operations):
    data = sorted(data, key=lambda i: i["date"], reverse=True)
    data = data[:last_operations]
    return data


def get_reformatted(data):
    reformatted_data = []
    for i in data:
        date = datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = i["description"]
        where_from, from_info = "", ""
        if "from" in i:
            adresser = i["from"].split()
            where_from = adresser.pop(-1)
            where_from = f"{where_from[:4]} {where_from[4:6]}** **** {where_from[-4:]}"
            from_info = " ".join(adresser)
        to = f"{i['to'].split()[0]} **{i['to'][-4:]}"
        operation_amount = f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"

        reformatted_data.append(f"""\
    {date} {description}
    {from_info} {where_from} -> {to}
    {operation_amount}""")
    return reformatted_data
