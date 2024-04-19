import pygame
import sys
import subprocess
from main import resolusion, define_colors, version_keys

# Initialize pygame
pygame.init()

# call on functions
screen_resolusion = resolusion()
program_state, program_version, Menu_Version, Settings_Version, Gameplay_Version, Title_Version = version_keys()

# Version indicator
Program_version = f"{program_state} {Title_Version}"
# define different fonts
version_font = pygame.font.SysFont(None, 20)


# Function to draw text on screen
def draw_text(surface, text, color, x, y):
    text_surface = version_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# Function to handle Enter key press
def handle_enter_key():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        subprocess.run(["python", "menu_menu.py"])
        pygame.quit()
        sys.exit()

# Main function
def main():
    # Set up the screen
    screen = pygame.display.set_mode((screen_resolusion[0], screen_resolusion[1]))
    pygame.display.set_caption("TITLESCREEN")
    icon = pygame.image.load("8bitsword.png")
    pygame.display.set_icon(icon)

    # Main loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill("BLACK")

        # Version indicators
        draw_text(screen, f"Game Version: {program_state} {Title_Version}", "WHITE", 15, screen_resolusion[1] - 50)

        # Handle Enter key press
        handle_enter_key()

        # Update the display
        pygame.display.flip()

    # Quit pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
