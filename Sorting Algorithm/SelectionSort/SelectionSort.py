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
DELAY = 0.5  # Delay in seconds

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Selection Sort Visualizer")

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


def selection_sort():
    """
    Generator to perform selection sort on the heights array.
    Yields after each swap to allow for visualization.
    """
    n = len(heights)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if heights[j] < heights[min_idx]:
                min_idx = j
        heights[i], heights[min_idx] = heights[min_idx], heights[i]
        yield


def main():
    """
    Main function to run the sorting visualization.
    """
    clock = pygame.time.Clock()
    running = True
    sorter = selection_sort()  # Create the sorter generator

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black
        draw_bars()  # Draw the bars on the screen

        try:
            next(sorter)  # Advance the sorting process by one step
        except StopIteration:
            pass  # The sorting process is complete

        pygame.display.update()  # Update the display
        time.sleep(DELAY)  # Delay to slow down the sorting process

    pygame.quit()  # Quit Pygame


if __name__ == "__main__":
    main()  # Run the main function
