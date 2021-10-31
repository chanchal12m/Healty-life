print("________________TO LIVE A HEALTHIER AND BETTER LIFE___________________\n")

print("----------------PLEASE SELECT ONE FROM THE THREE OPTIONS--------------------\n")

print("Select an operation to perform: ")

print("1. Health Checkup")

print("2. Healthy Food")

print("3. Exercise")



operation=int(input()) 
if operation == 1:
   print("These are some Normal Checkup\n")
   BP=int(input("Enter your Blood Pressure"))
   DB=int(input("Enter your Diabeties level"))
   CD=int(input("Enter your Cardiac level"))
   ECG=int(input("Enter your ECG"))
   Haemoglobin=int(input("Enter your Haemoglobin level"))
   if(BP>=90 and BP<=120 and DB>=70 and DB<=140 and CD>=100 and CD<=200 and ECG>=49 and ECG<=100 and
     Haemoglobin>=11 and Haemoglobin<=18 ):
      print("your Blood Pressure is Normal")
      print("Your sugar is Normal")
      print("Your Cardiac level is NOrmal")
      print("Your ECG is NOrmal")
      print("your Haemoglobin Normal")
   else:
      print("Abnormal")
      

elif operation == 2:
    print("These are some Healthy Food which you can Eat for your good  Health\n")
    print("Fruits\n") 
    print("Fruits       Protein     Carbohydrate\n")
    print("1.Apple        1g           19g     ")
    print("2.Orange      0.9g          12g   ")
    print("3.Strawberry  0.7g           8g     ")
    print("4.kewi        1.1g          15g    \n\n")
    print("Vegetable\n") 
    print("Vegetable        Protein     Carbohydrate\n")
    print("1.Spinach         2.5g           3g    ")
    print("2.Beetroot        1.6g           10g   ")
    print("3.Cauliflower     1.7g           5g     ")
    print("4.Bitter Gourd    3.1g           7g   \n\n ")

elif operation == 3:
   print("Thise are some Excercises For Maintaning Good Health\n\n")
   print("---------------------------------------------------------------------------------------------------------------------------")
   print("1.Water aerobics\n")
   print("*Aqua jogging ")
   print("*Flutter kicking")
   print("*Arm curls\n")
   print("Benefits\n")
   print(" *Water aerobics exercises improve your strength, flexibility, and balance with minimal stress on your body.\n\n")
   print("----------------------------------------------------------------------------------------------------------------------------")
   print("2.Chair yoga\n")
   print("*Overhead stretch")
   print("*Seated cow stretch")
   print("*Seated twist\n")
   print("Benefits\n")
   print(" *chair yoga has been shown to improve mental health in older  have better quality sleep, lower instances of depression, and report a general sense of well-being.\n\n")
   print("-------------------------------------------------------------------------------------------------------------------------------")
   print("3.Walking\n")
   print("Benefits\n")
   print(" *while strengthening muscles, lowering your risk of heart disease, stroke, diabetes, and colon cancer.\n\n\n")
   print("--------------------------------------------------------------------------------------------------------------------------------")
   print("4.Exercises Seniors Should Avoid\n")
   print("*Squats with dumbbells or weights")
   print("*Bench press")
   print("*Leg press")
   print("*Long-distance running")
   print("*Abdominal crunches")
   print("*Upright row")
   print("*Deadlift")
   print("*High-intensity interval training")
   print("*Rock climbing")
   print("*Power clean")
   print("-------------------------------------------------------------------------------------------------------------------------------")




   
   
   
   


