import urllib.request as ur

url = 'http://quotesondesign.com/wp-json/posts'
conn = ur.urlopen(url)

data = conn.read()

print(conn.status)
print(data)


for key, value in conn.getheaders():
	print("key: ", key, ", value: ", value)