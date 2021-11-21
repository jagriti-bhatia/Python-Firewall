# Python-Firewall
The above code is a simple packet filtering firewall. The firewall looks for TCP, and UDP packets, compares the header information of thosto the rules in the rule list(Rules.csv). If any matching rule is found, the required action is performed(accept/ deny). If no exact rule is found to match with the packet heade information, the packet is dropped. 

# System Requirements  
- Ubuntu
- required python imports(psutil)  

# Running instructions  
```sh
git clone git@github.com:preethika-ajay/Python-Firewall.git
cd Python-Firewall
sudo python3 main.py
```
