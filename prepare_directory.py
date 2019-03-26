import os

base_path = os.getcwd()
data_path = base_path + '/data'
chunks_path = data_path + '/uri_chunks'

try:
	os.makedirs(data_path)
except OsError:
	pass

try:
	os.makedirs(chunks_path)
except OsError:
	pass
