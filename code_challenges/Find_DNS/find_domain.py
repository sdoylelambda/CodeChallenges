import socket


def get_domain(ip_address: str) -> str:
    host = socket.gethostbyaddr(ip_address)
    print(host[0])
    return host[0]


# Example
get_domain("8.8.8.8")  # ➞ "dns.google"
get_domain("8.8.4.4")  # ➞ "dns.google"


