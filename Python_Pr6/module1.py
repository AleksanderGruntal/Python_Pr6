#Praktiline t��: S�ne ja j�rjesti funktsioonid. Video
nimekirja=[] #t�hi nimekirja
number=[1,2,3,4,5]
nimekirja2=["Abc","A","B"]
s�na="Programmerimine"
s�na_list=list(s�na)
print(s�na)
print(s�na_list)
while True:
    print("lisage loendisse t�ht")
    valik=int(input())
    if valik==1:
        a=input("sisestage t�ht")
        s�na_list.append(a)
        print(f"lisatud",s�na_list)
        print(s�na_list)
        while True:
            print("1-lisage loendisse t�ht")
            print("liita loendid\n3-lisage t�ht i -kohta")
            #--------------------------------------------
            valik=int(input())
            if valik==1:
                a=input("sisestage t�ht")
                s�na_list.append(a)
                print(f"lisas {a} uue nimekirja",s�na_list)
            elif valik==2:
                s�na_list.extend(nimekirja2)
                print(s�na_list)
            elif valik==3:
                a=input("sisestage t�ht, mida soovite lisada")
                i=int(input("sisestage positsiooni number, kuhu soovite t�he lisada"))
                s�na_list.insert(i-1,a) #0,1,2...
                print(s�na_list)
            elif valik==4:
                a=input("sisestage t�ht, mida soovite kustutada")
                n=s�na_list.count(a)
                if n>0:
                    for i in range(n):
                        s�na_list.remove(a)
                    else:
                        print("otsitav kiri on puudu")
                    print(s�na_list)
