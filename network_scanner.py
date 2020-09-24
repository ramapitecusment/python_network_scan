import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]

    clients_list = []

    for element in answered_list:
        client_dict = {"ip" : element[1].psrc, "mac" : element[1].hwsrc}
        clients_list.append(client_dict)

    return clients_list

def print_result(results_list):
    print("IP\t\t\tMAC Address\n------------------------------------------")

    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


#scan_result = scan("10.0.2.1/24")
#print_result(scan_result)

#print(arp_request.summary())
# scapy.ls(scapy.ARP())
# scapy.ls(scapy.Ether())
# print(broadcast.summary())

# arp_request.show()
# broadcast.show()
# arp_request_broadcast.show()
# print(arp_request_broadcast.summary())
# print(answered_list.summary())

# print(element[1].psrc)
# print(element[1].hwsrc)

# arp_request_broadcast = broadcast / arp_request
# answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
#
# print("IP\t\t\tMAC Address\n-------------------------------------------")
# for element in answered_list:
#     print(element[1].psrc + "\t\t" + element[1].hwsrc)

