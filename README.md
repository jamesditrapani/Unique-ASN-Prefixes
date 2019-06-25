# Unique-ASN-Prefixes
## Description
Find unique ASNs within a given IPv4 prefix

## Usage
asn_in_prefix.py [-h] [-r ROUTE_SERVER] prefix

positional arguments:
  prefix                IPv4 Prefix you wish to find the unique ASNs within

optional arguments:
  -h, --help            show this help message and exit
  -r ROUTE_SERVER, --route-server ROUTE_SERVER
                        Specify route server to use. Route server must be running Quagga
                        Default - route-views.sydney.routeviews.org


## Sample Output
```
(virtual-env) [james@web1.ditrapani.com.au][~/Github/asn_in_range]$ python asn_in_prefix.py 192.18.0.0/16

Prefix: 192.18.0.0/16
Unique Originating ASNs: 4
ASNs: AS792 AS4192 AS786 AS7160
```

## Authors
* **James Di Trapani** - [Github](https://github.com/jamesditrapani)
