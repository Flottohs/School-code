import json

data = {"students":
        [         {
          "firstName":"Bart",
          "lastName":"Simpson",
          "dateOfBirth":"27/3/2001"},
     {
         "firstName":"Stewie",
         "lastName":"Griffin",
         "dateOfBirth":"13/4/2002"}
                  ]
}

file=open("ex.json", "w")
json.dump(data, file)
file.close()

json_string = json.dumps(data, indent = 2)
print(json_string)
