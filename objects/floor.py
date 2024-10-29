import pygame.sprite

import assets
import configs
from layer import Layer


class Floor(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        self._layer = Layer.FLOOR
        self.image = assets.get_sprite("floor")
        self.rect = self.image.get_rect(bottomleft=(configs.SCREEN_WIDTH * index, configs.SCREEN_HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        super().__init__(*groups)

    def update(self):
        self.rect.x -= 2

        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH





# import pygame.sprite
# import assets
# import configs
# from layer import Layer

# class Floor(pygame.sprite.Sprite):
#   def __init__(self, index, *groups):
 #       self._layer = Layer.FLOOR
  #      original_image = assets.get_sprite("floor_2")
#
 #       self.image = pygame.transform.scale(original_image, (288, 300))
  #      self.rect = self.image.get_rect(bottomleft=(288 * index, configs.SCREEN_HEIGHT))
   #     self.mask = pygame.mask.from_surface(self.image)
#
 #       super().__init__(*groups)
#
 #   def update(self):
  #      self.rect.x -= 2
#
 #       if self.rect.right <= 0:
  #          self.rect.x = 288
