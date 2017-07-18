from datetime import datetime

def days_until(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

a = str(datetime.today())

class Front_Page(object):
    def __init__(self):
        self.heading = "heading"
        self.body = "Any sufficiently advanced technology is indisguishable from magic. --Arthur C. Clarke"
        self.until = days_until(a[:10],'2017-10-14')

class cls_WhoTheyAre(object):
    def __init__(self):
        self.heading = "Who They Are"
        self.MMDtitle = "Meaghan Mary Durgin"
        self.MMDdesc = ""
        self.ACKtitle = "Andrew Currin Katz"
        self.ACKdesc = ""

class cls_Event(object):
    def __init__(self, heading, datetime, description):
        self.heading = heading
        self.datetime = datetime
        self.description = description

class cls_Wedding(object):
    def __init__(self, heading, datetime, description):
        self.heading = heading
        self.datetime = datetime
        self.description = description


class cls_Registry(object):
    def __init__(self):
        self.heading = "Registry"
        self.datetime = "Registry"
        self.description = "Registry"

class cls_Hotel(object):
    def __init__(self):
        self.heading = "Hotel"
        self.datetime = "Hotel"
        self.description = "Hotel"

class cls_Bridesmaids(object):
    def __init__(self):
        self.heading = "Bridesmaids"
        self.datetime = "Bridesmaids"
        self.description = "Bridesmaids"

class cls_Groomsmen(object):
    def __init__(self):
        self.heading = "Groomsmen"
        self.datetime = "Groomsmen"
        self.description = "Groomsmen"

class cls_musicsubmission(object):
    def __init__(self):
        self.heading = "Groomsmen"

#    def go(self, direction):
#        return self.paths.get(direction, None)

#    def add_paths(self, paths):
#        self.paths.update(paths)


front = Front_Page()

#front = Front_Page(
#"Welcome to Meaghan and Andy's wedding website",
#"Any sufficiently advanced technology is indistinguishable from magic. --Arthur C. Clarke"
#,days_until(a[:10],'2017-10-14')
#,datetime.today()
#,"d"
#)

wth = cls_WhoTheyAre()

inst_rd = cls_Event(
"Rehearsal dinner",
"Rehearsal dinner",
"Rehearsal dinner"
)

inst_wedd = cls_Wedding(
"Wedding",
"Wedding",
"Wedding"
)

inst_registry = cls_Registry()
inst_hotel = cls_Hotel()
inst_bridesmaids = cls_Bridesmaids()
inst_groomsmen = cls_Groomsmen()
