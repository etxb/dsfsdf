import os
import re
import time
import random
from termcolor import colored

# Function to clear the console screen and reprint the banner and CLI text
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_title()

# Function to print ASCII title with dynamic gradient colors
def print_title():
    # Generate random RGB values for gradient colors within 0-255 range
    color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Construct the gradient title
    title = f"""
\033[38;5;117m╔═╗┌┬┐┬ ┬┬─┐┌┬┐┬ ┬  \033[0m\033[38;5;111m╔═╗┌─┐┬─┐┌┬┐\033[0m
\033[38;5;117m╚═╗ │ │ │├┬┘ ││└┬┘  \033[0m\033[38;5;111m║  │ │├┬┘ ││\033[0m
\033[38;5;117m╚═╝ ┴ └─┘┴└──┴┘ ┴   \033[0m\033[38;5;111m╚═╝└─┘┴└──┴┘\033[0m
    """
    
    # Print the title with colored gradient
    print(colored(title, 'white', attrs=['bold']))
    print("""
xiruss
          """)
    
# Define the paths using the current user's home directory
user_home = os.path.expanduser("~")
config_txt_path = r"C:\Program Files\EqualizerAPO\config\config.txt"
lite_plugin_js_path = os.path.join(user_home, "AppData", "Roaming", "BetterDiscord", "plugins", "Lite.plugin.js")
values_txt_path = r"F:\XirusCord\xiruscord.txt"

# ANSI art for nuke animation
nuke_animation = """
⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⠾⡆ 
⠀⠀⠀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠎⠀⡇ 
⠀⠀⠀⠉⠛⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⣇ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⠾⠛⠛⠛⠛⠛⠛⠛⠛⠃⠴⠶⠶⠶⠶⠶⠶⠶ 
"""

# Function to update files with spinning animation
def update_files():
    
    # Simulate reading values (replace with actual parsing code)
    gain = "2"
    bitrate = "512000"
    
    # Update successful, print updated settings
    clear_screen()
    print_title()
    print(f"\nSettings updated successfully!\n")
    print_settings(gain, bitrate, True)
    
    return gain, bitrate  # Return gain and bitrate values

# Function to print current settings and status
def print_settings(gain, bitrate, uncapped):
    clear_screen()  # Clear the screen to show only the banner and CLI text
    print(f"Current gain: {gain}")
    print(f"Current bitrate: {bitrate}")
    print(f"Uncapped: {uncapped}")
    
# Main function to continuously monitor and update
def main():
    clear_screen()

    try:
        last_modified = os.path.getmtime(values_txt_path)
    except FileNotFoundError:
        print(colored(f"Values file not found: {values_txt_path}", 'red'))
        return

    while True:
        try:
            current_modified = os.path.getmtime(values_txt_path)

            if current_modified != last_modified:
                
                gain, bitrate = update_files()  # Update files and get new gain and bitrate values
                print_settings(gain, bitrate, True)  # Display updated settings
                last_modified = current_modified  # Update last_modified after successful update
        except FileNotFoundError:
            return


if __name__ == "__main__":
    main()
