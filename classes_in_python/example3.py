class Contact:
    def __init__(self,name,phone,email="",birthday=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.birthday = birthday
    
class ContactBook:
    contacts = []
    def __init__(self,owner):
        self.owner = owner

    def add_contact(self,name,phone,email="",birthday=""):
        contact = Contact(name,phone,email,birthday)
        self.contacts.append(contact)

    def remove_contact(self,name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)

    def show(self):
        pass

# use this contact book and file 5 contact
