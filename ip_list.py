#!/usr/bin/python

from netaddr import IPNetwork

def ip_stuff(prefix):
    ips = []

    for ip in IPNetwork(prefix):
        ips.append(str(ip))
    return ips

class FilterModule(object):
    def filters(self):
        return {'ip_list': ip_stuff}
