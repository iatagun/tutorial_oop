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