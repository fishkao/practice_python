# -*- coding: utf-8 -*-

__author__ = 'fish'

import urllib
import json
import sys
import re


def get_info(ip):
    url_fp = urllib.urlopen(
        'http://ip.taobao.com/service/getIpInfo.php?ip=' + ip)
    ip_data = url_fp.read()
    url_fp.close()
    all_info = json.loads(ip_data)
    if "data" not in all_info:
        return None
    data = all_info["data"]
    return '%s %s' % (data["region"], data["city"])


'''
    traceroute -n ip | awk '{print $2}'
    input format :
    ....
    61.164.31.121
    202.97.34.57
    *
    *
    220.181.70.106
    ip address
'''
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        ips = filter(lambda x: x != "", sys.argv[1].split("\n"))
        pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        for ip in ips:
            ip = ip.strip()
            if pat.search(ip):
                print ip, get_info(ip)
