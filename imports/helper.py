import psutil

PROTOCOLS = {
    6: "TCP",
    17: "UDP"
}

def get_interfaces():
    addrs = psutil.net_if_addrs()
    try:
        interfaces = {}
        for key in addrs.keys():
            if key == "lo":
                continue
            else:
                interface_ip = addrs[key][0].broadcast.split(".")[0:3]
                interface_ip.append("0")
                interface_ip = ".".join(interface_ip)
                interfaces[key] = {"network":interface_ip,"ip":addrs[key][0].address, "netmask": addrs[key][0].netmask}
        return interfaces
    except AttributeError:
        return interfaces
    except Exception as e:
        print(f"Error getting interfaces : {e}")
        exit()
