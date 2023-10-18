class Animal:
    def __init__(self):
        #print("생성자")
        self.flag_sound = True
        
    def bbeonguri(self):
        self.flag_sound = False
        
    def __del__(self):
        #print("소멸자")
        pass
        
    def __str__(self):
        return "소리능력"+str(self.flag_sound)
        
        

class Human(Animal):
    def __init__(self):
        super().__init__()
        self.community_skill = 0
        
    def momstouch(self, punch):
        self.community_skill += punch  
            
            
               
        
if __name__ == '__main__':
    h = Human()
    print(h.community_skill)
    print(h.flag_sound)
    h.bbeonguri()
    h.momstouch(10)
    print(h.community_skill)
    print(h.flag_sound)