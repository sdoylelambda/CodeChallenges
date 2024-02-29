Find Domain Name From DNS Pointer (PTR) Records Using IP Address
Write a function that takes an IP address and returns the domain name using PTR DNS records.

Example
get_domain("8.8.8.8") ➞ "dns.google"

get_domain("8.8.4.4") ➞ "dns.google"

You may want to import socket.

Don't cheat and just print the domain name, you need to make a real DNS request.

Return as a string.



UPER

U - UNDERSTAND
    Use Socket library to find by domain passing in string with ~ 4 nums
    socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)

P - PLAN

x = www.google.com
or 
x = pass in -- '8.8.8.8'

socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)
socket.getaddrinfo(port='www.google.com')