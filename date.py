from re import M


class Date():
    def __init__(self, year=0, month=0, day=0, hour=0, minute=0, string=None):
        if(string == None):
            self.y = year
            self.m = month
            self.d = day
            self.h = hour
            self.min = minute
        else:
            ymd_hm = string.split(' ')
            ymd = ymd_hm[0].split('-')
            hm = ymd_hm[1].split(':')
            self.y = int(ymd[0])
            self.m = int(ymd[1])
            self.d = int(ymd[2])
            self.h = int(hm[0])
            self.min = int(hm[1])
            print(self)
    
    def __str__(self):
        ymd = str(self.y) + '-' + str(self.m) + '-' + str(self.d)
        ymd += ' ' + str(self.h) + ':' + str(self.min)

        return ymd

    def toId(self):
        return str(self.y*10000 + self.m*100 + self.d)
