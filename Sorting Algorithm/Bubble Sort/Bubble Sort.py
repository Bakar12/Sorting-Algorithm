import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600  # Width and height of the screen
ARRAY_SIZE = 50  # Number of bars in the array
BAR_WIDTH = WIDTH // ARRAY_SIZE  # Width of each bar
FPS = 60  # Frames per second
DELAY = 0.01  # Delay in seconds

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort Visualizer")

# Create a list of random heights
heights = [random.randrange(HEIGHT) for _ in range(ARRAY_SIZE)]

# Create a font object
font = pygame.font.Font(None, 36)

def draw_bars():
    """
    Draw the bars on the screen based on the heights array.
    """
    for i in range(ARRAY_SIZE):
        color = (0, 0, 255 - (heights[i] * 255 // HEIGHT))  # Color the bars based on their height
        pygame.draw.rect(screen, color, (i * BAR_WIDTH, HEIGHT - heights[i], BAR_WIDTH, heights[i]))

def bubble_sort():
    """
    Generator to perform bubble sort on the heights array.
    Yields after each swap to allow for visualization.
    """
    num_swaps = 0
    for i in range(ARRAY_SIZE):
        for j in range(ARRAY_SIZE - i - 1):
            if heights[j] > heights[j + 1]:
                heights[j], heights[j + 1] = heights[j + 1], heights[j]
                num_swaps += 1
                yield num_swaps  # Yield the number of swaps

def main():
    """
    Main function to run the sorting visualization.
    """
    clock = pygame.time.Clock()
    running = True
    sorter = bubble_sort()  # Create the sorter generator

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black
        draw_bars()  # Draw the bars on the screen

        try:
            num_swaps = next(sorter)  # Advance the sorting process by one step
            text = font.render(f"Swaps: {num_swaps}", True, (255, 255, 255))  # Create a text surface
            screen.blit(text, (10, 10))  # Draw the text surface on the screen
        except StopIteration:
            pass  # The sorting process is complete

        pygame.display.update()  # Update the display
        time.sleep(DELAY)  # Delay to slow down the sorting process

    pygame.quit()  # Quit Pygame

if __name__ == "__main__":
    main()  # Run the main function