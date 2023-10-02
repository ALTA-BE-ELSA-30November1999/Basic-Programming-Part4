Abjad =['A','B','C','D','E',
        'F','G','H','I','J',
        'K','L','M','N','O',
        'P','Q','R','S','T',
        'U','V','W','X','Y','Z']

def ubah_huruf(sentence):
    pattern = ""
    geserKe = 10
    
    for a in range (len(sentence)): 
        if sentence[a] in Abjad :
            Hasil_akhir = Abjad.index(sentence[a]) + geserKe #Index ke - a + 10 
        # print(Hasil_akhir)
            pattern += Abjad[ Hasil_akhir % 26] # Untuk mengambil indeks yang sudah digeser
        else :
            pattern += " "
    for b in pattern :
        return pattern

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB