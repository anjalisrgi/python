def convertKilometre(km):  
    conversion_ratio= 0.621371  
    miles = km * conversion_ratio  
    print ("The speed in Miles: ", miles)  
    
km = float (input ("Enter the speed in Kilometre: "))  
convertKilometre(km)
