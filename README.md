# LANBilling

## Installation

```
$ git clone https://github.com/alexanderfefelov/lanbilling-py.git
$ cd lanbilling
$ python setup.py install
```

## Usage

To use, simply do:

```python
>>> from lanbilling import LANBilling
>>> api = LANBilling(manager='admin', password='', host='127.0.0.1', port=1502)
>>> account = api.getAccount({'uid': 1})
>>> agreement = api.getAgreement(agrm_id=1)
```

To show all possible methods::

```python
>>> api.help()
```

To get help for method usage::

```python
>>> api.help('getAccount')
```
