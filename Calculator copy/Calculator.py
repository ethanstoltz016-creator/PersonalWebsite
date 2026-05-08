#import 
#import functions from another file
#from File import _____
import re
try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

try:
    import PySimpleGUI as sg
except ImportError:
    sg = None

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

conversion_options_by_category = {
    "Length": [
        ("in to ft (if)", "if", "inches", "feet", in2ft),
        ("ft to in (fi)", "fi", "feet", "inches", ft2in),
        ("in to mm", "in2mm", "inches", "mm", in2mm),
        ("mm to in", "mm2in", "mm", "inches", mm2in),
        ("in to cm", "in2cm", "inches", "cm", in2cm),
        ("cm to in", "cm2in", "cm", "inches", cm2in),
        ("cm to m", "cm2m", "cm", "meters", cm2m),
        ("m to cm", "m2cm", "meters", "cm", m2cm),
        ("mm to m", "mm2m", "mm", "meters", mm2m),
        ("m to mm", "m2mm", "meters", "mm", m2mm),
        ("yd to m", "yd2m", "yards", "meters", yd2m),
        ("m to yd", "m2yd", "meters", "yards", m2yd),
        ("mi to km (mk)", "mk", "miles", "kilometers", mi2km),
        ("km to mi (km)", "km", "kilometers", "miles", km2mi),
    ],
    "Area": [
        ("sq ft to sq m", "sqft2sqm", "sq ft", "sq m", sqft2sqm),
        ("sq m to sq ft", "sqm2sqft", "sq m", "sq ft", sqm2sqft),
        ("sq in to sq cm", "sqin2sqcm", "sq in", "sq cm", sqin2sqcm),
        ("sq cm to sq in", "sqcm2sqin", "sq cm", "sq in", sqcm2sqin),
        ("sq mi to sq km", "sqmi2sqkm", "sq mi", "sq km", sqmi2sqkm),
        ("sq km to sq mi", "sqkm2sqmi", "sq km", "sq mi", sqkm2sqmi),
        ("acre to sq ft", "acre2sqft", "acres", "sq ft", acre2sqft),
        ("sq ft to acre", "sqft2acre", "sq ft", "acres", sqft2acre),
        ("acre to sq m", "acre2sqm", "acres", "sq m", acre2sqm),
        ("sq m to acre", "sqm2acre", "sq m", "acres", sqm2acre),
        ("acre to sq mi", "acre2sqmi", "acres", "sq mi", acre2sqmi),
        ("sq mi to acre", "sqmi2acre", "sq mi", "acres", sqmi2acre),
        ("acre to sq km", "acre2sqkm", "acres", "sq km", acre2sqkm),
        ("sq km to acre", "sqkm2acre", "sq km", "acres", sqkm2acre),
        ("acre to sq yd", "acre2sqyd", "acres", "sq yd", acre2sqyd),
        ("sq yd to acre", "sqyd2acre", "sq yd", "acres", sqyd2acre),
        ("acre to hectare", "acre2hectare", "acres", "hectares", acre2hectare),
        ("hectare to acre", "hectare2acre", "hectares", "acres", hectare2acre),
    ],
    "Temperature": [
        ("c to f (cf)", "cf", "celsius", "fahrenheit", c2f),
        ("f to c (fc)", "fc", "fahrenheit", "celsius", f2c),
        ("c to r (cr)", "cr", "celsius", "rankine", c2r),
        ("r to c (rc)", "rc", "rankine", "celsius", r2c),
        ("c to K (cK)", "cK", "celsius", "Kelvin", c2K),
        ("K to c (Kc)", "Kc", "Kelvin", "celsius", K2c),
        ("f to K (fK)", "fK", "fahrenheit", "Kelvin", f2K),
        ("K to f (Kf)", "Kf", "Kelvin", "fahrenheit", K2f),
        ("K to r (Kr)", "Kr", "Kelvin", "rankine", K2r),
        ("r to K (rK)", "rK", "rankine", "Kelvin", r2K),
    ],
    "Volume": [
        ("tsp to tbsp", "tsp2tbsp", "tsp", "tbsp", tsp2tbsp),
        ("tbsp to tsp (tbts)", "tbts", "tbsp", "tsp", tbsp2tsp),
        ("tbsp to oz", "tbsp2oz", "tbsp", "oz", tbsp2oz),
        ("oz to tbsp", "oz2tbsp", "oz", "tbsp", oz2tbsp),
        ("oz to cups (oc)", "oc", "oz", "cups", oz2cups),
        ("cups to oz (co)", "co", "cups", "oz", cups2oz),
        ("cups to pints", "cups2pints", "cups", "pints", cups2pints),
        ("pints to cups", "pints2cups", "pints", "cups", pints2cups),
        ("pints to quarts", "pints2quarts", "pints", "quarts", pints2quarts),
        ("quarts to pints", "quarts2pints", "quarts", "pints", quarts2pints),
        ("quarts to gallons", "quarts2gallons", "quarts", "gallons", quarts2gallons),
        ("gallons to quarts", "gallons2quarts", "gallons", "quarts", gallons2quarts),
        ("ml to tsp", "ml2tsp", "ml", "tsp", ml2tsp),
        ("tsp to ml", "tsp2ml", "tsp", "ml", tsp2ml),
        ("ml to tbsp", "ml2tbsp", "ml", "tbsp", ml2tbsp),
        ("tbsp to ml", "tbsp2ml", "tbsp", "ml", tbsp2ml),
        ("ml to cups", "ml2cups", "ml", "cups", ml2cups),
        ("cups to ml", "cups2ml", "cups", "ml", cups2ml),
        ("ml to fl oz", "ml2floz", "ml", "fl oz", ml2floz),
        ("fl oz to ml", "floz2ml", "fl oz", "ml", floz2ml),
        ("liters to gallons", "liters2gallons", "liters", "gallons", liters2gallons),
        ("gallons to liters", "gallons2liters", "gallons", "liters", gallons2liters),
        ("liters to cups", "liters2cups", "liters", "cups", liters2cups),
        ("cups to liters", "cups2liters", "cups", "liters", cups2liters),
    ],
    "Mass/Weight": [
        ("mg to g", "mg2g", "mg", "g", mg2g),
        ("g to mg", "g2mg", "g", "mg", g2mg),
        ("g to kg", "g2kg", "g", "kg", g2kg),
        ("kg to g", "kg2g", "kg", "g", kg2g),
        ("g to oz", "g2oz", "g", "oz", g2oz),
        ("oz to g", "oz2g", "oz", "g", oz2g),
        ("kg to lbs (lk)", "lk", "kg", "lbs", kg2lbs),
        ("lbs to kg (kl)", "kl", "lbs", "kg", lbs2kg),
        ("kg to stones", "kg2stones", "kg", "stones", kg2stones),
        ("stones to kg", "stones2kg", "stones", "kg", stones2kg),
        ("kg to metric tons", "kg2metric_tons", "kg", "metric tons", kg2metric_tons),
        ("metric tons to kg", "metric_tons2kg", "metric tons", "kg", metric_tons2kg),
        ("lbs to oz", "lbs2oz", "lbs", "oz", lbs2oz),
        ("oz to lbs", "oz2lbs", "oz", "lbs", oz2lbs),
        ("stones to lbs", "stones2lbs", "stones", "lbs", stones2lbs),
        ("lbs to stones", "lbs2stones", "lbs", "stones", lbs2stones),
        ("metric tons to lbs", "metric_tons2lbs", "metric tons", "lbs", metric_tons2lbs),
        ("lbs to metric tons", "lbs2metric_tons", "lbs", "metric tons", lbs2metric_tons),
    ],
    "Speed": [
        ("mph to kmph (mk)", "mk_speed", "mph", "kmph", mph2kmph),
        ("kmph to mph (km)", "km_speed", "kmph", "mph", kmph2mph),
        ("mph to m/s", "mph2mps", "mph", "m/s", mph2mps),
        ("m/s to mph", "mps2mph", "m/s", "mph", mps2mph),
        ("kmph to m/s", "kmph2mps", "kmph", "m/s", kmph2mps),
        ("m/s to kmph", "mps2kmph", "m/s", "kmph", mps2kmph),
        ("knots to mph", "knots2mph", "knots", "mph", knots2mph),
        ("mph to knots", "mph2knots", "mph", "knots", mph2knots),
        ("knots to kmph", "knots2kmph", "knots", "kmph", knots2kmph),
        ("kmph to knots", "kmph2knots", "kmph", "knots", kmph2knots),
        ("knots to m/s", "knots2mps", "knots", "m/s", knots2mps),
        ("m/s to knots", "mps2knots", "m/s", "knots", mps2knots),
        ("ft/s to mph", "fts2mph", "ft/s", "mph", fts2mph),
        ("mph to ft/s", "mph2fts", "mph", "ft/s", mph2fts),
        ("ft/s to m/s", "fts2mps", "ft/s", "m/s", fts2mps),
        ("m/s to ft/s", "mps2fts", "m/s", "ft/s", mps2fts),
        ("ft/s to kmph", "fts2kmph", "ft/s", "kmph", fts2kmph),
        ("kmph to ft/s", "kmph2fts", "kmph", "ft/s", kmph2fts),
    ],
    "Custom function": [("f(x) [single/table/graph]", "fx", "x", "y", None)],
}

