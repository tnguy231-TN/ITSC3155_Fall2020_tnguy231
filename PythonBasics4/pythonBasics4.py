# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# # Part A.

def array_2_dict(emails, contacts):
    if len(emails) == 0 or not any(emails):
        for x in contacts:
            contacts[x] = ""
    else:
        for x in range(len(emails)):  # type: int
            contacts[list(contacts)[x]] = emails[x]
    return contacts


# # Part B.
def array2d_2_dict(contact_info, contacts):
    if len(contact_info) == 0 or not any(contact_info):
        for x in contacts:
            contacts[x] = ""
    else:
        for x in range(len(contact_info)):
            innerContact = {"email": contact_info[x][0], "phone": contact_info[x][1]}
            contacts[list(contacts)[x]] = innerContact
    return contacts


# # Part C.
def dict_2_array(contacts):
    if len(contacts) == 0:
        arr = [[], [], []]
    else:
        emails = []
        phone = []
        name = []
        for key, value in contacts.items():
            name.append(key)
            emails.append(contacts[key]["email"])
            phone.append(contacts[key]["phone"])
        # merge 3 single arrays into 3D array
        arr = [emails, phone, name]
    return arr
