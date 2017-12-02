import time
import math

class WashingMachine():
    def __init__(self,temp=25,time=1,rotations=4,gentle=2,detergent=1,high=True):
        self.temp=temp
        self.time=time
        self.rotations=rotations
        self.gentle=gentle
        self.detergent=detergent
        self.high=high
    def rinse(self):
        '''
            rinses clothes
            '''
        self.temp=math.degrees(temp)
        return
    def spin(self):
        """
            spins clothes
            """
        self.rotations*=2
        return
    def wash(self):
        """
            washes clothes
            """
        self.detergent*=2
        self.time=+1
    
    def describe(self):
        print("The washing machine ran with these settings temp={} time={} rotations={} gentle{} detergent={} high={}".format(self.temp,self.time,self.rotations,self.gentle,self.detergent,self.high))

w1=WashingMachine()
w1.describe()

