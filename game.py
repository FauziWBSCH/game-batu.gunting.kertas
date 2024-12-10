import random

while True:
    print('\n',"="*10, "SELAMAT DATANG DI GAME SUIT SEDERHANA",10*"=")
    print("DI GAME INI KAMU AKAN BERMAIN SUIT (BATU/GUNTING/KERTAS) DENGAN KOMPUTER")
    user_input = input("\nMaukkan pilihan kamu (batu/gunting/kertas): ").lower()
    

    pilihan = ['batu', 'gunting', 'kertas']
    index = random.randint(0, 2)

    if user_input == 'batu' and index == 0:
        print(f'pilihan computer --{pilihan[index]}--\npilihan kamu --{user_input}--\ngame ini seri ')
    elif user_input == 'batu' and index == 1:
        print(f'pilihan computer --{pilihan[index]}--\npilihan kamu --{user_input}--\nkamu menang ')
    elif user_input == 'batu' and index == 2:
        print(f'pilihan computer --{pilihan[index]}--\npilihan kamu --{user_input}--\nkamu kalah ')
    elif user_input == 'gunting' and index == 0:
        print(f'pilihan computer --{pilihan[index]}--\npilihan kamu --{user_input}--\nkamu kalah ')
    elif user_input == 'gunting' and index == 1:
        print(f'pilihan computer --{pilihan[index]}--\npilihan kamu --{user_input}--\ngame ini seri ')
    elif user_input == 'gunting' and index == 2:
        print(f'pilihan computer --{pilihan[index]}--\npilihan kamu --{user_input}--\nkamu menang ')
    elif user_input == 'kertas' and index == 0:
        print(f'pilihan computer --{pilihan[index]}--\npilihan kamu --{user_input}--\nkamu menang ')
    elif user_input == 'kertas' and index == 1:
        print(f'pilihan computer --{pilihan[index]}--\npilihan kamu --{user_input}--\nkamu kalah ')
    elif user_input == 'kertas' and index == 2:
        print(f'pilihan computer --{pilihan[index]}--\npilihan kamu --{user_input}--\ngame ini seri ')
    elif user_input != 'batu' or 'gunting' or 'kertas':
        print('Masukkan pilihan yang benar (batu/gunting/kertas)')

    input_user = input("\napakah ingin lanjut (y/n): ").lower()
    if input_user == 'n':
        break