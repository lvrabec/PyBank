import os
import datetime

def kreiraj_broj_racuna():
    godina=str(datetime.datetime.now().year)
    mjesec=str(datetime.datetime.now().month).zfill(2)

    broj_racuna='BA-'+ godina +'-'+ mjesec+'-00001'

    return(broj_racuna)

def kreiraj_racun():
    os.system('cls' if os.name== 'nt' else 'clear')
    print('*********************************** KREIRAJ RACUN ************************************************')
    global racun_tvrtke
    global stanje_racuna
    global transakcije
    global transakcija_id 
    print()
    racun_tvrtke['broj_racuna']= kreiraj_broj_racuna()
    racun_tvrtke['naziv_firme']= input('Unesite naziv tvrtke: \t\t\t\t')
    racun_tvrtke['adresa']= input('Unesite ulicu i broj tvrtke: \t\t\t')
    racun_tvrtke['postanski broj']= input('Unesite postanski broj sjedista tvrtke: \t')
    racun_tvrtke['sjediste']=input('Unesite grad sjedista tvrkte: \t\t\t')
    racun_tvrtke['porezni broj']=input('unesite porezni broj (OIB) : \t\t\t')
  
    while len(racun_tvrtke['porezni broj'])!=11:        
        print(' niste unjeli dovoljan broj znakova!')
        print(' OIB mora sadržavati TOČNO 11 znakova')
        print()
        racun_tvrtke['porezni broj']=input('unesite porezni broj (OIB) : \t\t\t')

        
    racun_tvrtke['odgovorna osoba']=input('unesite ime i prezime odgovorne osobe: \t\t')
    print('-------------------------------------------------------------------------')
    print(f'Generirani broj racuna tvrtke je : '+racun_tvrtke['broj_racuna'])
    print('-------------------------------------------------------------------------')
    print('Kod otvaranja računa potrebno je položiti iznos u EUR po vašoj volji.')
    print()
    prvi_polog=int(input('Molim vas unesite izos za prvi polog: \t\t'))
    while prvi_polog== 0:
            print('Nije moguće položiti 0 EUR !')
            prvi_polog=int(input('Molim vas unesite izos za prvi polog: \t\t'))
    stanje_racuna=stanje_racuna+prvi_polog
    transakcija_id=transakcija_id+1
    transakcije[transakcija_id]=f'+{prvi_polog}'

    print(f'unjeli ste prvi polog od {prvi_polog} EUR , a stanje računa je {stanje_racuna}') 


    x= input('Uspješno ste kreirali račun , pritisnite tipku ENTER za povratak u glavni izbornik. ')



def azuriraj_racun():
    os.system('cls' if os.name== 'nt' else 'clear')
    print('*********************************** PROMJENA PODATAKA ************************************************')
    print()
    global racun_tvrtke
    racun_tvrtke['naziv_firme']= input('Unesite NOVI naziv tvrtke: \t\t\t\t')
    racun_tvrtke['adresa']= input('Unesite NOVU adresu tvrtke: \t\t\t\t')
    racun_tvrtke['postanski broj']= input('Unesite NOVI postanski broj: \t\t\t\t')
    racun_tvrtke['sjediste']=input('Unesite NOVO sjediste tvrkte: \t\t\t\t')
    racun_tvrtke['porezni broj']=input('unesite NOVI porezni broj (OIB) : \t\t\t')
    while len(racun_tvrtke['porezni broj'])!=11:        
        print(' niste unjeli dovoljan broj znakova!')
        print(' OIB mora sadržavati TOČNO 11 znakova')
        print()
        racun_tvrtke['porezni broj']=input('unesite NOVI porezni broj (OIB) : \t\t\t')
    racun_tvrtke['odgovorna osoba']=input('unesite NOVU odgovornu osobu : \t\t\t\t')
    x= input('Promjena je uspjesna , pritisnite tipku ENTER za povratak u glavni izbornik. ')


def prikaz_stanja(stanje):
    os.system('cls' if os.name== 'nt' else 'clear')
    print('*********************************** STANJE NA RACUNU  **********************************************')
    print()
    print('Trenutno imate raspoloživo EUR: '+str(stanje))
    print()
    print('****************************************************************************************************')
    x= input('Pritisnite ENTER za nastavak: ')
    

def prikaz_prometa(transakcije):
    os.system('cls' if os.name== 'nt' else 'clear')
    print('*********************************** TRANASKCIJE PO RACUNU  *****************************************')
    print()
    print('Prometi po  Vašem računu ')
    for i,e in transakcije.items():
        str(print(f'Transakcija ID : {i}  Vrijednost transakcije : {e}'))
   
    print()
    print('****************************************************************************************************')
    x= input('Pritisnite ENTER za nastavak: ')

