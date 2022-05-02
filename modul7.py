from faker import Faker
fake = Faker("pl_PL")

class Business_card:
    def __init__(self, first_name, last_name, company, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.email = email
        self.phone_number = phone_number
        
        # Variables
        #self.label_length = first_name + last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.company} {self.email} {self.phone_number}'
    #def __repr__(self):
        #return f"Business_card(first_name={self.first_name} last_name={self.last_name} company={self.company} email={self.email} phone={self.phone_number})"
    def contact(self):
        return print(f'Kontaktuj się z:{self.first_name} {self.last_name} {self.company} {self.email} {self.phone_number}')
    @property
    def label_length(self):
        return sum([len(self.first_name),len(self.last_name)+1])


#bcard = Business_card(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), email=fake.email(), phone_number=fake.phone_number())
bcard = Business_card(first_name = "Wojtek", last_name = "Cejrowski", company = "Boso przez Świat", email = "cejrowski@gmail.com", phone_number = '666-666-666')
print(bcard)
bcard.contact()
cards=[]

for i in range(10):
    bc = Business_card(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), email=fake.email(), phone_number=fake.phone_number())
    #bc = (f'{fake.first_name} {fake.last_name} {fake.company} {fake.email}')
    cards.append(bc)


print(cards)
"""by_last_name = sorted(cards, key=lambda bcard: bcard.last_name)
print("By last name")
print(by_last_name)
by_first_name = sorted(cards, key=lambda bcard: bcard.first_name)
print("By first name")
print(by_first_name)
by_email = sorted(cards, key=lambda bcard: bcard.email)
print("By email")
print(by_email)"""

