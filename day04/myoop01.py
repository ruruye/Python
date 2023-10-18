class Vehicle:
    def __init__(self):
        self.wheel_cnt = 2
    def flex(self):
        self.wheel_cnt = 4
        
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.autopilot_level = 1
        
    def hit(self):
        self.autopilot_level += 1
        
if __name__ == "__main__":
    c = Car()
    print(c.wheel_cnt)
    print(c.autopilot_level)
    c.flex()
    c.hit()
    c.hit()
    c.hit()
    print(c.wheel_cnt)
    print(c.autopilot_level)   