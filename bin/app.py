import web
import os
from weddingwebsite import map
# export PYTHONPATH=$PYTHONPATH:.
# export PATH="/usr/local/bin:$PATH"
# PYTHONPATH is used by the python interpreter to determine which modules to load.
# PATH is used by the shell to determine which executables to run.


db = web.database(dbn='postgres', db="weddingwebsite", user='sid', pw='Blue8690')

urls = (
  '/whotheyare', 'cls_WhoTheyAre',
  '/','Index',
  '/rehearsaldinner', 'cls_Event',
  '/wedding', 'cls_Wedding',
  '/hotel', 'cls_Hotel',
  '/groomsmen', 'cls_Groomsmen',
  '/bridesmaids', 'cls_Bridesmaids',
  '/registry', 'cls_Registry',
  '/add', 'add',
  '/musicsubmission', 'cls_musicsubmission',
)

app = web.application(urls, globals())

# render = web.template.render('templates/')
render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        return render.front_page(map.front)

#    def POST(self):

class cls_WhoTheyAre(object):
    def GET(self):
        return render.who_they_are(map.wth)

class cls_Event(object):
    def GET(self):
        return render.event(map.inst_rd)

class cls_Wedding(object):
    def GET(self):
        MusicSubmissions = db.select('tblMusicSubmissions')
        return render.wedding(map.inst_wedd)
#    def GET(self):
#        todos = db.select('todo')
#        return render.wedding(todos)

class cls_musicsubmission:
    def GET(self):
        return render.musicsubmission(map.cls_musicsubmission)

class add:
    def POST(self):
        i = web.input()
        n = db.insert('tblMusicSubmissions', songtitle=i.songtitle, artist=i.artist)
        raise web.seeother('/musicsubmission')

class cls_Registry(object):
    def GET(self):
        return render.registry(map.inst_registry)

class cls_Hotel(object):
    def GET(self):
        return render.hotel(map.inst_hotel)


class cls_Bridesmaids(object):
    def GET(self):
        return render.bridesmaids(map.inst_bridesmaids)

class cls_Groomsmen(object):
    def GET(self):
        return render.groomsmen(map.inst_groomsmen)

if __name__ == "__main__":
    app.run()
