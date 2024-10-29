# import pygame.sprite
# import assets
# import configs
# from layer import Layer
#
#
# class Background(pygame.sprite.Sprite):
#     def __init__(self, index, *groups):
#         self._layer = Layer.BACKGROUND
#         self.image = assets.get_sprite("bg")
#         self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH * index, 0))
#         super().__init__(*groups)
#
#     def update(self):
#
#         self.rect.x -= 1
#
#
#         if self.rect.right <= 0:
#             self.rect.x = configs.SCREEN_WIDTH




import pygame.sprite
import pygame.transform

import assets
import configs
from layer import Layer


class Background(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        self._layer = Layer.BACKGROUND


        self.image = assets.get_sprite("background2")


        img_width, img_height = self.image.get_size()


        scale_factor = configs.SCREEN_HEIGHT / img_height


        new_width = int(img_width * scale_factor)
        new_height = configs.SCREEN_HEIGHT


        self.image = pygame.transform.scale(self.image, (new_width, new_height))


        self.rect = self.image.get_rect(topleft=(new_width * index, 0))

        super().__init__(*groups)

    def update(self):

        self.rect.x -= 1


        if self.rect.right <= 0:
            self.rect.x = self.rect.width









# import pygame.sprite
# import assets
# import configs
# from layer import Layer
#
# class Background(pygame.sprite.Sprite):
#     def __init__(self, index, *groups):
#         self._layer = Layer.BACKGROUND
#         original_image = assets.get_sprite("back")
#
#         # Thay đổi kích thước hình ảnh
#         self.image = pygame.transform.scale(original_image, (400, 712))
#         self.rect = self.image.get_rect(topleft=(288 * index, 0))
#
#         super().__init__(*groups)
#
#     def update(self):
#         self.rect.x -= 1
#
#         if self.rect.right <= 0:
#             self.rect.x = 288
