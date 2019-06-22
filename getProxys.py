#!/usr/bin/python3

import requests
import optparse

def getListProxy(typ, anon, country):
    url = "https://www.proxy-list.download/api/v1/get?type="+typ
    if(anon):
        url += "&anon="+anon
    if(country):
        url += "&country="+country

    res = requests.get(url)
    return res.text, res.status_code

def main():
    parser = optparse.OptionParser("%prog -t <http | https | socks4 | socks5> "+\
            "[-a <transparent | anonymous | elite> -c <country code>]")
    parser.add_option("-t", dest='typ', type="string",\
            help='specify the connection type')
    parser.add_option('-a', dest='anon', type='string',\
            help='specify the anonimity')
    parser.add_option('-c', dest='country', type='string',\
            help='specify the country')
    
    (options, args) = parser.parse_args()
    if(options.typ == None):
        print(parser.print_help())
        exit(0)
    else:
        typ = options.typ
        anon = ""
        country = ""
        if(options.anon != None): 
            anon = options.anon
        if(options.country != None):
            country = options.country
        (res, stcod) = getListProxy(typ, anon, country)

    if(stcod == 200 and res):
        nProxys = res.split('\n')
        print("[+] Everything goes perfect: " + str(len(nProxys) - 1) + " proxies")
        f = open('proxy_list.txt', 'w+')
        f.write(res)
        f.close()
    elif(not res):
        print("[-] Nothing with that parameters, try another ones!")
    else:
        print("[-] Bad parameters: " + str(stcod))

if __name__ == '__main__':
    main()
