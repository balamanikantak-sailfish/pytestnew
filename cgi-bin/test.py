import json
import cgi,cgitb
cgitb.enable()
jsondata = []	
jsonobj = {"id" : "1","name" : "mmmm","state" :"ap","cr_date" : "ssss"}
jsondata.append(jsonobj);
print("Content-type: application/json")
print()
print(json.JSONEncoder().encode(jsondata))
