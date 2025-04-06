#TempConvert.py
#Name:ANTONIO PEREZ
#Date: APRIL 6
#Assignment:LAB 3


def main():
  tempF = float(input("enter temp in farenheit: "))
  tempC = (tempF - 32) * 5/9
  
  print(tempF, "is ", tempC, "degrees celsius.")
  
if __name__ == '__main__':
  main()
  
  
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.