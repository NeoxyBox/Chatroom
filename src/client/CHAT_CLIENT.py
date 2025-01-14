import os
import sys
import time
import logging
import socket
from . import chatbase

chatbase.

print(Fore.RED + "Bu uygulama loglama sistemine sahiptir lütfen saygı çerçevesinde ve kibarca konuşmaya dikkat edin !")
time.sleep(2)
print("Araç başlatılıyor...")
time.sleep(2)
print("""         ________  ______   ________    ___________   ________ ®
        /  _/ __ \/ ____/  / ____/ /   /  _/ ____/ | / /_  __/
        / // /_/ / /      / /   / /    / // __/ /  |/ / / /   
      _/ // _, _/ /___   / /___/ /____/ // /___/ /|  / / /    
     /___/_/ |_|\____/   \____/_____/___/_____/_/ |_/ /_/
         by @Kerxunos                                         v2.65(Beta) """)
time.sleep(2)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(f"[*] IP Adresiniz: {ip}")
logging.info(f"Client IP: {ip}")
print(Fore.GREEN + "[*] Fiziksel soket oluşturuldu !")
time.sleep(2)
print(Fore.YELLOW + "[!] Lütfen İstemci IP Adresi ve Port numarasını doğru girdiğinizden emin olun !")
time.sleep(0.75)
print("[*] Lütfen herhangi bir hatayı github sayfama raporlayın")
time.sleep(2)
host = str(input("Server IP: "))
port = int(input("Server Port: "))
print(f"[*] Host: {host} Port: {port}")
logging.info(f"Host: {host} Port: {port}")
time.sleep(1)
print("Server'a bağlanmaya çalışıyoruz...")
s.connect((host, port))

print(Fore.GREEN + "Server'a bağlanıldı !")
uname = input("Kullanıcı adı giriniz: ")
logging.info(f"Client Username: {uname}")
print("Serverin kullanıcı adı bekleniyor...")
uname1 = uname.encode()
s.send(uname1)
ser_uname = s.recv(1024)
ser_uname = ser_uname.decode()
print(f"Server kullanıcı adı: {ser_uname}")
logging.info(f"Server Username: {ser_uname}")
time.sleep(2)
while True:
    try:
        print(f"Server({ser_uname}) yazıyor...")
        ser_msg = s.recv(1024)
        ser_msg = ser_msg.decode()
        if ser_msg == "/kick":
            print("Server tarafından kicklendiniz")
            time.sleep(2)
            sys.exit(0)
        if ser_msg == "/shutdown":
            print("server bağlantıyı sonlandırdı")
            time.sleep(1)
            s.close()
            sys.exit(0)
        if ser_msg == "/client_ip":
            ip1 = ip.encode()
            s.send(ip1)
        if ser_msg == "/clear":
            os.system("cls")
        print(f"{ser_uname}: {ser_msg}")
        logging.info(f"{ser_uname}: {ser_msg}")
        msg = input(f"{uname}--> ")
        print(f"{uname}: {msg}")
        logging.info(f"{uname}: {msg}")
        msg1 = msg.encode()
        s.send(msg1)
    except KeyboardInterrupt as e:
        print("Bizi tercih ettiğiniz için teşekkürler !")
        sys.exit(0)
