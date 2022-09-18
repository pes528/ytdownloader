#!/bin/python3
import os, json
import time
try:
    import requests
    from pytube import YouTube
except:
    print("INSTALANDO DEPENDENCIAS...")
    os.system("pip install pytube > /dev/null 2>&1")
    os.system("pip install tqdm > /dev/null 2>&1")
    os.system("pip install requests > /dev/null 2>&1")
    from pytube import YouTube
    import requests
from tqdm import tqdm

#AUTHOR: 


verde = "\033[1;102m"
barrita = "\033[1;101m"
nor = "\033[1;38m"
rojito = "\033[1;31m"
fin = "\033[0m"
rutaTermux = "/data/data/com.termux/files/home/storage/downloads/"



class bot:
    cancion = ""
    nombre=""
    url = ""
    token = ""
    id = ""
    info = {}
    def verifica(self, token):
        url = f"https://api.telegram.org/bot{token}/getMe"
        resp = requests.get(url).json() 
        if resp["ok"] == True:
            self.url = f"https://api.telegram.org/bot{token}/sendMessage"
            self.token = token
            return True
        else:
            
            return False
    def message(self, id):
        data = {"chat_id":int(id), "text":"BOT CONFIGURADO CON EXITO"}
        resp = requests.get(self.url, data=data).json()

        if resp["ok"] == True:
            self.id = int(id)
            self.nombre = resp["result"]["from"]["first_name"]
            self.info = resp
            return True
        else:
            return False


    def save(self, data):
        with open("bot.json", "w") as f:
            json.dump(data, f)

    def activo(self):
        try:

            with open("bot.json", "r") as f:
                resp = json.load(f)
                if resp["activo"] == True:
                    return True
                else:
                    return False 
        except:
            return ("None")
    def showStatus(self):
        with open("bot.json", "r") as f:
            resp = json.load(f)  
            if resp["activo"] == True:
                return (f"{verde}ON{fin}")
            else:
                return (f"{barrita}OFF{fin}")

    def sendfile(self, namefile):
        
        with open("bot.json", "r") as f:
            resp = json.load(f)
        tok = resp["token"]
        url = f"https://api.telegram.org/bot{tok}/sendAudio"
        if leerRuta() == True:
            pay = {"chat_id":resp["userId"]}
            music = {"audio": open(f"YTdescargas/{namefile}", "rb")}
            
            body = requests.get(url, data=pay, files=music).json()
            if body["ok"] == False:
                
                return (body["description"])
            else:
                os.remove(f"YTdescargas/{namefile}")
                return True
        elif leerRuta() == False:
            pay = {"chat_id":resp["userId"]}
            music = {"audio": open(f"{rutaTermux}{namefile}", "rb")}
            
            body = requests.get(url, data=pay, files=music).json()
            if body["ok"] == False:
                
                return (body["description"])
            else:
                os.remove(f"{rutaTermux}{namefile}")
                return True

    def nameFormat(self, name):
        letras = """" "|\)($%¬#·?¿¡'}{+`-_,;:<> """
        for i in letras:
            nam = name.replace(i, "")
        
        return (nam)
           
botsito = bot()




def rutaoficial():
    
    if botsito.activo() == "None" or botsito.activo() == False:
        if leerRuta() == True:
            return ("/YTdescargas")
        else:
            return (rutaTermux)
    else:
        with open("bot.json", "r") as f:
            resp = json.load(f)
        bot = resp["bot"]["result"]["from"]["first_name"]
        return (f"BOT TELEGRAM                   {bot}")
def showRute():
    if leerRuta() == True:
        return ("/YTdescargas/")
    else:
        return (rutaTermux)
    


def d(fun):
    def dib():
        print(f"{rojito}—{fin}"*42)
        fun()
        print(f"{rojito}—{fin}"*42)
    return dib






def logo():
    print(f"""
 ██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗
 ██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║
 ██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║
 ██║░░██║██║░░██║░░████╔═████║░██║╚████║
 ██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║
 ╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝""")
    
    print(" \033[1;101m                by @pes528              \033[0m")
    
def verifica(link):
    try:
      YouTube(link).title
      return True 
    except:
      return False





