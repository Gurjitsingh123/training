import hashlib
s='<gurjitsingh>'
d=hashlib.md5(s.encode())
print(d.hexdigest())
