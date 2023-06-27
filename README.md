Sem - 3: Mini Project  

# Python-Firewall
The above code is a simple packet filtering firewall. The firewall looks for TCP, and UDP packets, compares the header information of those to the rules in the rule list(Rules.csv). If any matching rule is found, the required action is performed(accept/ deny). If no exact rule is found to match with the packet header information, the packet is dropped. 

# System Requirements  
- Any Linux distribution
- required python imports(psutil)  

# Running instructions  
### Cloning the folder into local system
```sh
git clone git@github.com:preethika-ajay/Python-Firewall.git
cd Python-Firewall
```  

### Running the project  
```sh
sudo python3 main.py
```
