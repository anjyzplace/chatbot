
def profile(a,b):
    if(60 <= a <= 100 and 60 <= b <= 100):
        return "Normal"
    if(101 <= a <= 200 and 101 <= b <= 200):
        return "High"  
    if(201 <= a <= 300 and 201 <= b <= 300):
        return "Very High" 
    if(301 <= a <= 400 and 301 <= b <= 400):
        return "Extremely High"         