from tld import get_tld

# Input: An URL from user (in any form: http or https, with or without www).
# Output: Top level domain name. Ex: Google.com instead of www.google.com.


def get_domain_name(url):
    print("Acquiring domain name for: " + url)
    domain_name = get_tld(url)
    print("Domain name acquired: " + domain_name)

    return domain_name
