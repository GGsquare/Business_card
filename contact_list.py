from multiprocessing.dummy import JoinableQueue
from faker import Faker
import faker
fake = Faker("pl_PL")
c = []
class BaseContact:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
    def __str__(self):
        return f'Drukuj:{self.first_name} {self.last_name} {self.email} {self.phone_number}'
    def __repr__(self):
        return f"BaseContact(first_name={self.first_name} last_name={self.last_name} email={self.email} phone={self.phone_number})"
    def contact(self):
        return print(f'Wybieram numer:{self.phone_number} i dzwonie do:{self.first_name} {self.last_name}')
    def create_contacts(self, int):
           for i in range(int):
            card = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email(), phone_number=fake.phone_number())
            c.append(card)
    @property
    def label_length(self):
        return sum([len(self.first_name),len(self.last_name)+1])

class BusinessContact(BaseContact):
    def __init__(self, job, company, company_phone_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.company_phone_number = company_phone_number
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.phone_number} {self.job} {self.company} Company phone:{self.company_phone_number}'
    def __repr__(self):
        return f"BusinessContact(first_name={self.first_name} last_name={self.last_name} email={self.email} phone={self.phone_number} job={self.job} company={self.company} company_phone_number={self.phone_number})"
    def contact(self):
        return print(f'Wybieram numer:{self.company_phone_number} i dzwonie do:{self.first_name} {self.last_name}')
    def create_contacts(self, int):
        for i in range(int):
            bcard = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email(), phone_number=fake.phone_number(), job = fake.job(), company = fake.company(), company_phone_number = fake.phone_number())
            c.append(bcard)

card = BaseContact(first_name = "Wojtek", last_name = "Cejrowski", email = "cejrowski@gmail.com", phone_number = '666-666-666')
print(card)
bcard = BusinessContact(first_name = "Olo", last_name = "Barczak", email = "olo@wp.pl", phone_number = "+48 123456789", job = "HSE", company = "SIEMENS", company_phone_number = "+48 987654321")
print(bcard)
bcard.contact()
card.contact()
card.create_contacts(1)
print("test jak drukuje wizytówki prywatne")
print(c)
bcard.create_contacts(5)
print("test jak drukuje wizytówki służbowe")
print(c)