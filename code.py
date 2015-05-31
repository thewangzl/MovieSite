#! /usr/bin/env python

import web

#render = web.template.render('templates/')
render = web.template.render('templates/')
db = web.database(dbn='sqlite',db='MovieSite.db')

urls = (
	'/','index',
        '/movie/(.*)','movie',
	'/cast/(.*)','cast',
	'/director/(.*)','director'
)

class index:
	def GET(self):
		movies = db.select('movie')
		return render.index(movies)
	def POST(self):
		data = web.input()
		condition = r'title like "%' + data.title + r'%"'
		movies = db.select('movie',where=condition)
		return render.index(movies)
class movie:
	def GET(self,movie_id):
#		movie_id = int(movie_id)
#		condition = 'id=' + movie_id
#		movie = db.select('movie',where=condition,vars=locals())[0]
		movie = db.select('movie',where='id=$int(movie_id)',vars=locals())[0]
		return render.movie(movie)

class cast :
	def GET(self,cast_name):
		condition = r'casts like "%' + cast_name + r'%"'
		movies = db.select('movie',where = condition)
		return render.index(movies)

class director:
	def GET(self,director_name):
		condition = r'directors like "%' + director_name + r'%"'
		movies = db.select('movie',where = condition)
		return render.index(movies)


if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()