def polog_racun():
    os.system('cls' if os.name== 'nt' else 'clear')
    print('*********************************** POLOŽI NOVCE ***************************************************')
    print()
    global stanje_racuna
    global transakcije
    global transakcija_id 
    unos_pologa=int(input('Unesite polog u EUR:'))
    stanje_racuna=stanje_racuna+unos_pologa
    transakcija_id=transakcija_id+1
    transakcije[transakcija_id]=f'+{unos_pologa}'
    print()
    print('****************************************************************************************************')
    print()

    print(f'unjeli ste polog od {unos_pologa} EUR , a novo stanje računa je {stanje_racuna}') 
    x= input('Pritisnite ENTER za nastavak: ')
def podizanje_novca():
    os.system('cls' if os.name== 'nt' else 'clear')
    print('*********************************** PODIGNI NOVCE **************************************************')
    global stanje_racuna
    global transakcija_id
    global transakcije
    if (stanje_racuna!= 0):
        print('Trenutno imate raspoloživo EUR: '+str(stanje_racuna))
        podigni=int(input('Unesite iznos u EUR koji želite podići: '))
        while (podigni>stanje_racuna):
            print('Nedovoljno sredstava na računu , pokušajte ponovno !')  
            podigni=int(input('Unesite iznos u EUR koji želite podići: '))  
    else:
        pass
    stanje_racuna=stanje_racuna-podigni
    transakcija_id=transakcija_id+1
    transakcije[transakcija_id]=f'-{podigni}'
    print(f'Podigli ste {podigni} EUR , a novo stanje računa je {stanje_racuna}') 
    print()
    print()
    print('****************************************************************************************************')
    print()
    x= input('Pritisnite ENTER za nastavak: ')
def brisanje_racuna():
    os.system('cls' if os.name== 'nt' else 'clear')
    print('*********************************** BRISANJE RACUNA ************************************************')
    global racun_tvrtke
    obrisi=input('Odabrali ste BRISANJE racuna , želite li nastaviti ?  (D/N):  ')
    if (obrisi=='d' or obrisi=='D'):
        racun_tvrtke= {
                        
                        'broj_racuna':'',
                        'naziv_firme':'',
                        'adresa':'',
                        'postanski broj':'',
                        'sjediste':'',
                        'porezni broj':'',
                        'odgovorna osoba':'',
                    }
        print('Racun je uspjesno obrisan')

    elif(obrisi=='n' or obrisi=='N'):
        print('odabrali ste NE , račun ostaje u otvoren. ')
    else:
        print('Odabrali ste krivi unos !')

    print()
    print('****************************************************************************************************')
    x= input('Pritisnite ENTER za nastavak: ')
def izbornik():
    os.system('cls' if os.name== 'nt' else 'clear')
    izbor=  '''
    ***********************************************************************************
            1- Kreiranje racuna
            2- Azuriranje racuna
            3- Prikaz stanja računa
            4- Prikaz prometa po racunu
            5- Polog na račun
            6- Podizanje novca
            7- Brisanje računa

            8- Izlaz
    ***********************************************************************************
            '''


    print(izbor)





#---------------------------------------Glavni Program------------------------------ 


racun_tvrtke= {
    
    'broj_racuna':'',
    'naziv_firme':'',
    'adresa':'',
    'postanski broj':'',
    'sjediste':'',
    'porezni broj':'',
    'odgovorna osoba':'',
}

transakcije= {}
transakcija_id = 0
stanje_racuna = 0

while True:
    izbornik()
    izbor_=int(input('Odaberite opciju iz izbornika: '))
    if(izbor_ == 1 and racun_tvrtke['naziv_firme']== ''):
        kreiraj_racun()
    elif(izbor_ == 2 and racun_tvrtke['naziv_firme']!=''):
       azuriraj_racun()

    elif(izbor_ == 3 and racun_tvrtke['naziv_firme']!=''):
       prikaz_stanja(stanje_racuna)

    elif(izbor_ == 4 and racun_tvrtke['naziv_firme']!=''):
       prikaz_prometa(transakcije) 

    elif(izbor_ == 5 and racun_tvrtke['naziv_firme']!=''):
       polog_racun()

    elif(izbor_ == 6 and racun_tvrtke['naziv_firme']!=''):
       podizanje_novca()

    elif(izbor_ == 7 and racun_tvrtke['naziv_firme']!=''):
       brisanje_racuna()


    elif(izbor_ == 8 and racun_tvrtke['naziv_firme']!=''):
       break 
  
    else:
        print('-------------------------------------------------------------------------')
        print('Krivi unos jer račun  ne postoji ,  kreirajte račun!')
        print('-------------------------------------------------------------------------')
        print()
        x= input('Pritisnite ENTER za nastavak i pokušajte ponovno. ')
        
