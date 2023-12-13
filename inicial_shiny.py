import pyautogui as bot
import cv2

normal_sprite = cv2.imread('treecko_n.png')
shiny_sprite = cv2.imread('treecko_s.png')

print(normal_sprite.shape)
print(shiny_sprite.shape)
cv2.imshow('Normal Sprite', normal_sprite)
cv2.imshow('Shiny Sprite', shiny_sprite)
cv2.waitKey(0)
cv2.destroyAllWindows()
