
#conversion weight in kg to pounds

#name=input("enter your name: ")
#weight=float(input("Enter weight in kg: "))    
#pound=weight * 2.20462
#print( name, "weight in pound:", pound)
########################
#pound into kg 
#name=input("Enter your name: ")
#weight_pound=float(input("Enter weight in pounds: "))
#weight_kg = weight_pound *  0.453592
#print(name, "weight in kg:", weight_kg)


#name = "m ahmad"
#print(name [::-1]   )  

#name = input("Enter student name: ")
#count = 0
#result = ""
#for char in name:
    #if char == "a":
    #         result += "e"
  #      else:
 #           result = result + char
#    else:
     #   result = result + char


#import calendar

#day = calendar.weekday(2025,9,2)
#days =["mon","tue","wed","thu","fri","sat","sun"]
#print("september 2,2025 is a" ,days[day])    
import tkinter as tk
from tkcalendar import Calendar

root = tk.Tk()
root.title("Calendar with Highlighted Date")

cal = Calendar(root, selectmode="day", year=2025, month=9, day=2)
cal.pack(pady=20)

cal.calevent_create("2025-09-10", "Special Day", "reminder")
cal.tag_config("reminder", background="red", foreground="white")

root.mainloop()


