import os


def get_whois_info(url):
    print("Acquiring WHOIS info for: " + url)
    command = "whois " + url
    process = os.popen(command)
    results = str(process.read())
    print("WHOIS info acquired.")

    return results

