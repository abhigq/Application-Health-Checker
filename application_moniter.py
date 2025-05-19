import requests
import pandas as pd

datafr=pd.read_excel(r'C:\Users\Lenovo\Documents\websites.xlsx')

for index, sites in datafr.iterrows():
    try:
        
        res=requests.get(sites["sites"], timeout=20)
        if res.status_code==200:
                datafr.at[index,"status"]= f"site is up ({res.status_code})"
        else:
                datafr.at[index,"status"]= f"site is down ({res.status_code})"
    except:
        datafr.at[index, "status"]= "site is not available"

print(datafr)
        
                
