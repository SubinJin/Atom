import json

data = '''
{
    "name" : "Subin",
    "phone" : {
        "type" : "intl",
        "number" : "+82 5674 7829"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print("Name : ", info["name"])
print("Hide : ", info["email"]["hide"])
