import pytest
from utils import get_data, get_filtered, get_last_operations, get_reformatted


@pytest.fixture()
def test_url():
    return "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230210T151236Z&X-Amz-Expires=86400&X-Amz-Signature=49e7e60535fb6e7835c06f25301c449b2f38ff40ae69f040dd40837d60ce29ef&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22operations.json%22&x-id=GetObject"


def test_get_data(test_url):
    assert len(get_data(test_url)[0]) > 0

@pytest.fixture()
def test_data():
    return [{'date': '2019-08-26T10:50:58.294041',
  'description': 'Перевод организации',
  'from': 'Maestro 1596837868705199',
  'id': 441945886,
  'operationAmount': {'amount': '31957.58',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'EXECUTED',
  'to': 'Счет 64686473678894779589'},
 {'date': '2019-07-03T18:35:29.512364',
  'description': 'Перевод организации',
  'from': 'MasterCard 7158300734726758',
  'id': 41428829,
  'operationAmount': {'amount': '8221.37',
                      'currency': {'code': 'USD', 'name': 'USD'}},
  'state': 'EXECUTED',
  'to': 'Счет 35383033474447895560'},
 {'date': '2018-06-30T02:08:58.425572',
  'description': 'Перевод организации',
  'from': 'Счет 75106830613657916952',
  'id': 939719570,
  'operationAmount': {'amount': '9824.07',
                      'currency': {'code': 'USD', 'name': 'USD'}},
  'state': 'EXECUTED',
  'to': 'Счет 11776614605963066702'},
 {'date': '2018-03-23T10:45:06.972075',
  'description': 'Открытие вклада',
  'id': 587085106,
  'operationAmount': {'amount': '48223.05',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'EXECUTED',
  'to': 'Счет 41421565395219882431'},
 {'date': '2019-04-04T23:20:05.206878',
  'description': 'Перевод со счета на счет',
  'from': 'Счет 19708645243227258542',
  'id': 142264268,
  'operationAmount': {'amount': '79114.93',
                      'currency': {'code': 'USD', 'name': 'USD'}},
  'state': 'EXECUTED',
  'to': 'Счет 75651667383060284188'}]


def test_get_filtered(test_data):
    assert len(get_filtered(test_data)) == 5
    assert len(get_filtered(test_data, from_none=True)) == 4


def test_get_last_operations(test_data):
    data = get_last_operations(test_data, 4)
    assert data[0]["date"] == '2019-08-26T10:50:58.294041'
    assert len(data) == 4


def test_get_reformatted(test_data):
    data = get_reformatted(test_data)
