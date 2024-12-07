import curses
import random
import time
import argparse


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

    # Initialize variables
    raindrops = []  # List of (y, x) positions for raindrops
    splashes = {}  # Dictionary to track splashes and their timestamps
    start_time = time.time()

    # Main simulation loop
    while True:
        if duration is not None and time.time() - start_time >= duration:
            break

        stdscr.clear()
        raindrops = generate_rain(stdscr, raindrops, splashes, intensity)
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
    args = parser.parse_args()

    # Validate intensity
    if not (0.1 <= args.intensity <= 1.0):
        print("Error: Intensity must be between 0.1 and 1.0.")
        exit(1)

    # Run the curses simulation
    curses.wrapper(main, args.intensity, args.duration)

