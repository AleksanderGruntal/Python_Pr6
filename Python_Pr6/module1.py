#Praktiline töö: Sõne ja järjesti funktsioonid. Video
nimekirja=[] #tühi nimekirja
number=[1,2,3,4,5]
nimekirja2=["Abc","A","B"]
sõna="Programmerimine"
sõna_list=list(sõna)
print(sõna)
print(sõna_list)
while True:
    print("lisage loendisse täht")
    valik=int(input())
    if valik==1:
        a=input("sisestage täht")
        sõna_list.append(a)
        print(f"lisatud",sõna_list)
        print(sõna_list)
        while True:
            print("1-lisage loendisse täht")
            print("liita loendid\n3-lisage täht i -kohta")
            #--------------------------------------------
            valik=int(input())
            if valik==1:
                a=input("sisestage täht")
                sõna_list.append(a)
                print(f"lisas {a} uue nimekirja",sõna_list)
            elif valik==2:
                sõna_list.extend(nimekirja2)
                print(sõna_list)
            elif valik==3:
                a=input("sisestage täht, mida soovite lisada")
                i=int(input("sisestage positsiooni number, kuhu soovite tähe lisada"))
                sõna_list.insert(i-1,a) #0,1,2...
                print(sõna_list)
            elif valik==4:
                a=input("sisestage täht, mida soovite kustutada")
                n=sõna_list.count(a)
                if n>0:
                    for i in range(n):
                        sõna_list.remove(a)
                    else:
                        print("otsitav kiri on puudu")
                    print(sõna_list)
