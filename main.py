import os
while True:
    print("""
 _                   _____           _              __  
| |                 |_   _|         | |            /  | 
| |     __ _ _____   _| | ___   ___ | |___  __   __`| | 
| |    / _` |_  / | | | |/ _ \ / _ \| / __| \ \ / / | | 
| |___| (_| |/ /| |_| | | (_) | (_) | \__ \  \ V / _| |_
\_____/\__,_/___|\__, \_/\___/ \___/|_|___/   \_/  \___/
                  __/ | Author : Agil             
                 |___/                                  
    
    """)
    print("Pilih:")
    print("1. SQL Injection")
    print("2. XSS")
    print("3. Keluar")
    pilihan = input("Pilih: ")

    if pilihan == '1':
        os.system("python sqlinjection.cpython-311.pyc")
    elif pilihan == '2':
        os.system("python xss.cpython-311.pyc")
    elif pilihan == '3':
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
