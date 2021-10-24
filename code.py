import pygame
pygame.init()

from time import sleep


WIDTH = 600 # Width of the game
HEIGHT = 500 # Height of the game

WIDTH_CENTER = WIDTH // 2
HEIGHT_CENTER = HEIGHT // 2


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) # Use the width and the height to show the game
pygame.display.set_caption("Snake") # Name of the game

clock = pygame.time.Clock()

blue = (0, 0, 255) # Blue color
red = (255, 0, 0) # Red color
black = (0, 0, 0) # BLack color


# Shows a message on the screen
def message(text, color):
    FONT_SIZE = 50 # Size of the text

    TEXT_WIDTH_CENTER = WIDTH_CENTER - FONT_SIZE * 1.5 # Place the text in the width center
    TEXT_HEIGHT_CENTER = HEIGHT_CENTER - FONT_SIZE # Place the text in the height center

    font_style = pygame.font.SysFont("arial", FONT_SIZE) # Makes the font style

    message = font_style.render(text, True, color) # Edits the message with the color
    WINDOW.blit(message, [TEXT_WIDTH_CENTER, TEXT_HEIGHT_CENTER]) # Shows the message on the screen

    pygame.display.update() # Updates the screen to show the text


# Updates the screen
def update_window(vertical, horizontal):
    WINDOW.fill(black) # Deletes the previous snake block
    pygame.draw.rect(WINDOW, blue ,[vertical, horizontal, 10, 10]) # Draw a snake block in the middle
    pygame.display.update() # Updates the game screen

    clock.tick(10) # Snake's movement speed


def main():
    game_over = False # If the game is not being played

    vertical = WIDTH_CENTER # Vertical allignment ( left - right )
    horizontal = HEIGHT_CENTER # Horizontal allignment ( top - bottom )

    vertical_change = 0 # Amount to change the vertical allignment per tick     
    horizontal_change = 0 # Amount to change the horizontal allignment per tick 


    # If the user plays the game
    while not game_over:        
        # If the game is open
        for event in pygame.event.get():   
            # Check if the game is closed     
            if event.type == pygame.QUIT:
                game_over = True # Ends the game

            # If a player clicks on a key
            elif event.type == pygame.KEYDOWN:
                # If the player clicks on the top arrow or "w"
                if event.key == pygame.K_w  and horizontal_change == 0 or event.key == pygame.K_UP and horizontal_change == 0:
                    vertical_change = 0 # Resets the vertical movement
                    horizontal_change = -10 # Move the snake 10px per tick

                # If the player clicks on the down arrow or "s"
                elif event.key == pygame.K_s and horizontal_change == 0 or event.key == pygame.K_DOWN and horizontal_change == 0:
                    vertical_change = 0 # Resets the vertical movement
                    horizontal_change = 10 # Move the snake 10px per tick
                
                # If the player clicks on the left arrow or "a"
                elif event.key == pygame.K_a and vertical_change == 0 or event.key == pygame.K_LEFT and vertical_change == 0:
                    vertical_change = -10 # Move the snake 10px per tick
                    horizontal_change = 0 # Resets the horizontal movement
                
                # If the player clicks on the right arrow or "d"    
                elif event.key == pygame.K_d and vertical_change == 0 or event.key == pygame.K_RIGHT and vertical_change == 0:
                    vertical_change = 10 # Move the snake 10px per tick
                    horizontal_change = 0 # Resets the horizontal movement

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
        message("You lost", red) # Send a text and a color to the game
        sleep(5) # Wait 5 seconds quit the game
        pygame.quit() # Quit the game
        quit() # Quit the terminal

# If the code starts
if __name__ == "__main__":
    main()