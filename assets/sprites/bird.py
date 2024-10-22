import pygame.sprite
import assets
import configs
from layer import Layer
from objects.column import Column
from objects.floor import Floor

class Bird(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.PLAYER

        # Đặt kích thước mong muốn của con chim
        new_width = 34  # chiều rộng mới của hình ảnh
        new_height = 24  # chiều cao mới của hình ảnh

        # Tải và thay đổi kích thước các hình ảnh của con chim
        self.images = [
            pygame.transform.scale(assets.get_sprite("redbird-upflap"), (new_width, new_height)),
            pygame.transform.scale(assets.get_sprite("redbird-midflap"), (new_width, new_height)),
            pygame.transform.scale(assets.get_sprite("redbird-downflap"), (new_width, new_height))
        ]

        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(-50, 50))

        # Lấy kích thước mới của con chim từ hình ảnh đã thay đổi kích thước
        self.width = self.rect.width
        self.height = self.rect.height

        self.mask = pygame.mask.from_surface(self.image)
        self.flap = 0

        super().__init__(*groups)

    def update(self):
        # Cập nhật hình ảnh để tạo hiệu ứng vỗ cánh
        self.images.insert(0, self.images.pop())
        self.image = self.images[0]

        # Áp dụng trọng lực
        self.flap += configs.GRAVITY
        self.rect.y += self.flap

        # Đảm bảo chim di chuyển tới vị trí chính xác
        if self.rect.x < 50:
            self.rect.x += 3

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.flap = 0
            self.flap -= 6
            assets.play_audio("wing")

    def check_collision(self, sprites):
        for sprite in sprites:
            if ((type(sprite) is Column or type(sprite) is Floor) and sprite.mask.overlap(self.mask, (
                    self.rect.x - sprite.rect.x, self.rect.y - sprite.rect.y)) or
                    self.rect.bottom < 0):
                return True
        return False
