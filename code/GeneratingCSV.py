#Generating CSV - Rows As Dictionary

import csv

users=[{'Id':'101','Name':'Vaibhav'},{'Id':'102','Name':'Rohan'},{'Id':'103','Name':'Shreyas'}]

keys=['Id','Name']

#Using writerows all data at a time

with open('result.csv','w') as f1:
    writer=csv.DictWriter(f1,fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)


