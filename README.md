# lanbilling-py

## Installation

```
$ git clone https://github.com/alexanderfefelov/lanbilling-py.git
$ cd lanbilling-py
$ python setup.py install
```

## Usage

```python
>>> from lanbilling import LANBilling
>>> api = LANBilling(manager='admin', password='', host='127.0.0.1', port=1502)
>>> print(api)
>>> api.version()
>>> account = api.getAccount({'uid': 1})
>>> print(account)
>>> api.help()
>>> api.help('getAccount')
```
