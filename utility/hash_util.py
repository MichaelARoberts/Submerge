import hashlib

BUFFSIZE = 1073741824

def hash_md5(file_data):
	hasher = hashlib.md5()
	with open(str(file_data),'rb') as f:
		buf = f.read(BUFFSIZE)

		while len(buf) > 0:
			hasher.update(buf)
			buf = f.read(BUFFSIZE)

	return hasher.hexdigest()

def hash_sha1(file_data):
	hasher = hashlib.sha1()
	with open(str(file_data),'rb') as f:
		buf = f.read(BUFFSIZE)

		while len(buf) > 0:
			hasher.update(buf)
			buf = f.read(BUFFSIZE)

	return hasher.hexdigest()
