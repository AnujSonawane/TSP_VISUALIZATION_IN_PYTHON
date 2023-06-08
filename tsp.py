'''
Author - Anuj Suresh Sonawane
Project - Visualization of Travelling salesman problem (TSP)
'''

import pygame
import math

# Set up the display
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Travelling Salesman Problem")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the font
font = pygame.font.SysFont(None, 30)

# Set up the cities
cities = []
num_cities = 0

# Set up the distance function
def distance(city1, city2):
    return math.sqrt((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2)

# Set up the path function
def path(cities, order):
    return [cities[i] for i in order]

# Set up the loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Add a city
            if event.button == 1:
                cities.append(event.pos)
                num_cities += 1
            # Reset the cities
            elif event.button == 3:
                cities = []
                num_cities = 0

    # Clear the screen
    screen.fill(WHITE)

    # Draw the cities
    for city in cities:
        pygame.draw.circle(screen, BLACK, city, 5)

    # Draw the path
    if num_cities > 1:
        current_order = list(range(num_cities))
        current_path = path(cities, current_order)
        best_order = current_order.copy()
        best_distance = sum([distance(current_path[i], current_path[i+1]) for i in range(num_cities-1)])
        best_distance += distance(current_path[num_cities-1], current_path[0])
        for i in range(math.factorial(num_cities)-1):
            # Generate the next permutation
            j = num_cities - 2
            while j >= 0 and current_order[j] >= current_order[j+1]:
                j -= 1
            if j == -1:
                break
            k = num_cities - 1
            while current_order[j] >= current_order[k]:
                k -= 1
            current_order[j], current_order[k] = current_order[k], current_order[j]
            current_order[j+1:] = reversed(current_order[j+1:])
            current_path = path(cities, current_order)
            # Calculate the current distance
            current_distance = sum([distance(current_path[i], current_path[i+1]) for i in range(num_cities-1)])
            current_distance += distance(current_path[num_cities-1], current_path[0])
            # Check if the current path is better than the best path
            if current_distance < best_distance:
                best_order = current_order.copy()
                best_distance = current_distance
        for i in range(num_cities-1):
            pygame.draw.line(screen, GREEN, current_path[i], current_path[i+1], 2)
        pygame.draw.line(screen, GREEN, current_path[num_cities-1], current_path[0], 2)

        # Draw the current distance and the best distance
        text = font.render("Current Distance: {:.2f}".format(current_distance), True, BLACK)
        screen.blit(text, (20, HEIGHT-50))
        text = font.render("Best Distance: {:.2f}".format(best_distance), True, BLACK)
        screen.blit(text, (20, HEIGHT-20))

    # Update the display
    pygame.display.update()

# Quit Pygame properly
pygame.quit()
