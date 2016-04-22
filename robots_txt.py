import urllib.request
import io


def get_robots_txt(url):
    print("Attempting to acquire robots.txt for: " + url)
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'

    req = urllib.request.urlopen(path + "robots.txt", data=None)
    data = io.TextIOWrapper(req, encoding='utf-8')

    print("Robots.txt acquired.")

    return data.read()
