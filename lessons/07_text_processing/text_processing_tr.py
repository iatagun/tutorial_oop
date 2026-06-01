import string
import re

class TextProcess:

    nesne_sayisi =  0
    def __init__(self, sent, lang='Türkçe'):
        self.__ham_metin = sent          # orijinali sakla
        self.__lang = lang
        self.__temiz = self.__temizle()  # temizlenmiş hali
        TextProcess.nesne_sayisi += 1    # class variable — sadece sayaç!

    def __temizle(self):
        return "".join(
            char for char in self.__ham_metin.lower() 
            if char not in string.punctuation
        )

    def kelime_say(self):
        return len(self.__temiz.split())
    
    def kelime_list(self):
        return self.__temiz.split()

    
    def cumle_say(self):
        cumle = re.split(r'[.!?]+', self.__ham_metin.strip())
        return len([c for c in cumle if c.strip()])  # boş stringleri say

    @staticmethod
    def stopword_mu(kelime):
        stop_words = ['ve', 'ile', 'bir', 'bu', 'da', 'de', 'mi', 'mu'] # static method!
        if kelime in stop_words:
            return (f'{kelime} bir stoprword')
        
        return (f'{kelime}  bir stopword değil')
    
    def calc_len_words(self):
        words= self.__temiz.split()
        longest_word = max(words, key=len)
        return longest_word
    

    def __str__(self) -> str:
        return (f'Text Process {self.__lang}, {self.__ham_metin}, {self.__temiz}')

test = TextProcess('Bu bir denemedir. Bu da ikinci.')
print(test.kelime_list())
print('Cümle sayısı',test.cumle_say())
test2 = TextProcess('Bu bir denemedir')
test3 = TextProcess('Python öğreniyorum')

print('Nesne Sayısı ',TextProcess.nesne_sayisi)

print(TextProcess.stopword_mu('mi'))
print(test.calc_len_words())

class TurkceMetin(TextProcess):

    def __init__(self, sent, lang='Türkçe'):
        super().__init__(sent, lang='Türkçe')
        

    def find_suffix(self):

        suffix_list = ['lar', 'ler', 'da', 'de', 'ın', 'in']
        sonuclar = []
        for kelime in self.kelime_list():          # her kelime için
            for ek in suffix_list:                 # tüm ekleri dene
                if kelime.endswith(ek):            # in değil, endswith!
                    sonuclar.append(f'{kelime} → -{ek}')
                    break                          # bir kelimede bir ek yeter
        
        return sonuclar
                
        

test2 = TurkceMetin('Bunlar da hile yapıyor')
print(test2.find_suffix())