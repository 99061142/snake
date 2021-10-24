import pygame

WIDTH = 600 # Width of the game
HEIGHT = 500 # Height of the game

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) # Use the width and the height to show the game
pygame.display.set_caption("Snake") # Name of the game

clock = pygame.time.Clock()

blue = (0, 0, 255) # Blue color
black = (0, 0, 0) # BLack color


# Updates the screen
def update_window(x1, y1):
    WINDOW.fill(black) # Deletes the previous snake block
    pygame.draw.rect(WINDOW, blue ,[x1, y1, 10, 10]) # Draw a snake block in the middle
    pygame.display.update() # Updates the game screen

    clock.tick(10) # Snake's movement speed


def main():
    game_over = False # If the game is not being played

    vertical = WIDTH // 2 # Vertical allignment ( left - right )
    horizontal = HEIGHT // 2 # Horizontal allignment ( top - bottom )

    vertical_change = 0 # Amount to change the vertical allignment      
    horizontal_change = 0 # Amount to change the horizontal allignment    


    # If the user plays the game
    while not game_over:        
        
        # If the game is open
        for event in pygame.event.get():   
            # Check if the game is closed     
            if event.type == pygame.QUIT:
                game_over = True # Ends the game

            # If a player clicks on a key
            elif event.type == pygame.KEYDOWN:
                
                # If the player clicks on the left arrow
                if event.key == pygame.K_a:
                    vertical_change = -10 # Changes the vertical allignent
                    horizontal_change = 0 # Changes the horizontal allignent
                
                # If the player clicks on the right arrow
                elif event.key == pygame.K_d:
                    vertical_change = 10 # Changes the vertical allignent
                    horizontal_change = 0 # Changes the horizontal allignent
                
                # If the player clicks on the top arrow
                elif event.key == pygame.K_w:
                    vertical_change = 0 # Changes the vertical allignent
                    horizontal_change = -10 # Changes the horizontal allignent
            
                # If the player clicks on the down arrow
                elif event.key == pygame.K_s:
                    vertical_change = 0 # Changes the vertical allignent
                    horizontal_change = 10 # Changes the horizontal allignent

        else:
            # If the snake is off screen
            if vertical < 0 or horizontal < 0:
                game_over = True # Ends the game
            
            # If the snake is not off screen
            else:
                vertical += vertical_change # Changes the horizontal allignent with the last arrow that is pressed
                horizontal += horizontal_change # Changes the horizontal allignent with the last arrow that is pressed

                update_window(vertical, horizontal) # Updates the window what the user sees

    # If the game gets closed
    else:
        pygame.quit() # Go out of the game
        quit() # Go out of the terminal

# If the code starts
if __name__ == "__main__":
    main()