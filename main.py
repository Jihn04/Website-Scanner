import urllib.request
import io
from tld import get_tld
from general import *

ROOT_DIR = 'companies'
create_dir(ROOT_DIR)


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


def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(domain_name)
    nmap = get_nmap('-F', ip_address)
    robots_txt = get_robots_txt(url)
    whois = get_whois(domain_name)
    create_report(name, url, domain_name, ip_address, nmap, robots_txt, whois)


def create_report(name, full_url, domain_name, ip_address, nmap, robots_txt, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/ipaddress.txt', ip_address)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/robots.txt', robots_txt)
    write_file(project_dir + '/whois.txt', whois)


if __name__ == '__main__':
    gather_info('youtube', 'https://www.youtube.com/')
