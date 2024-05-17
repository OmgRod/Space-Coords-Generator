import random
import pyperclip
import os

def generate_space_coords():
    # Generate random coordinates
    hours = random.randint(0, 23)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 59)
    degrees = random.randint(-90, 90)
    minutes_deg = random.randint(0, 59)
    seconds_deg = random.randint(0, 59)
    
    # Format coordinates
    coords = f"{hours}h {minutes}m {seconds}s, {'+' if degrees >= 0 else '-'}{abs(degrees)}° {minutes_deg}' {seconds_deg}\""
    return coords

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    input("Press Enter to generate random space coordinates and copy them to clipboard, or press Ctrl+C to exit...")
    
    # Generate coordinates
    space_coords = generate_space_coords()
    
    # Copy to clipboard
    pyperclip.copy(space_coords)
    
    # Print and clear console
    print("Random Space Coordinates:")
    print(space_coords)
    clear_console()