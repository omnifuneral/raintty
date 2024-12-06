import curses
import random
import time
import argparse


def generate_rain(stdscr, raindrops, splashes, intensity, wind):
    """Updates raindrops, handles falling and wind logic, and creates splashes."""
    # Get terminal dimensions dynamically
    height, width = stdscr.getmaxyx()

    # Add new raindrops at the top
    for x in range(width):
        if random.random() < intensity:
            raindrops.append((0, x))  # Add a new raindrop at the top row

    # Process existing raindrops
    new_raindrops = []
    for y, x in raindrops:
        # Apply wind to horizontal movement
        x = (x + wind) % width  # Wrap around if the raindrop moves out of bounds

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


def lightning_flash_effect(stdscr, raindrops, splashes):
    """Handles the lightning flash effect."""
    height, width = stdscr.getmaxyx()
    
    # Brighten the screen
    stdscr.clear()
    for y, x in raindrops:
        if 0 <= y < height and 0 <= x < width:
            stdscr.addch(y, x, '|', curses.color_pair(3))  # Bright white raindrops
    for x in splashes.keys():
        if 0 <= x < width:
            try:
                stdscr.addch(height - 1, x, '~', curses.color_pair(3))  # Bright white splashes
            except curses.error:
                pass  # Ignore if addch fails

    stdscr.refresh()
    time.sleep(0.2)  # Flash lasts for 0.2 seconds


def main(stdscr, intensity, duration, wind, lightning):
    """Main function to run the rain simulation using curses."""
    # Set up curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)  # Make getch non-blocking
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)  # Rain color
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Splash color
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Lightning color

    # Initialize variables
    raindrops = []  # List of (y, x) positions for raindrops
    splashes = {}  # Dictionary to track splashes and their timestamps
    start_time = time.time()

    # Main simulation loop
    while True:
        if duration is not None and time.time() - start_time >= duration:
            break

        # Lightning effect
        lightning_flash = False
        if lightning and random.random() < 0.01:  # 1% chance of lightning per frame
            lightning_flash = True

        stdscr.clear()

        # Generate and draw raindrops
        raindrops = generate_rain(stdscr, raindrops, splashes, intensity, wind)

        # Apply lightning effect
        if lightning_flash:
            lightning_flash_effect(stdscr, raindrops, splashes)

        stdscr.refresh()
        time.sleep(0.1)  # Control the frame rate

        # Check for 'q' key press
        key = stdscr.getch()
        if key == ord('q'):
            break


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="`raintty`: A whimsical terminal rain simulator.")
    parser.add_argument(
        "-i", "--intensity", type=float, default=0.4,
        help="Set the rain intensity (default: 0.4, range: 0.1 to 1.0)"
    )
    parser.add_argument(
        "-d", "--duration", type=float, default=None,
        help="Set the duration of the simulation in seconds (default: runs until 'q' is pressed)"
    )
    parser.add_argument(
        "-w", "--wind", type=int, default=0,
        help="Set wind intensity (negative: left, positive: right, default: 0)"
    )
    parser.add_argument(
        "-l", "--lightning", action="store_true",
        help="Enable lightning flashes (default: off)"
    )
    args = parser.parse_args()

    # Validate intensity
    if not (0.1 <= args.intensity <= 1.0):
        print("Error: Intensity must be between 0.1 and 1.0.")
        exit(1)

    # Run the curses simulation
    curses.wrapper(main, args.intensity, args.duration, args.wind, args.lightning)

