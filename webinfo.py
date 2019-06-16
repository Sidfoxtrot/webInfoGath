import requests
url=input("Enter the url to get header info:")
URL=url
def headerinfo():
    global url
    udata = requests.get(url,verify=False)
    print("Server:"+udata.headers['Server'])
    print("Technology Used:"+udata.headers['content-type'])
    contenttype=udata.headers['content-type']
    if contenttype:
        print("Content-Type available")
    else:
        print("Content-Type not available")
    print("--------------------")
    url=URL
def robot():
    print("Checking for robots.txt")
    global url
    url+="/robots.txt"
    udata = requests.get(url,verify=False)
    if int(udata.status_code)==200:
        print("Robots.txt is available")
        print ("Response: ",udata.content)
    else:
        print("Robots.txt is'nt available")
    print("--------------------")
    url=URL
def directorytraversal():
    print("Checking for Directory Traversal")
    global url
    payload=input("Enter the payload:")
    equal = url.find("=")
    found = url[:equal + 1] + url + payload
    udata = requests.get(found, verify=False)
    if "www-data".encode() in udata.content:
        print ("Directory traversal is possible with "+ payload)
        print ("Response: ",udata.content)
    else:
        print ("Directory traversal isn't possible")
if __name__ == "__main__":
	try:
		headerinfo()
		robot()
		directorytraversal()
	except KeyboardInterrupt: 
		exit()
            
    
