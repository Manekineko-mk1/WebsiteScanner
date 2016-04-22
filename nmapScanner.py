import os


def get_nmap(options, ip):
    print("Attempting to acquire NMAP info for: " + ip)
    if options == "":
        options = "-F"

    command = "nmap " + options + " " + ip
    process = os.popen(command)
    results = str(process.read())

    print("NMAP info retrieved.")

    return results
