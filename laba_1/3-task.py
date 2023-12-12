# Задача 3
phones_list = ['0-351-00-00', '0-351-00-01', '0-351-00-02', '0-351-00-03']
names_list = ['Ivan', 'Kate', 'Sergey', 'Fox']
print("Hello!")
str_name = input("Write name: ")

if str_name in names_list:
    index = names_list.index(str_name)
    print(str_name, "phone is", phones_list[index])
else:
    print("User not found")

# Рефакторінг
users_list = [
    {
        "name": "Ivan",
        "phone": "0-351-00-00"
    },
    {
        "name": "Kate",
        "phone": "0-351-00-01"
    },
    {
        "name": "Sergey",
        "phone": "0-351-00-02"
    },
    {
        "name": "Fox",
        "phone": "0-351-00-03"
    }
]

search_contact = input("Write name: ")

found_contact = None

for contact in users_list:
    if contact["name"] == search_contact:
        found_contact = contact
        break
    
if found_contact:
    print(f"{found_contact['name']} phone is {found_contact['phone']}")
else:
    print("User not found")