# This is a sample Python script.

# The Body Mass Index or BMI is calculated from weight and height.

# Asked for user info for the input.
Height = float(input("Enter your height in centimeters: "))
Weight = float(input("Enter your Weight in Kg: "))

# Calculate the height.
Height = Height/100

# Calculate the Body Mass Index/BMI.
BMI=Weight/(Height*Height)

print("your Body Mass Index is: ",BMI)

if(BMI>0):

	if(BMI<=18):
		print("you are severely underweight")

	elif(BMI<=20):
		print("you are underweight")

	elif(BMI<=30):
		print("you are Healthy")

	elif(BMI<=40):
		print("you are overweight")

	else: print("you are severely overweight")

else:("enter valid details")
