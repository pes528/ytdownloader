#!/bin/python3
import os
import time
try:
    from pytube import YouTube
except:
    print("INSTALANDO DEPENDENCIAS...")
    os.system("pip install pytube > /dev/null 2>&1")
    os.system("pip install tqdm > /dev/null 2>&1")
    from pytube import YouTube
from tqdm import tqdm

nor = "\033[1;38m"
rojito = "\033[1;31m"
fin = "\033[0m"

#author @pes528

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
    """print("\033[1;32m"+"__   _______   ____   _____        ___   _ _     ___    _    ____  _____ ____ \033[0m")
    print("\033[1;32m"+"\ \ / /_   _| |  _ \ / _ \ \      / / \ | | |   / _ \  / \  |  _ \| ____|  _ \ \033[0m")   
    print("\033[1;32m"+" \ V /  | |   | | | | | | \ \ /\ / /|  \| | |  | | | |/ _ \ | | | |  _| | |_) |\033[0m")
    print("\033[1;32m"+"  | |   | |   | |_| | |_| |\ V  V / | |\  | |__| |_| / ___ \| |_| | |___|  _ < \033[0m")
    print("\033[1;32m"+"  |_|   |_|   |____/ \___/  \_/\_/  |_| \_|_____\___/_/   \_\____/|_____|_| \_\ \033[0m")
    print("")"""
    print(" \033[1;101m                by @pes528              \033[0m")
    
def verifica(link):
    try:
      YouTube(link).title
      return True 
    except:
      return False







"""def most():
    print("="*20, "MOST QUALITY DONWLOADER ", "="*20)
    url = input("URL DEL VIDEO---> ")
    
    if verifica(url) == True:
      yt = YouTube(url)
      print(yt.title)
      print(yt.streams.filter(adaptive=True))
      
      d = yt.streams.get_by_itag(137)
      d.download()
      
      

      
    else:
      print("URL NO VALIDO")
      return most()"""


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
        try:
          e=yt.streams.get_audio_only()
          print("DESCARGANDO....")
          e.download(output_path="YTdescargas", filename=titu)
          for i in tqdm(range(10)):
              time.sleep(0.5)
          print("DESCARGA REALIZADA..")
          print("ARCHIVO GUARDADO EN LA CARPETA YTdescargas/\n")
          input("PRECIONA CUALQUIER TECLA PARA VOLVER: ")
          return main()

        except:
          print("ALGO SALIO MAL")
          time.sleep(2)
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
            dow.download(output_path="YTdescargas")
            for i in tqdm(range(10)):
                time.sleep(0.5)
            print("DESCARGA REALIZADA..")
            print("ARCHIVO GUARDADO EN LA CARPETA YTdescargas/\n")
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




def main():
    os.system("clear")
    if os.path.isdir("YTdescargas"):
      pass
    else:
      os.mkdir("YTdescargas")
    logo()
    op = input("""
    ===================================
    1: DESCARGA NORMAL
    2: DESCARGAR MP3()
    0: SALIR
    ===================================
    
    OPCION: """)
    
    if op == "1":
      descargarvideo()
    elif op == "2":
      music()
    elif op == "0":
      os.system("clear")
      time.sleep(2)
      print("PARA VOLVER A INICIAR ->> python main.py")
      
      
    else:
      
      print("OPCION INCORRECTA")
      time.sleep(1)
      main()


if __name__ == "__main__":
    
    main()
    
