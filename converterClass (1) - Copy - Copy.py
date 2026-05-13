class converter:
    def inches_to_feet(self,inches):
        return inches/12
    def feet_to_inches(self,feet):
        return feet*12
    def cm_to_meters(self,cm):
        return cm/100
    def meters_to_cm(self,meters):
        return meters*100
    def kg_to_grams(self,kg):
        return kg*1000
    def grams_to_kg(self,grams):
        return grams/1000
c=converter()
print("12 inches in feet:",c.inches_to_feet(12))
print("5  feet in inches:",c.feet_to_inches(5))
print("150 cm in meters:",c.cm_to_meters(150))
print("2 meters in cm:",c.meters_to_cm(2))
print("3 kg in grams:",c.kg_to_grams(3))
print("500 grams in kg:",c.grams_to_kg(500))