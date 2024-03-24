import os
from colorama import Fore
from gtts import gTTS
from playsound import playsound

PATH_AUDIO = 'audio.mp3'
PATH_FILE = 'data.txt'


def opcion(label):
    value = input(Fore.YELLOW + label)
    if value.lower() == 'y':
        return True

    if value.lower() == 'n':
        return False

    print(Fore.RED + 'Valor invalido')
    return opcion(label)


def read_file():
    input(Fore.YELLOW + 'Guarde su mensaje en el archivo data.txt. Presione ENTER para continuar...')

    if not os.path.isfile(PATH_FILE):
        print(Fore.RED + 'No existe el archivo data.txt')
        return read_file()

    try:
        with open(PATH_FILE, 'r') as file:
            content = file.read()
            if len(content) <= 0:
                print(Fore.RED + 'El archivo esta vacío')
                return read_file()
            else:
                return content
    except:
        print(Fore.RED + 'Hubo un problema al leer el archivo')
        return read_file()


def main():
    os.system('clear')

    try:
        print(Fore.CYAN + 'Bienvenido, esta aplicación te permite pasar de texto a voz')

        text = read_file()
        try:
            audio = gTTS(text, lang="es")
            audio.save(PATH_AUDIO)

            play = opcion('Deseas reproducir el audio? y/n: ' + Fore.WHITE)

            if play:
                playsound(PATH_AUDIO)

            print(Fore.CYAN + "El archivo de audio fue guardado en la raiz del proyecto")
        except:
            print(
                Fore.RED + 'Hubo un problema al crear el audio, porfavor revise su conexión a internet')

    except KeyboardInterrupt:
        print(Fore.CYAN + "\nAdios ...")


if __name__ == "__main__":
    main()
