gewicht = float(input("Gewicht in kilogram: "))
lengte = float(input("Lengte in meter: "))
bmi = gewicht / lengte ** 2
if (bmi >= 18.5 and bmi <= 25):
    print("OK")
