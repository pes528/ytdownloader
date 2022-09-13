#!/bin/python3
import os
import time
try:
    from pytube import YouTube
except:
    print("INSTALANDO DEPENDENCIAS...")
    os.system("pip install pytube > dev/null 2>&1")
    os.system("pip install tqdm > dev/null 2>&1")
    from pytube import YouTube
from tqdm import tqdm

#AUTHOR: @pes528



nor = "\033[1;38m"
rojito = "\033[1;31m"
fin = "\033[0m"

def d(fun):
    def dib():
        print(f"{rojito}—{fin}"*60)
        fun()
        print(f"{rojito}—{fin}"*60)
    return dib


def logo():
    print("\033[1;32m"+"__   _______   ____   _____        ___   _ _     ___    _    ____  _____ ____ \033[0m")
    print("\033[1;32m"+"\ \ / /_   _| |  _ \ / _ \ \      / / \ | | |   / _ \  / \  |  _ \| ____|  _ \ \033[0m")   
    print("\033[1;32m"+" \ V /  | |   | | | | | | \ \ /\ / /|  \| | |  | | | |/ _ \ | | | |  _| | |_) |\033[0m")
    print("\033[1;32m"+"  | |   | |   | |_| | |_| |\ V  V / | |\  | |__| |_| / ___ \| |_| | |___|  _ < \033[0m")
    print("\033[1;32m"+"  |_|   |_|   |____/ \___/  \_/\_/  |_| \_|_____\___/_/   \_\____/|_____|_| \_\ \033[0m")
    print("")
    print("\033[1;101m                                   by @pes528                                   \033[0m")
    print("                                            telegram:@pes528")
def verifica(link):
    try:
      YouTube(link).title
      return True 
    except:
      return False

def hecho():
    
    for i in tqdm(range(10)):
        time.sleep(0.5)
    print("DESCARGA REALIZADA..")
    print("ARCHIVO GUARDADO EN LA CARPETA YTdescargas/\n")
    input("PRECIONA CUALQUIER TECLA PARA VOLVER: ")
    return main()

@d
def mai():
    op = input("""
    =============================================
    1: DESCARGA NORMAL
    2: DESCARGAR MP3()
    0: SALIR
    ==============================================
    
    OPCION: """)
    if op == "1":
      descargarvideo()
    elif op == "2":
      music()
    elif op == "0":
      exit()
    else:
      print("OPCION INCORRECTA")
      main()


"""def most():
    print("="*20, "MOST QUALITY DOWNLOADER ", "="*20)
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

@d
def music():
    print("="*20, "MP3 DOWNLOADER ", "="*20)
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
          hecho()

        except:
          print("ALGO SALIO MAL")
          return main()


    else:
        print("")
        print("URL NO VALIDO ")
        return music()
@d
def descargarvideo():
    print("="*17, "STANDAR DOWNLOADER VIDEO", "="*17, "\n")
    print("Preciona 0 para volver\n")
    url = input("URL-->  ")
    if url == "0":
        main()
    try:

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

        dow=yt.streams.get_by_resolution(calidad)
        print("DESCARGANDO....")
        dow.download(output_path="YTdescargas")
        hecho()
        
    except:
        print("ALGO SALIO MAL, POSIBLES RAZONES\n-LA URL NO ES VALIDA\n-VIDEO NO DISPONIBLE PARA DESCARGA")
        return descargarvideo()




def main():
    if os.path.isdir("YTdescargas"):
      pass
    else:
      os.mkdir("YTdescargas")
    logo()
    mai()



if __name__ == "__main__":
    
    main()
    
