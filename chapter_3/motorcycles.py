invitees = ['amanda', 'derrick', 'kristina', 'julz']
print(invitees)
guest_one = 'julz'
invitees.remove(guest_one)
print(invitees)
print(f"\n {guest_one.title()} is unable to make it tonight")

guest_two = 'bella'
invitees.insert(3,guest_two)
print(invitees)
