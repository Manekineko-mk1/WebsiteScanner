# This program will gather information about a website. Information such as IP address, WHOIS, nmap, robot.txt etc.

# Input: An URL
# Output: Text file

from general import *
from domain_name import *
from ip_address import *
from nmapScanner import *
from robots_txt import *
from get_whois import *


ROOT_DIR = 'companies'
create_dir(ROOT_DIR)

# name = name of the website (folder name)
# url = website's url


def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(domain_name)
    nmap_result = get_nmap('', ip_address)
    robots_result = get_robots_txt(url)
    whois_result = get_whois_info(domain_name)
    create_report(name, url, domain_name, nmap_result, robots_result, whois_result)


def create_report(name, full_url, domain_name, nmap_result, robots_result, whois_result):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/nmap_result.txt', nmap_result)
    write_file(project_dir + '/robots_result.txt', robots_result)
    write_file(project_dir + '/whois_result.txt', whois_result)

print(gather_info('Reddit', 'https://www.reddit.com/'))
