import pyautogui as bot
import cv2
import numpy as np
from Controller import PressKey, ReleaseKey, Z, A
from time import sleep
import traceback

def capture_sprite_region():
    screenshot = bot.screenshot()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)


def detect_shiny(normal_image_paths):

    try:
        positions = [bot.locateOnScreen(image_path, confidence=0.8) for image_path in normal_image_paths]
        
        if any(positions):
            print('Pokémon normal detectado!')
            return False
        else:
            print('Pokémon shiny detectado!')
            return True

    except bot.ImageNotFoundException:
        print('Imagem não encontrada na tela.')
        return True


def main():

    normal_image_paths = ['treecko1.png', 'treecko2.png']

    try:
        sleep(5)
        while True:

            for n in range(5):
                PressKey(Z)
                sleep(1)
                ReleaseKey(Z)
                sleep(1)
            PressKey(A)
            sleep(1)
            ReleaseKey(A)
            sleep(3)

            for _ in range(2):
                PressKey(Z)
                sleep(1)
                ReleaseKey(Z)
                sleep(1)
            sleep(7)
            PressKey(Z)
            sleep(1)
            ReleaseKey(Z)
            sleep(5)

            if detect_shiny(normal_image_paths):
                print('Pokémon shiny detectado!')
                return
            
            else:
                print('Não é shiny. Continuando...')
                sleep(1)
                bot.click(x=79, y=29)
                sleep(1)
                bot.click(x=130, y=314)
                sleep(5)

    except Exception as e:
        print('Detalhes adicionais sobre o erro:')
        traceback.print_exc()


if __name__ == '__main__':
    main()
