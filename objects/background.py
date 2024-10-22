import pygame.sprite
import assets
import configs
from layer import Layer

class Background(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        self._layer = Layer.BACKGROUND
        original_image = assets.get_sprite("back")

        # Thay đổi kích thước hình ảnh
        self.image = pygame.transform.scale(original_image, (400, 712))
        self.rect = self.image.get_rect(topleft=(288 * index, 0))

        super().__init__(*groups)

    def update(self):
        self.rect.x -= 1

        if self.rect.right <= 0:
            self.rect.x = 288
