#some information about my dog
my_son = {"name":"Hobbes",
"age":6,
"Hobbies":["running", "playing", "eating"],
 "wake up":{"Monday":6, "Tuesday":7, "Wednesday":7}}
print(f'I am {my_son["name"]} and I am {my_son["age"]} years old')
print(f'I have {len(my_son["Hobbies"])} Hobbies!')
print(f'My favorite hobby is {my_son["Hobbies"][2]}')
print(f'My dog wakes up at {my_son["wake up"]["Monday"]} am!')