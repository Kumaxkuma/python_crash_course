#Amanda Moyo Aug 29, 2022

first_name = "Derrick"
last_name = "Utsey"
full_name = f"{first_name} {last_name}"
message = f"Hello {full_name.title()}, would you like to learn some Python today?"
print(message)

first_name = "Jerry"
last_name = "Springer"
full_name = f"{first_name} {last_name}"
message = f'{full_name} once said, "The audience is always right...unless they are wrong."'
print(message)

first_name = "Jerry"
last_name = "Springer"
famous_person = f"{first_name} {last_name}"
message = f'{famous_person} once said, "The audience is always right...unless they are wrong."'
print(message)

first_name =  'Jerry '
last_name = ' Springer '
full_name = f"{first_name} {last_name}"
print(f'{full_name} once said:\n\t "The audience is always right...unless they are wrong."')

first_name =  'Jerry '
last_name = ' Springer '
full_name = f"{first_name} {last_name}"
print(f'{full_name.rstrip()} once said:\n\t "The audience is always right...unless they are wrong."')

first_name =  'Jerry '
last_name = ' Springer '
full_name = f"{first_name} {last_name}"
print(f'{full_name.strip()} once said:\n\t "The audience is always right...unless they are wrong."')

first_name =  'Jerry '
last_name = ' Springer '
full_name = f"{first_name.lstrip()} {last_name.strip()}"
print(f'{full_name.strip()} once said:\n\t "The audience is always right...unless they are wrong."')
