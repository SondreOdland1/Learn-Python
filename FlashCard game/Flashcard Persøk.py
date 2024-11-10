import pygame
import random
import os

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (144, 238, 144)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
DARK_RED = (200, 0, 0)
DARK_YELLOW = (200, 200, 0)
DARK_BLUE = (0, 0, 200)

# Screen setup
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flashcard Game')

# Font
font = pygame.font.SysFont(None, 48)

# Flashcards with both text and images in the same card (if needed)
flashcards = [
    {'question': '', 'answer': ['', 'image: '], 'repeats': 1},
    {'question': '', 'answer': ['', 'image: '], 'repeats': 1},
    {'question': '', 'answer': ['', 'image: '], 'repeats': 1},
    {'question': '', 'answer': ['', 'image: '], 'repeats': 1},
]

# Function to split text into multiple lines to fit within a maximum width
def split_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""
    
    for word in words:
        if font.size(current_line + word)[0] < max_width:
            current_line += word + " "
        else:
            lines.append(current_line)
            current_line = word + " "
    
    lines.append(current_line)
    return lines

# Function to draw multiple lines of text on the screen
def draw_text_multiline(text, font, color, surface, x, y, max_width):
    lines = split_text(text, font, max_width)
    for i, line in enumerate(lines):
        text_obj = font.render(line, True, color)
        surface.blit(text_obj, (x, y + i * font.get_linesize()))

# Function to display the question on the screen
def show_question(card):
    screen.fill(GREEN)
    draw_text_multiline(card['question'], font, BLACK, screen, 50, 100, 1000)
    pygame.display.flip()

# Function to display the answer, including both text and images
def show_answer(card, selected=None):
    screen.fill(GREEN)
    
    y_offset = 100  # Starting position for displaying text
    
    for item in card['answer']:
        if item.startswith('image:'):
            image_path = item.replace('image:', '').strip()
            
            if os.path.exists(image_path):
                image = pygame.image.load(image_path)
                image = pygame.transform.scale(image, (400, 400))  # Resize the image to 400x400
                image_rect = image.get_rect(center=(WIDTH // 2, y_offset + 200))  # Adjust y_offset for placing the image
                screen.blit(image, image_rect)
                y_offset += 450  # Adjust y_offset after displaying the image
            else:
                draw_text_multiline(f"Image not found: {image_path}", font, BLACK, screen, 50, y_offset, 1000)
                y_offset += 50
        else:
            # Display text portion
            draw_text_multiline(item, font, BLACK, screen, 50, y_offset, 1000)
            y_offset += font.get_linesize() * len(split_text(item, font, 1000))  # Adjust y_offset after text

    # Display a confirmation of the selection
    if selected == 'cant':
        draw_text_multiline("You selected: Can't", font, RED, screen, 50, y_offset, 1000)
    elif selected == 'medium':
        draw_text_multiline("You selected: Medium", font, YELLOW, screen, 50, y_offset, 1000)
    elif selected == 'can':
        draw_text_multiline("You selected: Can", font, BLUE, screen, 50, y_offset, 1000)
    
    # Display buttons for "Can't", "Medium", "Can"
    pygame.draw.rect(screen, DARK_RED if selected == 'cant' else RED, [50, HEIGHT - 100, 200, 50])  # "Can't" button
    pygame.draw.rect(screen, DARK_YELLOW if selected == 'medium' else YELLOW, [300, HEIGHT - 100, 200, 50])  # "Medium" button
    pygame.draw.rect(screen, DARK_BLUE if selected == 'can' else BLUE, [550, HEIGHT - 100, 200, 50])  # "Can" button

    draw_text_multiline("Can't", font, WHITE, screen, 100, HEIGHT - 95, 200)  # "Can't" text
    draw_text_multiline("Medium", font, BLACK, screen, 350, HEIGHT - 95, 200)  # "Medium" text
    draw_text_multiline("Can", font, WHITE, screen, 600, HEIGHT - 95, 200)  # "Can" text
    
    pygame.display.flip()

# Function to update the number of repeats based on user selection
def update_repeats(card, selection):
    if selection == 'cant':
        card['repeats'] = 3  # If user selects "Can't", show it 3 times next round
    elif selection == 'medium':
        card['repeats'] = 2  # If user selects "Medium", show it 2 times next round
    elif selection == 'can':
        card['repeats'] = 1  # If user selects "Can", show it 1 time next round

# Function to show the end menu
def show_end_menu():
    screen.fill(GREEN)
    draw_text_multiline("All questions completed!", font, BLACK, screen, 50, 200, 1000)
    draw_text_multiline("Press S to restart or Q to quit", font, BLACK, screen, 50, 300, 1000)
    pygame.display.flip()

# Function to restart the game, adjusting the frequency of questions based on user selections
def restart_game():
    global remaining_cards, current_card, showing_answer, selected
    remaining_cards = []  # Clear the list of remaining cards
    
    # Add each flashcard according to its repeat count
    for card in flashcards:
        remaining_cards.extend([card] * card['repeats'])
    
    random.shuffle(remaining_cards)  # Shuffle the flashcards
    current_card = remaining_cards.pop()
    showing_answer = False
    selected = None  # Reset selection for the new game
    show_question(current_card)

# Start by shuffling the questions and setting up a queue of flashcards
remaining_cards = random.sample(flashcards, len(flashcards))
current_card = remaining_cards.pop()
showing_answer = False  # Flag to track if the answer is being shown
selected = None  # Variable to keep track of which button is pressed

# Show the first question
show_question(current_card)

running = True
end_game = False  # Variable to control whether we are at the end of the game

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and not end_game:  # Handle mouse click when the game is running
            mouse_x, mouse_y = event.pos  # Get the position of the mouse click
            
            if not showing_answer:  # If the answer is not being shown, show it on the first click
                show_answer(current_card)
                showing_answer = True  # Now showing the answer
            
            else:  # If the answer is being shown, only allow button clicks
                # Check if user clicks one of the answer buttons on the answer screen
                if 50 <= mouse_x <= 250 and HEIGHT - 100 <= mouse_y <= HEIGHT - 50:
                    update_repeats(current_card, 'cant')  # User chose "Can't"
                    selected = 'cant'  # Track the selection
                elif 300 <= mouse_x <= 500 and HEIGHT - 100 <= mouse_y <= HEIGHT - 50:
                    update_repeats(current_card, 'medium')  # User chose "Medium"
                    selected = 'medium'  # Track the selection
                elif 550 <= mouse_x <= 750 and HEIGHT - 100 <= mouse_y <= HEIGHT - 50:
                    update_repeats(current_card, 'can')  # User chose "Can"
                    selected = 'can'  # Track the selection
                
                # Only move to the next question if a button was clicked
                if selected is not None:
                    if len(remaining_cards) == 0:  # When all questions are used up
                        show_end_menu()  # Show end menu
                        end_game = True  # Set end of game flag
                    else:
                        current_card = remaining_cards.pop()
                        show_question(current_card)
                        showing_answer = False  # Reset for next round
                        selected = None  # Reset the selection for the new card
        
        if end_game:  # Handle end menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # Press S to restart
                    restart_game()  # Restart the game
                    end_game = False  # Return to game
                    selected = None  # Reset the selection
                elif event.key == pygame.K_q:  # Press Q to quit
                    running = False  # Exit the game

# Quit pygame
pygame.quit()



