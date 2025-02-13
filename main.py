import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Fill screen with black color
        screen.fill("black")  # You can also use (0, 0, 0) for black
        
        # Update the display
        pygame.display.flip()
    
        dt = clock.tick(60) / 1000.0

    pygame.quit()

if __name__ == "__main__":
    main()
