#tutte le conversioni vengono fatte a partire dai kelvin

def toKelvin(temp):
    return (temp,'Kelvin');

def fromKelvin(temp):
    return temp;

def toCelsius(temp):
    return ((temp - 273.15),"Celsius")

def fromCelsius(temp):
    return temp + 273.15

def toFahrenheit(temp):
    return (temp * 9/5 - 459.67,"Fahrenheit")

def fromFahrenheit(twmp):
    return  (temp + 459.67) * 5/9

def toRankine(temp):
    return (temp * 9/5,"Rankine")

def fromRankine(tmep):
    return temp * 5/9

def toDelisle(temp):
    return ((373.15 - temp) * 3/2,"Delisle")

def fromDelisle(temp):
    return 373.15 - temp * 2/3

def toNewton(temp):
    return ((temp - 273.15) * 33/100,"Newton")

def fromNewton(temp):
    return temp * 100/33 + 273.15

def toReaumur(temp):
    return  ((temp - 273.15) * 4/5,"Reaumur")

def fromReaumur(temp):
    return temp * 5/4 + 273.15

def toRomer(temp):
    return  ((temp - 273.15) * 21/40 + 7.5, "Romer")

def fromRomer(temp):
    return (temp - 7.5) * 40/21 + 273.15

toFunctions = [toKelvin,toCelsius,toFahrenheit,toRankine,toDelisle,toNewton,toReaumur,toRomer]

def table(n):
    s="\n"
    for f in toFunctions:
        (temp,scale) = f(n)
        s+="{0: 8.2f} {1}\n".format(temp,scale)
    return s

fromFunctions = {'Kelvin':fromKelvin,'Celsius':fromCelsius,'Fahrenheit':fromFahrenheit, 'Rankine':fromRankine,'Delisle':fromDelisle,'Newton':fromNewton,'Reaumur':fromReaumur,'Romer':fromRomer}

def toAll(temp,scale):
    return table(fromFunctions[scale](temp))
