import numpy as np
import sys
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#size of inner radius of donut
r2 = 2 
#width of donut
r1 = 1
#screen width in px
w = 100
#screen length in px
l = 100
'''Rotation matrices
rx = [1 0 0
      0 cos(x) -sin(x)
      0 sin(x) cos(x)]
ry = [cos(y) 0 sin(y)
      0 1 0
      -sin(y) 0 cos(y)]
rz = [cos(z) -sin(z) 0
      sin(z) cos(z)  0
      0 0 1]
'''



class Display(object):
  def __init__(self):
    self.h = 720
    self.w  = 720
    pygame.init()
    self.screen = pygame.display.set_mode((self.h, self.w))
    pygame.display.set_caption("Donut")
    self.bg_color = BLACK
    self.font = pygame.font.SysFont('Arial', 50)

  def run(self):
    while (True):
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
      self.screen.fill(self.bg_color)
      self.display_text("Donut", self.h / 2, self.w / 2)
      pygame.display.flip()

  def display_text(self, char, x, y):
    text = self.font.render(str(char), True, WHITE)
    text_rect = text.get_rect(center=(x,y))
    self.screen.blit(text, text_rect)

if __name__ == '__main__':
  d = Display()
  d.run()
