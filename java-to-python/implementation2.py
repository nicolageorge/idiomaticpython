from nettools import NetworkElement

with NetworkElement('127.0.0.1') as ne:
    for route in ne.routing_table:
        print '{} -> {}'.format(route.name, route.ipaddr)