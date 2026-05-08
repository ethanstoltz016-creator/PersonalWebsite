#===========================================================================
# LENGTH CONVERSIONS
#===========================================================================

#Inches to Feet
def in2ft(inches):
    return inches/12
def ft2in(ft):
    return ft*12

#Inches to Millimeters
def in2mm(inches):
    return inches*25.4
def mm2in(mm):
    return mm/25.4

#Inches to Centimeters
def in2cm(inches): 
    return inches*2.54
def cm2in(cm):
    return cm/2.54

#Centimeters to Meters
def cm2m(cm):
    return cm/100
def m2cm(m):
    return m*100

#Millimeters to Meters
def mm2m(mm):
    return mm/1000
def m2mm(m):
    return m*1000

#Yards to Meters
def yd2m(yd):
    return yd*0.9144
def m2yd(m):
    return m/0.9144

#Miles to Kilometers
def mi2km(mi):
    return mi*1.60934
def km2mi(km):
    return km/1.60934

#===========================================================================
# AREA CONVERSIONS
#===========================================================================

#Square Feet to Square Meters
def sqft2sqm(sqft):
    return sqft*0.092903
def sqm2sqft(sqm):
    return sqm/0.092903

#Square Inches to Square Centimeters
def sqin2sqcm(sqin):
    return sqin*6.4516
def sqcm2sqin(sqcm):
    return sqcm/6.4516

#Square Miles to Square Kilometers
def sqmi2sqkm(sqmi):    
    return sqmi*2.58999
def sqkm2sqmi(sqkm):
    return sqkm/2.58999

#Acres to Square Feet
def acre2sqft(acre):
    return acre*43560
def sqft2acre(sqft):
    return sqft/43560

#Acres to Square Meters
def acre2sqm(acre):
    return acre*4046.86
def sqm2acre(sqm):
    return sqm/4046.86

#Acres to Square Miles
def acre2sqmi(acre):
    return acre*0.0015625
def sqmi2acre(sqmi):
    return sqmi/0.0015625

#Acres to Square Kilometers
def acre2sqkm(acre):
    return acre*0.00404686
def sqkm2acre(sqkm):
    return sqkm/0.00404686

#Acres to Square Yards
def acre2sqyd(acre):
    return acre*4840
def sqyd2acre(sqyd):
    return sqyd/4840

#Acres to Hectares
def acre2hectare(acre):
    return acre*0.404686
def hectare2acre(hectare):
    return hectare/0.404686

#===========================================================================
# TEMPERATURE CONVERSIONS
#===========================================================================

#Celsius to Fahrenheit
def c2f(c):
    return ((c*(9/5))+32)
def f2c(f):
    return ((f-32)*(5/9))

#Celsius to Rankine
def c2r(c):
    return (c*(9/5)+491.67) 
def r2c(r):
    return ((r-491.67)/(9/5))

#Celsius to Kelvin
def c2K(c):
    return (c+273.15)
def K2c(K):
    return (K-273.15)

#Fahrenheit to Kelvin 
def f2K(f):
    return (((f-32)*(5/9))+273.15)
def K2f(K):
    return (((K-273.15)*(9/5))+32)
    
#Kelvin to Rankine
def K2r(K):
    return (K*(9/5))
def r2K(r):
    return (r/(9/5))

#===========================================================================
# VOLUME/COOKING CONVERSIONS
#===========================================================================

#Teaspoons to Tablespoons
def tsp2tbsp(tsp):
    return tsp/3
def tbsp2tsp(tbsp):
    return tbsp*3

#Tablespoons to Ounces
def tbsp2oz(tbsp):
    return tbsp/2
def oz2tbsp(oz):
    return oz*2

#Ounces to Cups
def oz2cups(oz):
    return oz/8
def cups2oz(cups):
    return cups*8

#Cups to Pints
def cups2pints(cups):
    return cups/2
