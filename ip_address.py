import socket


def get_ip_address(url):
    print("Acquiring IP address for: " + url)

    try:
        ip = socket.gethostbyname(url)
    except socket.gaierror as err:
        print("cannot resolve hostname:", err)

    print("IP address retrieved. IP: " + ip)

    return ip
