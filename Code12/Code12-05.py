class Car:
    color=""
    speed=0

    def __init__(self,name,speed):
        self.name=name
        self.speed=speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed


Car1=Car("아우디",0)
Car2=Car("벤츠",30)

print("%s의 현재 속도는 %d입니다."%(Car1.getName(),Car1.getSpeed()))
print("%s의 현재 속도는 %d입니다."%(Car2.getName(),Car2.getSpeed()))