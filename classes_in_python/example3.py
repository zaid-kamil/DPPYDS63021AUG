class Contact:
    def __init__(self,name,phone,email="",birthday=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.birthday = birthday
    
    def show(self):
        print("Name:",self.name)
        print("Phone:",self.phone)
        print("Email:",self.email)
        print("Birthday:",self.birthday)
    
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
        print("Contact list of",self.owner)
        for c in self.contacts:
            c.show()

# use this contact book and file 5 contact

book = ContactBook("Zaid Kamil")
book.add_contact("Rajesh",9090909021)
book.add_contact("Ramesh",9090909022,"12-12-12")
book.add_contact("Suresh",9090909023,birthday="12-11-12",email ='suresh@gmail.com')

book.remove_contact("Ramesh")

book.show()
