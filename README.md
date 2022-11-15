# DNS Practice

Domain Name: 'wenjin.tech'

A record: 
- Host Name: `@`
- Value: `34.134.169.17`
- TTL: `7200`

This is currently linked to a VM instance from GCP 

Steps: 
1. Initiate a VM instance on either GCP or Azure
2. Once the VM is up and running run the following commands: 
```sh 
sudo apt-get update
sudo apt install python3-pip 
pip3 install flask 
sudo apt install python3-flask
```
The 
```sh 
sudo apt install python3-flask
``` 
line of code is to make sure that flask is installed on teh VM in case the previous code didnt work] 

3. Git Clone any github repo that has a python script for a flask app
4. Once the repo is cloned run the python scrip with 
```sh 
sudo python3 app.py
```