def pints2cups(pints):
    return pints*2

#Pints to Quarts
def pints2quarts(pints):
    return pints/2
def quarts2pints(quarts):
    return quarts*2

#Quarts to Gallons
def quarts2gallons(quarts):
    return quarts/4
def gallons2quarts(gallons):
    return gallons*4

#Milliliters to Teaspoons
def ml2tsp(ml):
    return ml/4.929
def tsp2ml(tsp):
    return tsp*4.929

#Milliliters to Tablespoons
def ml2tbsp(ml):
    return ml/14.787
def tbsp2ml(tbsp):
    return tbsp*14.787

#Milliliters to Cups
def ml2cups(ml):
    return ml/236.588
def cups2ml(cups):
    return cups*236.588

#Milliliters to Fluid Ounces
def ml2floz(ml):
    return ml/29.574
def floz2ml(floz):
    return floz*29.574

#Liters to Gallons (US)
def liters2gallons(liters):
    return liters/3.78541
def gallons2liters(gallons):
    return gallons*3.78541

#Liters to Cups
def liters2cups(liters):
    return liters*4.22675
def cups2liters(cups):
    return cups/4.22675

#===========================================================================
# MASS/WEIGHT CONVERSIONS
#===========================================================================

#Milligrams to Grams
def mg2g(mg):
    return mg/1000
def g2mg(g):
    return g*1000

#Grams to Kilograms
def g2kg(g):
    return g/1000
def kg2g(kg):
    return kg*1000

#Grams to Ounces
def g2oz(g):
    return g/28.3495
def oz2g(oz):
    return oz*28.3495

#Kilograms to Pounds
def kg2lbs(kg):
    return kg*2.20462
def lbs2kg(lbs):
    return lbs/2.20462

#Kilograms to Stones
def kg2stones(kg):
    return kg/6.35029
def stones2kg(stones):
    return stones*6.35029

#Kilograms to Metric Tons
def kg2metric_tons(kg):
    return kg/1000
def metric_tons2kg(tons):
    return tons*1000

#Pounds to Ounces
def lbs2oz(lbs):
    return lbs*16
def oz2lbs(oz):
    return oz/16

#Stones to Pounds
def stones2lbs(stones):
    return stones*14
def lbs2stones(lbs):
    return lbs/14

#Metric Tons to Pounds
def metric_tons2lbs(tons):
    return tons*2204.62
def lbs2metric_tons(lbs):
    return lbs/2204.62

#===========================================================================
# SPEED CONVERSIONS
#===========================================================================

#Miles Per Hour to Kilometers Per Hour
def mph2kmph(mph):
    return mph*1.60934
def kmph2mph(kmph):
    return kmph/1.60934

#Miles Per Hour to Meters Per Second
def mph2mps(mph):
    return mph*0.44704
def mps2mph(mps):
    return mps/0.44704

#Kilometers Per Hour to Meters Per Second
def kmph2mps(kmph):
    return kmph/3.6
def mps2kmph(mps):
    return mps*3.6

#Knots to Miles Per Hour
def knots2mph(knots):
    return knots*1.15078
def mph2knots(mph):
    return mph/1.15078

#Knots to Kilometers Per Hour
def knots2kmph(knots):
    return knots*1.852
def kmph2knots(kmph):
    return kmph/1.852

#Knots to Meters Per Second
def knots2mps(knots):
    return knots*0.51444
def mps2knots(mps):
    return mps/0.51444

#Feet Per Second to Miles Per Hour
def fts2mph(fts):
    return fts*0.68182
def mph2fts(mph):
    return mph/0.68182

#Feet Per Second to Meters Per Second
def fts2mps(fts):
    return fts*0.3048
def mps2fts(mps):
    return mps/0.3048

#Feet Per Second to Kilometers Per Hour
def fts2kmph(fts):
    return fts*1.09728
def kmph2fts(kmph):
    return kmph/1.09728
