import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json

USER = input("Enter your login username:  ") 
PASSWORD = getpass ("Enter the password associated with the username: ")


home = 'https://sandboxdnac.cisco.com'
pathTok = '/dna/system/api/v1/auth/token'
vlan = '/dna/intent/api/v1/topology/vlan/vlan-names'

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

authToken = home + pathTok

resp = requests.post(authToken, auth=HTTPBasicAuth(USER, PASSWORD), headers=headers, data=payload)

tJ = resp.json()

TOKEN = tJ['Token']

ciscoVlan = home + vlan

getpayload={}
getheaders = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-Auth-Token': TOKEN ,
}

getresponse = requests.get(ciscoVlan, headers=getheaders, data=getpayload)

hi = getresponse.json()

print(hi)


