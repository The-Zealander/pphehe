import pygame
import time
import defines
from Animations import PlayerAnimation
from player_mods import HealthModule
from defines import player_size, player_speed

# Define different movement directions
class Direction:
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, player_size, player_size)

        # Animation setup for different directions
        self.animations = {
            "down": PlayerAnimation(["Goblin_sprites_walking/goblin_walk_down_{}.png".format(i) for i in range(1, 7)],
                                    0.09),
            "up": PlayerAnimation(["Goblin_sprites_walking/goblin_walk_up_{}.png".format(i) for i in range(1, 7)], 0.09),
            "left": PlayerAnimation(["Goblin_sprites_walking/goblin_walk_left_{}.png".format(i) for i in range(1, 7)],
                                    0.09),
            "right": PlayerAnimation(["Goblin_sprites_walking/goblin_walk_right_{}.png".format(i) for i in range(1, 7)],
                                     0.09),
        }
        self.current_animation = "down"
        self.current_cycle = self.animations[self.current_animation]

        # Health module
        self.health = HealthModule(100)  # Start with 100 health
        self.invincible = False  # Flag for invincibility
        self.invincibility_start = 0  # Start time for invincibility


    # Handle player movement and animation
    def move(self, direction, dt):
        # Change animation if direction changes
        if direction != self.current_animation:
            self.current_animation = direction
            self.current_cycle = self.animations[direction]

        # Update animation
        self.current_cycle.update(dt)

    def take_damage(self, damage):
        if not self.invincible:
            self.health.take_damage(damage)  # Only take damage if not invincible
            self.invincible = True  # Enable invincibility
            self.invincibility_start = time()  # Record start time

    def update(self, dt):
        # Manage invincibility duration
        if self.invincible and (time() - self.invincibility_start) > defines.INVINCIBILITY_DURATION:
            self.invincible = False

    def draw(self, screen, camera):
        # If invincible, flash white
        if self.invincible:
            if int(time() * 10) % 2 == 0:  # Toggle every 0.1 second for flashing effect
                screen.blit(
                    self.current_cycle.get_current_frame(),
                    (self.rect.x - camera.offset_x, self.rect.y - camera.offset_y),
                )
            else:
                screen.blit(
                    pygame.Surface((player_size, player_size), pygame.SRCALPHA).convert_alpha(),
                    (self.rect.x - camera.offset_x, self.rect.y - camera.offset_y),
                )
        else:
            screen.blit(
                self.current_cycle.get_current_frame(),
                (self.rect.x - camera.offset_x, self.rect.y - camera.offset_y),
            )