def music():
    print(f"{rojito}—{fin}"*42)
    print(" ", "="*11, "MP3 DOWNLOADER ", "="*11)
    print("Preciona 0 para volver")
    url = input("URL-->  ")
    if url == "0":
      return main()
    elif verifica(url) == True:

        yt = YouTube(url)
        print(yt.title)
        titu = yt.title+".mp3"
        e=yt.streams.get_audio_only()
        print("DESCARGANDO....")
        try:
          
          if leerRuta() == True:
              if botsito.activo() == True:
                  nombre=botsito.nameFormat(titu)
                  e.download(output_path="YTdescargas", filename=nombre)
              else:

                  e.download(output_path="YTdescargas", filename=titu)
          else:
              if botsito.activo() == True:
                  nombre=botsito.nameFormat(titu)
                  e.download(output_path=rutaTermux, filename=nombre)
              else:
                  e.download(output_path=rutaTermux, filename=titu)
        except ValueError:
          print("ALGO SALIO MAL")
          time.sleep(2)
          return main()
        for i in tqdm(range(10)):
            time.sleep(0.5)
                    
        print("DESCARGA REALIZADA..")
        if botsito.activo() == True:
            print("INTENTANDO ENVIAR EL ARCHIVO A TELEGRAM...")
            time.sleep(1)
            nameOficial = botsito.nameFormat(titu)
            if botsito.sendfile(nameOficial) == True:
                print("ARCHIVO ENVIADO ")
                time.sleep(1)
                input("PRECIONA CUALQUIER TECLA PARA VOLVER: ")
                return main()
            else:
                print("ERROR")
                print(botsito.sendfile(titu))
                time.sleep(2)
                main()
            
        else:
            print(f"ARCHIVO GUARDADO -->> {rutaoficial()}\n")

        

            input("PRECIONA CUALQUIER TECLA PARA VOLVER: ")
            return main()

    else:
        print("")
        print("URL NO VALIDO ")
        return music()

def descargarvideo():
    print(f"{rojito}—{fin}"*42)
    print("="*8, "STANDAR DOWNLOADER VIDEO", "="*8, "\n")
    print("Preciona 0 para volver\n")
    url = input("URL-->  ")
    if url == "0":
        main()
    elif verifica(url) == True:


        yt = YouTube(url)

        calid = yt.streams.filter(progressive=True, file_extension="mp4")
        print("CALIDAD DISPONIBLE")
        quality = []
        for i in calid:
          quality.append(i.resolution)
          print(i.resolution)
        #calidad = input("ESCRIBE LA CALIDAD A DESCARGAR EJEMPLO(720p): ")
        while True:
          
          calidad = input("ESCRIBE LA CALIDAD A DESCARGAR EJEMPLO(720p): ")
          if len(calidad) == 4 and calidad in quality:
            break
          else:
            print(f"CALIDAD INCORRECTA  --> [{calidad}]\n")
            print("CALIDAD DISPONIBLE: ")
            for i in quality:
              print(i)
        try:

            dow=yt.streams.get_by_resolution(calidad)
            print("DESCARGANDO....")
            if leerRuta() == True:

                dow.download(output_path="YTdescargas")
                
            else:
                dow.download(output_path=rutaTermux)
            for i in tqdm(range(10)):
                time.sleep(0.5)
            print("DESCARGA REALIZADA..")
            print(f"ARCHIVO GUARDADO --->> {rutaoficial()}\n")
            input("PRECIONA CUALQUIER TECLA PARA VOLVER: ")
        
            return main()
        
        except:
            print("NO SE PUDO REALIZAR LA DESCARGA")
            time.sleep(1)
            return main()
    else:
      print("ENLACE NO VALIDO")
      time.sleep(1)
      descargarvideo()


def escribirRuta(op):
    data = {"Default": op}
    with open("config.json", "w") as f:
        json.dump(data, f)

def leerRuta():
    with open("config.json", "r") as f:
        dat = json.load(f)
        return dat["Default"]


def ruta():
    os.system("clear")
    print(f"{rojito}—{fin}"*42)
    print(" ", "="*7, "CAMBIAR RUTA DE ALMACENAMIENTO ", "="*7, "\n")
    print("")
    op = input("""
    RUTA DE DESCARGAS POR DEFECTO [/YTdescargas/]
    ===========================================

    1-> MANTENER RUTA POR DEFECTO
    2-> CAMBIAR RUTA [almacenamiento interno]
    0-> VOLVER

    ===========================================
    OPCION--> """)
    if op == "1":
        escribirRuta(True)
        print("RUTA POR DEFECTO [True]")
        time.sleep(1)
        main()
    elif op == "2":
        print("RECUERDA QUE DEBES TENER\nACCESO AL ALMACENAMENTO INTERNO")
        time.sleep(2)
        escribirRuta(False)
        print("RUTA CAMBIADA CON EXITO")
        time.sleep(2)
        main()
    elif op == "0":
        main()
    else:
        print("OPCION INCORRECTA")
        time.sleep()
        ruta()



