
# coding: utf-8

# In[38]:

"""
Various functions to run the BitX API through python in a user friendly manner.
Note that all arguments passed to functions (currency pairs mostly) should be strings
Also note that bitx keeps the values of prices in string format so it is necessary to 
convert this to float for any mathematical operations thereon.
"""

# import relevant modules
import urllib3
import certifi
import json
from datetime import datetime
from time import mktime

# setup the connection and bind necessary URLs to variables for later use
# refer to urllib3 and certifi documentation for more information
def establish_and_fetch(fetch_type):
    http = urllib3.PoolManager(cert_reqs = 'CERT_REQUIRED', ca_certs = certifi.where())
    url = 'https://api.mybitx.com/api/1/'
    return http.request('GET', url+fetch_type).data.decode('utf-8')


# call to return latest ticker indicators and convert from bytes to json friendly format"""
def get_ticker_ind(pair):
    pair = '?pair='+pair
    raw_data = establish_and_fetch('ticker'+pair)
    return json.loads(raw_data)

# fetch current order book for a given pair
def fetch_order_book(pair):
    pair = '?pair='+pair
    raw_data = establish_and_fetch('orderbook'+pair)
    return json.loads(raw_data)

# fetch most recent trades, date from which is optional (yyy, mm, dd)
def fetch_recent_trades(pair, *date):
    pair = '?pair='+pair
    datetime_obj = datetime(date[0], date[1], date[2])
    date_tuple = datetime_obj.timetuple()
    timestamp = int(mktime(date_tuple))
    raw_data = establish_and_fetch('trades'+pair+'&since='+str(timestamp))
    return json.loads(raw_data)

