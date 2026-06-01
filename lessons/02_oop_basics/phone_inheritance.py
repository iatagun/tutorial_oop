class Phone():

    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    def dial(self):
        print(f"{self.name} is dialing...")
    
    def call(self):
        print(f"{self.name} is calling...")

    def add_number(self, name, new_number):
        self.name = name
        self.number = new_number
        return (f'New number added: {self.name} - {self.number}')
        
    

test = Phone("Annem", "1234567890")
test.call()
test.dial()
test.add_number("babam", "0987654321")
print(f'New number added: {test.name} - {test.number}')
test.dial()

class Smartphone(Phone): # inherit ederek Phone sınıfının hem attributes hem de methodslarını kullanabilmek için super() fonksiyonunu kullanıyoruz.
    
    def __init__(self, name, number, brand):
        # inherit ederek Phone sınıfının hem attributes hem de methodslarını kullanabilmek için super() fonksiyonunu kullanıyoruz.
        super().__init__(name, number)
        self.brand = brand
    
    def browse(self):
        print(f"{self.name} is browsing the internet on {self.brand} smartphone.")

print("\nTesting Smartphone class:")
iphone = Smartphone("Annem", "1234567890", "iPhone")
# inherit ederek Phone sınıfının hem attributes hem de methodslarını kullanabilmek için super() fonksiyonunu kullanıyoruz.
iphone.call()
iphone.dial()
iphone.browse()

