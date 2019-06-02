#!/usr/bin/env python3

# Imports
from argparse import ArgumentParser
from re import findall
import telnetlib
from time import sleep

# Define global values
AS_PATH_REGEX = r'[0-9]+ [i\?]'
RESULT_MESSAGE = 'Found {0} unique originating ASNs for prefix {1}'

def get_unique_asns(prefix, route_server):
    unique_asns = set()
    server_prompt = '{0}> '.format(route_server)

    # Get Output from Route Server
    session = telnetlib.Telnet(route_server)
    session.read_until(server_prompt.encode('ascii'), 5)
    session.write('terminal length 0\n'.encode('ascii'))
    sleep(3)
    session.write('show ip bgp {0} longer-prefixes\n'.format(prefix).encode('ascii'))
    sleep(3)
    output = session.read_until(server_prompt.encode('ascii'), 300)
    session.write(b'exit\n')
    output = session.read_all().decode('ascii')

    # Match AS Regex against output, add AS's to a unique object set
    all_asn = findall(AS_PATH_REGEX, output)
    for asn in all_asn:
        unique_asns.add('AS{0}'.format(asn.split()[0]))

    # Display Result to User
    print('\nPrefix: {0}'.format(prefix))
    print('Unique Originating ASNs: {0}'.format(len(unique_asns)))
    print('ASNs:', *unique_asns)



def main():
    parser = ArgumentParser(
        description='Find the unique origination ASNs within given IPv4 Prefix'
    )
    parser.add_argument(
        '-r', '--route-server',
        type=str,
        default='route-views.sydney.routeviews.org',
        help='Specify route server to use. Route server must be running Quagga'
             'Default - route-views.sydney.routeviews.org'
    )
    parser.add_argument(
        'prefix',
        type=str,
        help='IPv4 Prefix you wish to find the unique ASNs within'
    )
    arguments = parser.parse_args()
    get_unique_asns(arguments.prefix, arguments.route_server)


if __name__ == "__main__":
    main()
