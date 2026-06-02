class MetinIsleme:

    def __init__(self, text='', kelime='', buyuk_harf=False, tekrar=3):
        self.text = text
        self.kelime = kelime
        self.buyuk_harf = buyuk_harf
        self.tekrar = tekrar

    def buyuk_yap(self):
        if self.buyuk_harf==True:
            return self.text.upper()
        return self.text
    
    def yazdir_tekrar(self):
        return self.kelime*self.tekrar

    
    def __str__(self) -> str:
        return (f'Metin işleme: {self.text}, {self.kelime}')
    

test = MetinIsleme('Bu bir deneme', 'deneme ', buyuk_harf=True)
print(test.buyuk_yap())
print(test.yazdir_tekrar())

kelimeler = ['linguistik', 'dil', 'morfoloji', 'ses', 'sözdizimi', 'anlambilim']

def make_upper(kelime):
    return kelime.upper()

def make_lower(kelime):
    return kelime.lower()


def set_min_len(x):
    return len(x) >= 5

print(list(map(make_upper, kelimeler)))
result = []
for i in list(filter(set_min_len, kelimeler)):
    result.append(make_upper(i))
    
print(result)

make_upper_lambda = lambda kelime: kelime.upper()
set_min_len_lambda = lambda x: len(x) >= 5


