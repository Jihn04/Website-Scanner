import urllib.request
import io
from tld import get_tld
import os


def get_domain_name(url):
    domain_name = get_tld(url)
    return domain_name


def get_ip_address(domain_name):
    command = 'host ' + domain_name
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('has address') + 12
    ip_address = results[marker:].splitlines()[0].strip()
    return ip_address


def get_nmap(options, ip):
    command = 'nmap ' + options + ' ' + ip
    process = os.popen(command)
    results = str(process.read())
    return results


def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib.request.urlopen(path + 'robots.txt', data=None)
    data = io.TextIOWrapper(req, encoding='utf-8')
    return data.read()


def get_whois(url):
    command = "whois " + url
    process = os.popen(command)
    results = str(process.read())
    return results
