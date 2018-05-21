# Author: John Paul Antonovich
import random
from datetime import tzinfo, timedelta, datetime, timezone
from pprint import pprint
import os
import sqlite3
import time

class NeatStuff():
    def __init__(self, docDate=None, cFold=None, creditMsg=None):
        self.docDate = datetime.today().strftime('%Y-%m-%d')
        self.cFold = os.path.dirname(os.path.abspath(__file__))
        self.creditMsg = "Using the 'NeatStuff' class by John Paul Antonovich"
        self.credit()

    def credit(self):
        print(self.creditMsg)

    def formDocDate(self):
        return self.docDate

    def findCF(self):
        return self.cFold

    def seeT(self, test):
        if bool(test) == True:
            print(str(test) + " is true")
        else:
            print(str(test) + " is false")

    def eEnter(self):
        input('Press enter to quit the program... ')

    def fancyWait(self, timeWaiting):
        counter = 0
        while timeWaiting > counter:
            print('Please Wait...')
            time.sleep(1)
            counter += 1

    def likeProgram(self):
        conn = sqlite3.connect('likeP.db')
        cc = conn.cursor()

        cc.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix, like TEXT, dislike TEXT)')
        unix = time.time()
        while True:
            askOp = input('Do you like this program? Y/N ')
            if askOp.lower() == 'y' or askOp.lower() == 'yes':
                cc.execute("INSERT INTO stuffToPlot (unix, like) VALUES (?, ?)",(unix, 'Liked'))
                conn.commit()
                cc.execute("SELECT like, dislike FROM stuffToPlot WHERE unix > 1493257438")
                for row in cc.fetchall():
                    print(row)
                cc.close()
                conn.close()
                break
            elif askOp.lower() == 'n' or askOp.lower() == 'no':
                cc.execute("INSERT INTO stuffToPlot (unix, dislike) VALUES (?, ?)",(unix, 'Disliked'))
                conn.commit()
                cc.execute("SELECT like, dislike FROM stuffToPlot WHERE unix > 1493257438")
                for row in cc.fetchall():
                    print(row)
                cc.close()
                conn.close()
                break
            else:
                continue
