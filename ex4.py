name = "Strangelove"
age = 28
height = 71 #inches
height_in_cm = height * 2.54    #cms
weight = 180 #lbs
weight_in_kg = weight * 0.45359237
eyes = "black"
teeth = "white"
hair = "black"

print("Let's talk about %s." % name)
print("He's %d inches tall (%d cm)." % (height, height_in_cm) )
print("He's %d pounds heavy (%d Kg)." % (weight, weight_in_kg) )
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %r depending on the coffee." % teeth)

print("If I add %d, %d and %d I get %d." % (age, height, weight, age + height + weight))