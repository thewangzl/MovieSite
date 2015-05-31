import urllib
import json
import time

movie_ids = []
for index in range(0,250,50):
	print index
	response = urllib.urlopen('http://api.douban.com/v2/movie/top250?start=%d&count=50' % index)
	data = response.read()
	data_json = json.loads(data)
	#print data
	movie250 = data_json['subjects']
	for movie in movie250:
		movie_ids.append(movie['id'])
		print movie['id'],movie['title']
	time.sleep(3)
print movie_ids
