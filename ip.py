__author__ = 'fish'

import urllib, urllib2
import json
import sys


def get_info(ip):
    urlfp = urllib.urlopen('http://ip.taobao.com/service/getIpInfo.php?ip=' + ip)
    ipdata = urlfp.read()
    urlfp.close()
    allinfo = json.loads(ipdata)
    if "data" not in allinfo:
        return None
    data = allinfo["data"]
    return '%s %s' %(data["region"],data["city"])


if __name__ == "__main__":
    if len(sys.argv)<2:
        print "usage: python ip.py ipaddress"
    else:
        print get_info(sys.argv[1])
