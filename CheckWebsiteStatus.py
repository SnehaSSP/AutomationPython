import os
import requests
import socket


def ping_test(domain):
    response = os.system("ping -c 1 " + domain)
    return response == 0


def http_status_check(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return str(e)


def dns_resolution_check(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.error as e:
        return str(e)


def port_check(domain, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((domain, port))
    sock.close()
    return result == 0


def website_status(url):
    domain = url.split("//")[-1].split("/")[0]
    status = {
        "ping_test": ping_test(domain),
        "http_status_code": http_status_check(url),
        "dns_resolution": dns_resolution_check(domain),
        "port_80_open": port_check(domain, 80),
        "port_443_open": port_check(domain, 443)
    }
    return status


if __name__ == "__main__":
    website_url = "https://automateqx.com/"  # Replace with the website URL you want to check
    status = website_status(website_url)
    print(status)
