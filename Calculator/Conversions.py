#in to mm
def in2mm(inches):
    return inches*25.4
def mm2in(mm):
    return mm/25.4

#in to ft 
def in2ft(inches):
    return inches/12
def ft2in(ft):
    return ft*12
#---------------------------------------------------------------------------
#celsius to fahrenheit
def c2f(c):
    return ((c*(9/5))+32)
def f2c(f):
    return ((f-32)*(5/9))

#celsius to rankine
def c2r(c):
    return (c*(9/5)+491.67) 
def r2c(r):
    return ((r-491.67)/(9/5))

#celsius to Kelvin
def c2K(c):
    return (c+273.15)
def K2c(K):
    return (K-273.15)

#fahrenheit to Kelvin 
def f2K(f):
    return (((f-32)*(5/9))+273.15)
def K2f(K):
    return (((K-273.15)*(9/5))+32)
    
#Kelvin to rankine
def K2r(K):
    return (K*(9/5))
def r2K(r):
    return (r/(9/5))
#---------------------------------------------------------------------------
#oz to cups
def oz2cups(oz):
    return oz/8
def cups2oz(cups):
    return cups*8

#tbsp to tsp
def tbsp2tsp(tbsp):
    return tbsp*3
def tsp2tbsp(tsp):
    return tsp/3

#mph to kmph
def mph2kmph(mph):
    return mph*1.60934
def kmph2mph(kmph):
    return kmph/1.60934

#kg to lbs
def kg2lbs(kg):
    return kg*2.2
def lbs2kg(lbs):
    return lbs/2.2
