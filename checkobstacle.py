def check(x,y,radius):
        if (x == 150 and y<=250+radius):#firstbound            
            x = 10
            y = 0
        elif y == 150 and (x>=275-radius and x<=370+radius):#second horizontal
            x = 10
            y = 0            
        elif x==275 and (y>=180 and y<=390+radius):#third
            x = 10
            y = 0
        elif x==500 and (y>=152-radius and y<=285+radius):#fourth
            x = 10
            y = 0
        elif x==625 and (y>=285-radius and y<=390+radius):#fifth
            x = 10
            y = 0
        elif y == 400:#lower horitzontal
            x = 10
            y = 0                         
        return x,y 