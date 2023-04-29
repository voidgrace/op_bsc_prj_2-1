class Car:
    color=""
    speed=0

    def upSpeed(self,value):
        self.speed+=value

    def downSpeed(self,value):
        self.speed-=value

    def printMessage(self):
        print("시험 출력이다.")

