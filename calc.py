
# konvertē datu mērvienības
def megabit_to_megabyte(megabit):
   result = int(megabit*8)
   return result

# saskaiti degvielas patēriņu uz 100 km
def fuel_consumption(litres, kilometers):
   hundred = kilometers/100
   result = litres/hundred
   return result

# konvertē temperatūru
def celsius_to_fahrenheit(celsius):
    result = celsius * 9/5+32
    return result

# saliec visus skaitļus pirms dota skaitļa (izmanto for)
def sigma(tail):
    result = 0
    if tail!=0:
        tail=int(tail)
        for i in range(tail+1):
           result = result + i    
    else:
        result = 0
    return result

# nokonvertē svaru uz tuvāko mērvienību - grams, kilograms, tonna (izmanto if)
def weight(grams):
    if grams >= 1000000:
        result = int(grams/1000000)
        return str(result) + "t"
    elif grams >= 100000:
        result = int(grams/100000)
        return str(result) + "c"
    elif grams >= 1000:
        result = int(grams/1000)
        return str(result) + "kg"
    else:   
        return str(grams) + "g"