conversion_map = {}
for category, conversions in conversion_options_by_category.items():
    for item in conversions:
        conversion_map[item[0]] = item


def run_gui():
    if sg is None:
        print("PySimpleGUI is not installed. Run the GUI.")
        return

    categories = list(conversion_options_by_category.keys())
    default_category = categories[0]
    default_conversions = [item[0] for item in conversion_options_by_category[default_category]]

    layout = [
        [sg.Text("Select Category:"),
        sg.Combo(
            categories,
            default_value=default_category,
            key='-CAT-',
            size=(35,1),
            enable_events=True
        )],

        [sg.Text("Select conversion or custom function:")],

        [sg.Combo(
            default_conversions,
            default_value=default_conversions[0],
            key='-OP-',
            size=(35,1)
        )],

        [sg.Text("Numeric input / x value:"), sg.Input(key='-VAL-', size=(20,1))],
        [sg.Text("Function expression:"), sg.Input(key='-EXPR-', size=(35,1))],

        [sg.Text('Mode:'),
        sg.Radio('Single value', 'MODE', default=True, key='-MODE-S-'),
        sg.Radio('Table', 'MODE', key='-MODE-T-'),
        sg.Radio('Graph', 'MODE', key='-MODE-G-')],

        [sg.Button('Calculate'), sg.Button('Clear'), sg.Button('Exit')],
        [sg.Multiline(key='-OUT-', size=(80,20), disabled=True, autoscroll=True)],
    ]

    window = sg.Window('Converter Calculator', layout, finalize=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        
        # Handle category change
        if event == '-CAT-':
            selected_category = values['-CAT-']
            new_conversions = [item[0] for item in conversion_options_by_category[selected_category]]
            window['-OP-'].update(values=new_conversions, value=new_conversions[0])
            continue
        
        if event == 'Clear':
            window['-OUT-'].update('')
            continue

        selection = values['-OP-']
        output = ''

        if selection == 'f(x) [single/table/graph]':
            expr = values['-EXPR-'].strip()
            if not expr:
                output = 'Enter a function expression.'
            elif values['-MODE-S-']:
                try:
                    x_val = float(values['-VAL-'])
                except ValueError:
                    output = 'Enter a valid x value.'
                else:
                    result = safe_eval(expr, x_val)
                    output = result if isinstance(result, str) else f'{round(result, 2)}'
            elif values['-MODE-T-']:
                output_lines = ['x | y', '-----']
                for i in range(-20, 21):
                    x_val = i / 10
                    result = safe_eval(expr, x_val)
                    output_lines.append(
                        f'{x_val} | {result}' if isinstance(result, str) else f'{x_val} | {round(result, 2)}'
                    )
                output = '\n'.join(output_lines)
            elif values['-MODE-G-']:
                plot_expr(expr)
                output = 'Graph displayed.'
            else:
                output = 'Invalid mode.'
        else:
            try:
                selected = conversion_map[selection]
            except KeyError:
                output = 'Select a valid operation.'
            else:
                try:
                    value = float(values['-VAL-'])
                except ValueError:
                    output = f'Enter a valid {selected[2]} value.'
                else:
                    result = selected[4](value)
                    output = f'{value} {selected[2]} = {round(result, 2)} {selected[3]}'

        window['-OUT-'].update(output)

    window.close()


def run_cli():
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

if __name__ == '__main__':
    if sg is not None:
        run_gui()
    else:
        run_cli()
