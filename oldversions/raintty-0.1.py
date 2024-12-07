import curses
import random
import time


def clear_and_show(stdscr, message, color_pair):
    """Clears the screen and shows a message."""
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    stdscr.addstr(height // 2, (width - len(message)) // 2, message, curses.color_pair(color_pair))
    stdscr.refresh()


def generate_rain(stdscr, raindrops, splashes, intensity):
    """Updates raindrops, handles falling logic, and creates splashes."""
    # Get terminal dimensions dynamically
    height, width = stdscr.getmaxyx()

    # Add new raindrops at the top
    for x in range(width):
        if random.random() < intensity:
            raindrops.append((0, x))  # Add a new raindrop at the top row

    # Process existing raindrops
    new_raindrops = []
    for y, x in raindrops:
        if y + 1 >= height:  # Prevent going out of bounds
            continue
        if y + 1 == height - 1:  # If raindrop hits the bottom
            splashes[x] = time.time()  # Add a splash with a timestamp
            if 0 <= y < height and 0 <= x < width:  # Safely clear the raindrop
                stdscr.addch(y, x, ' ')
            if 0 <= x < width:  # Safely add splash
                try:
                    stdscr.addch(y + 1, x, random.choice(['~', '.', '\'']), curses.color_pair(2))
                except curses.error:
                    pass  # Ignore if addch fails
        else:
            # Move the raindrop down
            if 0 <= y < height and 0 <= x < width:
                stdscr.addch(y, x, ' ')  # Clear the old position
            if 0 <= y + 1 < height and 0 <= x < width:
                try:
                    stdscr.addch(y + 1, x, '|', curses.color_pair(1))  # Draw the raindrop
                except curses.error:
                    pass  # Ignore if addch fails
            new_raindrops.append((y + 1, x))  # Update the raindrop position

    # Fade out splashes
    current_time = time.time()
    for x, splash_time in list(splashes.items()):
        if current_time - splash_time > 0.5:  # Splash lasts 0.5 seconds
            splashes.pop(x)
            if 0 <= x < width:
                try:
                    stdscr.addch(height - 1, x, ' ')  # Safely clear splash
                except curses.error:
                    pass  # Ignore if addch fails

    return new_raindrops


def main(stdscr, intensity, duration):
    """Main function to run the rain simulation using curses."""
    # Set up curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)  # Make getch non-blocking
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)  # Rain color
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Splash color
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Message color

    # Initialize variables
    raindrops = []  # List of (y, x) positions for raindrops
    splashes = {}  # Dictionary to track splashes and their timestamps
    start_time = time.time()

    # Main simulation loop
    while time.time() - start_time < duration:
        stdscr.clear()
        raindrops = generate_rain(stdscr, raindrops, splashes, intensity)
        stdscr.refresh()
        time.sleep(0.1)  # Control the frame rate

    # Show end message
    clear_and_show(stdscr, "Thanks for watching DrizzleDance! 🌧️", 3)
    time.sleep(2)  # Pause before exiting


if __name__ == "__main__":
    # Get user inputs before initializing curses
    try:
        print("Welcome to DrizzleDance! 🌧️")
        intensity = float(input("Set rain intensity (0.1 - 1.0): ").strip())
        duration = int(input("Set duration in seconds: ").strip())
        print("Starting the simulation...")
        time.sleep(1)  # Pause before starting
    except ValueError:
        print("Invalid input. Using defaults: intensity=0.5, duration=10.")
        intensity, duration = 0.5, 10

    # Run the curses simulation
    curses.wrapper(main, intensity, duration)

