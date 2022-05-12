import math

def haversine(r,x1,y1,x2,y2): 
    domx = [-90,90]
    domy = [-180,180]
        
    t1 = (x2 - x1)/2
    t2 = (y1 - y2)/2
    
    x1r = math.radians(x1)
    x2r = math.radians(x2)
    t1r = math.radians(t1)
    t2r = math.radians(t2)
    
    t3 = math.sin(t1r) ** 2
    t4 = math.sin(t2r) ** 2
    
    t5 = t3 + (math.cos(x1r)*math.cos(x2r)*t4)
    t6 = t5**0.5
    arcsin_valor = math.asin(t6)
    d = 2*r*arcsin_valor
    
    return d
    
    