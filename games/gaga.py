import random
import main

def start():
    while True:
        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 4  #INI GOA YANG HARUS KOSONG
        goa = goa_kosong.copy() #INI ADALAH TEMPAT BARU UNTUK SI GAGA
        gaga_position = random.randint(1, 4)
        goa[gaga_position - 1] = "|0_0|"

        goa_kosong =' '.join(goa_kosong)
        goa =' '.join(goa)


        
        print(f'Halo coba perhatikan goa dibawah ini\n\n{goa_kosong}\n') 
        pilihan_user = int(input("menurut kamu dimana gaga berada? [1 / 2 / 3 / 4] "))    
                
        if pilihan_user == gaga_position:
            print(f"\n{goa}\n\nSELAMAT KAMU MENANG!")
        else:
            print(f"\n{goa}\n\nMAAF KAMU KALAH GAGA ADA DI NOMOR {gaga_position}!")
        
        play_again = input("\n\napakah kamu yakin ingin melanjutkan game [Y/N]: ")
        if play_again == "N":
            main.menu()

if __name__ == '__main__':
    start()