class BankaHesabı:

    iban_len = 26
    hesap_sayisi = []

    def __init__(self, hesap_ismi='', hesap_no='', bakiye=0):
        self.hesap_ismi = hesap_ismi
        self.__hesap_no = hesap_no
        self.__bakiye = bakiye
        BankaHesabı.hesap_sayisi.append(hesap_ismi)
        

    def para_yatır(self, yatır_miktar):
        self.__bakiye += yatır_miktar
        return self.__bakiye
        

    def para_cek(self, cek_miktar):
        self.__bakiye -= cek_miktar
        return self.__bakiye


    def bakiye_goster(self):
        return self.__bakiye
    
        
    
    @classmethod
    def hesap_sayisi_len(cls):
        return len(cls.hesap_sayisi)
    
    @staticmethod
    def check_iban(iban=''):
        if iban.startswith('TR') and len(iban) == 26:
            return True
        return False
        

    def __str__(self): # this method is used to return a string representation of the object when it is printed. It is called when you use the print() function on an instance of the class. By defining this method, you can customize how the object is displayed as a string.
        return f"BankaHesabı ({self.hesap_ismi}, {self.__hesap_no}, {self.__bakiye})"
    
test = BankaHesabı('ilker', 'TR123456789012345678901234', 500)
print(test)
test.para_yatır(100)
print(test)
BankaHesabı.hesap_sayisi_len
print(len(BankaHesabı.hesap_sayisi))
print(BankaHesabı.check_iban('TR123456789012345678901234'))

class VadesizHesap(BankaHesabı):

    def __init__(self, hesap_ismi='', hesap_no='', bakiye=0, hesap_türü=''):
        super().__init__(hesap_ismi=hesap_ismi, hesap_no=hesap_no, bakiye=bakiye)
        self.hesap_türü = hesap_türü

    def show_tyoeofaccount(self):
        return self.hesap_türü

test2 = VadesizHesap('Özgür', 'TR123456789012345678901235', 500, 'Vadesiz')
print(f'Vadesiz Hesap {test2}')
print(test2.show_tyoeofaccount())
test2.para_cek(200)
print(f'Vadesiz Hesap {test2.bakiye_goster()}')


