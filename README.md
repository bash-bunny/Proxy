# Proxy
Tool for search proxies

The script obtains a list of proxies from: https://www.proxy-list.download and write it to a file call proxy_list.txt where you have IP:PORT

Type python -h to get help

To use it:

python getProxys.py -t <type of the proxy>
  Accepted types:
    http
    https
    socks4
    socks5

Another options are:
  -a for anonimity proxies, the options are:
      transparent
      anonymous
      elite
      
  -c for country code, where you have to specify the country code.
