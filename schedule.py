import json
from date import Date

class Schedule():
    def __init__(self, fname):
        self.fname = fname
        file = open(fname + '.json')
        self.sch = json.load(file)
        file.close()

    def newEvent(self, name, date, notes):
        new_id = date.toId()
        ids = list(self.sch.keys())
        count = 0
        for id in ids:
            if(id.__contains__(new_id)):
                count += 1
        new_id += str(count+1)
        
        self.sch.update({new_id: [name, str(date), notes]})
        file = open(self.fname + '.json', 'w')
        json.dump(self.sch, file)
        file.close()
        

        