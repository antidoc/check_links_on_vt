from virustotal_python import Virustotal
import time

def read_links():
    f = open('links.txt', 'r')
    l = f.read()
    links_list = l.split("\n")
    return links_list


def vt_gen(links_list):
    key_file = open('api', 'r')
    vt_api = key_file.read()
    vtotal = Virustotal(vt_api)
    result = open('result.txt', 'w')
    for link in links_list:
        resp = vtotal.url_report([link])
        result.write(resp['json_resp']['permalink'] + '\n')
        time.sleep(17)
    result.close()

links = read_links()
vt_gen(links)