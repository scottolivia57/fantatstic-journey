#Name: Olivia Scott, Ebun Obisesan, and Kairal Johnson
#email: scottom, obiseseo, johns7kj (@mail.uc.edu)
#Assignment Title: Assignment 10
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: API
#Citations: Professor Nicholson
#Anything else that's relevant:

#main.py

import json5
import requests
from apiPackage.API import *

#AIP Link
response = requests.get('https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=id,school.name,2013.student.size&api_key=cvvxPX2Qp02bYBUmNzXXyN2HKfDBnajvI66GeFYn')
json_string = response.content
  
#Printing the data 
parsed_json = json5.loads(json_string) # Now we have a python dictionary
iterate_dictionary(parsed_json)
print(parsed_json) 

#print(parsed_json5['data'][0]['description'])
