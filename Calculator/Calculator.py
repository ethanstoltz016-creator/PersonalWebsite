#import 
#import functions from another file
#from File import _____
import re
try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

from Conversions import *  #* = wildcard or everything
#from Conversions  import specificF(x)

#global variables/objects
menu = '''
    in to ft (if)           mph to kph (mk)
    ft to in (fi)           kph to mph (km)
                            
    tbsp to tsp (tbts)      lbs to kg (lk)
    tsp to tbsp (tstb)      kg to lbs (kl)
                            
    c to f (cf)             oz to cups (oc)
    f to c (fc)             cups to oz (co)
    
    c to r (cr)             c to K (cK)
    r to c (rc)             K to c (Kc)

    f to K (fK)             K to r (Kr)
    K to f (Kf)             r to K (rK)

    f(x) (fx)  [single/table/graph]

    stop (stop)

What woud you like to do?
'''

def safe_eval(expr, x):
    expr = expr.strip()
    if expr.lower().startswith('y='):
        expr = expr[2:].strip()
    expr = expr.replace('^', '**')  # Allow ^ for exponents

    # Convert implicit multiplication like 2x, x2, x(x), and )x
    expr = re.sub(r'(?<=\d)\s*(?=x)', '*', expr)
    expr = re.sub(r'(?<=x)\s*(?=\d|\()', '*', expr)
    expr = re.sub(r'(?<=\))\s*(?=x|\()', '*', expr)
    expr = re.sub(r'(?<=\d)\s*(?=\()', '*', expr)

    allowed_names = {"x": x, "__builtins__": {}}
    try:
        return eval(expr, {"__builtins__": {}}, allowed_names)
    except Exception as e:
        return f"Error: {e}"


def plot_expr(expr, x_min=-2, x_max=2, step=0.1):
    if not MATPLOTLIB_AVAILABLE:
        print("Graph mode requires matplotlib, which is not installed.")
        return

    xs = [round(x_min + i * step, 10) for i in range(int((x_max - x_min) / step) + 1)]
    ys = []
    for x in xs:
        result = safe_eval(expr, x)
        if isinstance(result, str):
            print(f"Error evaluating expression at x={x}: {result}")
            return
        ys.append(result)

    plt.figure()
    plt.plot(xs, ys, marker='o')
    plt.title(f"y = {expr}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#main loop
user = input(menu)
while(user!="stop"):
    if user == "if":
        print(round(in2ft(float(input("inches: "))), 2))
        pass  #pass is when you need a place holder to pass
                #   through the conditional and skip stuff
    elif user == "fi":
        print(round(ft2in(float(input("ft: "))), 2))
        pass
    elif user == "mk":
        print(round(mph2kmph(float(input("mph: "))), 2))
        pass
    elif user == "km":
        print(round(kmph2mph(float(input("kmph: "))), 2))
        pass
    elif user == "tbts":
        print(round(tbsp2tsp(float(input("tbsp: "))), 2))
        pass
    elif user == "tstb":
        print(round(tsp2tbsp(float(input("tsp: "))), 2))
        pass
    elif user == "lk":
        print(round(lbs2kg(float(input("lbs: "))), 2))
        pass
    elif user == "kl":
        print(round(kg2lbs(float(input("kg: "))), 2))
        pass
#---------------------------------------------------------------------------
    elif user == "cf":                                      #Celsius to Fahrenheit
        print(round(c2f(float(input("celsius: "))), 2))
        pass
    elif user == "fc":                                      #F to C
        print(round(f2c(float(input("fahrenheit: "))), 2))
        pass
    elif user == "cr":                                      #Celsius to Rankine
        print(round(c2r(float(input("celsius: "))), 2))
        pass
    elif user == "rc":                                      #R to C
        print(round(r2c(float(input("rankine: "))), 2))
        pass
    elif user == "cK":                                      #Celsius to Kelvin
        print(round(c2K(float(input("celsius: "))), 2))
        pass
    elif user == "Kc":                                      #K to C
        print(round(K2c(float(input("Kelvin: "))), 2))
        pass
    elif user == "fK":                                      #Fahrenheit to Kelvin
        print(round(f2K(float(input("fahrenheit: "))), 2))
        pass
    elif user == "Kf":                                      #K to f
        print(round(K2f(float(input("Kelvin: "))), 2))
        pass
    elif user == "Kr":                                      #Kelvin to rankine
        print(round(K2r(float(input("Kelvin: "))), 2))
        pass
    elif user == "rK":                                      #r to K
        print(round(r2K(float(input("rankine: "))), 2))
        pass
#---------------------------------------------------------------------------
    elif user == "fx":                                      #f(x)
        expr = input("Enter function (use x as variable): ")
        mode = input("Single value (s), table (t), or graph (g)? ").lower()
        if mode == "s":
            x = float(input("x: "))
            result = safe_eval(expr, x)
            if isinstance(result, str):
                print(result)
            else:
                print(round(result, 2))
        elif mode == "t":
            print("x | y")
            print("-----")
            for i in range(-20, 21):
                x_val = i / 10
                result = safe_eval(expr, x_val)
                if isinstance(result, str):
                    print(f"{x_val}|{result}")
                else:
                    print(f"{x_val}|{round(result, 2)}")
        elif mode == "g":
            plot_expr(expr)
        else:
            print("Invalid mode")
        pass
    elif user == "oc":                                      #Oz to Cups
        print(round(oz2cups(float(input("oz: "))), 2))
        pass
    elif user == "co":                                      #C to O
        print(round(cups2oz(float(input("cups: "))), 2))
        pass
    else:
        print("I'm sorry I didn't quite get that")
    user = input(menu)
