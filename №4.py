def dns_server():
    a = int(input())
    dns_records = {}
    for _ in range(a):
        domain, ip = input().split()
        dns_records[domain] = ip
    b = input()
    if b in dns_records:
        print(dns_records[b])
    else:
        print("Domain not found =(")
dns_server()