def botTelegram():
    data={}
    os.system("clear")
    print(f"{rojito}—{fin}"*42)
    print("PARA CONFIGURAR TU BOT NECESITAS ESTOS DATOS:\n-> TOKEN DE TU BOT\n--> TU ID DE USUARIO")
    op = input("""
    1> Continuar
    0> Salir
    OPCION-->  """)
    if op == "1":
        token = input("TOKEN DE TU BOT ->> ")
        id = input("COPIA TU ID-->  ")
        print("VERIFICANDO...")
        if botsito.verifica(token) == True and botsito.message(id) == True:
            print(f"BOT ENCONTRADO ->>> nombre: {botsito.nombre}")
            data["activo"]=False
            data["userId"]=botsito.id
            data["token"]=botsito.token
            data["bot"]=botsito.info
            
            
            botsito.save(data)
            print("BOT CONFIGURADO CON EXITO")
            print("YA PUEDES ACTIVAR EL BOT")
            time.sleep(2)
            main()
        else:
            print("TOKEN O ID INCORRECTOS, VERIFICA LOS DATOS")
            time.sleep(2)
            main()

    elif op == "0":
        main()
    else:
      print("OPCION INCORRECTA")
      time.sleep(1)
      botTelegram()

def activarBot():
    os.system("clear")
    print(f"{rojito}—{fin}"*42)
    print(f"RECUERDA SI EL BOT ESTA ACTIVO [ON]\nLAS DESCARGAS IRAN A TU TELEGRAM\nNO SE ALMACENARA NADA EN LA MEMORIA\n{rojito}FUNCION SOLO DISPONIBLE PARA DESCARGAS MP3{fin}")
    time.sleep(5)        
    print(">>CAMBIANDO ESTADO DEL BOT....")
    time.sleep(3)
    with open("bot.json", "r") as f:
        resp = json.load(f)
        if resp["activo"] == True:
            resp["activo"]=False
            botsito.save(resp)
        else:
            resp["activo"]=True
            botsito.save(resp)
    print("STATUS DEL BOT CAMBIADO CON EXITO")
    time.sleep(2)
    main()

def main():
    os.system("clear")
    if os.path.isdir("YTdescargas"):
      pass
    else:
      os.mkdir("YTdescargas")
    logo()
    
    print(f"RUTA:{rojito}{rutaoficial()}{fin}")
    if os.path.isfile("bot.json") and botsito.activo() != "None":
        print(f"""
      ===================================
      1: DESCARGA NORMAL
      2: DESCARGAR MP3()
      3: CAMBIAR RUTA DE ALMACENAMIENTO
      4: CONFIGURAR BOT (TELEGRAM)
      5: ACTIVAR/DESACTIVAR BOT [{botsito.showStatus()}] 
      0: SALIR
      ===================================
        """)
        op = input("OPCION: ")
    
        if op == "1":
            descargarvideo()
        elif op == "2":
            music()
        elif op == "3":
            ruta()

        elif op == "4":
            botTelegram()
        elif op == "5":
            activarBot()
        elif op == "0":
            os.system("clear")
            time.sleep(2)
            print("PARA VOLVER A INICIAR ->> python main.py")
      
      
        else:
      
            print("OPCION INCORRECTA")
            time.sleep(1)
            main()
    else:

      op = input("""
      ===================================
      1: DESCARGA NORMAL
      2: DESCARGAR MP3()
      3: CAMBIAR RUTA DE ALMACENAMIENTO
      4: CONFIGURAR BOT (TELEGRAM) 
      0: SALIR
      ===================================
    
      OPCION: """)
    
      if op == "1":
        descargarvideo()
      elif op == "2":
        music()
      elif op == "3":
        ruta()

      elif op == "4":
        botTelegram()
      elif op == "0":
        os.system("clear")
        time.sleep(2)
        print("PARA VOLVER A INICIAR ->> python main.py")
      
      
      else:
      
        print("OPCION INCORRECTA")
        time.sleep(1)
        main()


if __name__ == "__main__":
    if os.path.isfile("config.json"):
        pass
    else:
        escribirRuta(True)
    main()
    
