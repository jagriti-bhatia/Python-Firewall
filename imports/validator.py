import csv

def compare_rules(primary_rule: str, secondary_rules: list):
    result = []
    for rule in secondary_rules:
        if str(primary_rule).strip() == str(rule).strip():
            result.append(True)
        else:
            result.append(False)
    return any(result)

def validate_with_route_table(src_addr, dst_addr, src_port, dst_port):
    rules_stream = open("./imports/Rules.csv", "r")
    rules = csv.reader(rules_stream)
    for rule in rules:
        # <SRC_IP> <SRC_PORT> <DST_IP> <DST_PORT>
        # check for IP
        if compare_rules(rule[1], [src_addr, "any"]) and compare_rules(rule[3], [dst_addr, "any"]):
            # check for port
            if compare_rules(rule[2], [src_port, "any"]) and compare_rules(rule[4], [dst_port, "any"]):
                if str(rule[0]).lower() == "allow":
                    return True
                elif str(rule[0]).lower() == "deny":
                    continue
    return False
    
