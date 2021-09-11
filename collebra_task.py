import requests,json
response=requests.get("https://api.macaddress.io/v1?apiKey=at_DQLKi4GdsLTD93cJIKFmkMwgDBl9H&output=json&search=44:38:39:ff:ef:57")
print(response)
print(response.json())

b={'vendorDetails': {'oui': '443839', 'isPrivate': False, 'companyName': 'Cumulus Networks, Inc', 'companyAddress': '650 Castro Street, suite 120-245 Mountain View CA 94041 US', 'countryCode': 'US'}, 'blockDetails': {'blockFound': True, 'borderLeft': '443839000000', 'borderRight': '443839FFFFFF', 'blockSize': 16777216, 'assignmentBlockSize': 'MA-L', 'dateCreated': '2012-04-08', 'dateUpdated': '2015-09-27'}, 'macAddressDetails': {'searchTerm': '44:38:39:ff:ef:57', 'isValid': True, 'virtualMachine': 'Not detected', 'applications': ['Multi-Chassis Link Aggregation (Cumulus Linux)'], 'transmissionType': 'unicast', 'administrationType': 'UAA', 'wiresharkNotes': 'No details', 'comment': ''}}
print(b["macAddressDetails"]["searchTerm"])
#print(b['vendorDetails']['companyName'])
#completed task
