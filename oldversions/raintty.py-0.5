import curses
import random
import time
import argparse
import math


def generate_rain(stdscr, raindrops, splashes, intensity, wind):
    """Updates raindrops, handles falling and wind logic, and creates splashes."""
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
            if 0 <= y < height and 0 <= x < width:
                stdscr.addch(y, x, ' ')  # Clear the raindrop
            if 0 <= x < width:
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
        if current_time - splash_time > 0.5:
            splashes.pop(x)
            if 0 <= x < width:
                try:
                    stdscr.addch(height - 1, x, ' ')  # Clear splash
                except curses.error:
                    pass

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

    stdscr.refresh()  # Force redraw for the lightning flash
    time.sleep(0.2)  # Flash lasts for 0.2 seconds

    # Reset the screen after the flash
    stdscr.clear()
    stdscr.refresh()

def display_settings(stdscr, intensity, wind, lightning):
    """Displays the current settings."""
    height, width = stdscr.getmaxyx()  # Get current terminal dimensions
    settings = f"Intensity: {intensity:.2f}  Wind: {wind:+d}  Lightning: {'ON' if lightning else 'OFF'}"
    stdscr.addstr(height - 1, 0, settings[:width - 1])  # Truncate if too long

def main(stdscr, intensity, duration, wind, lightning, dynamic, randomness):
    """Main function to run the rain simulation with dynamic changes and interactive controls."""
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)  # Make getch non-blocking
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)  # Rain color
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Splash color
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Lightning color

    raindrops = []  # List of (y, x) positions for raindrops
    splashes = {}  # Dictionary to track splashes and their timestamps
    start_time = time.time()

    cycle_time = 0
    show_hud = True  # Default HUD visibility

    while True:
        if duration is not None and time.time() - start_time >= duration:
            break

        # Dynamic Mode Adjustments
        if dynamic:
            cycle_time += 0.05  # Slow down changes (smaller increments)
            intensity = max(
                0.1,
                min(
                    1.0,
                    0.5 + 0.2 * math.sin(cycle_time) +  # Reduce amplitude to ±0.2
                    random.uniform(-randomness / 2, randomness / 2)  # Scale down randomness
                )
            )
            wind = max(
                -5,  # Reduce wind range to ±5
                min(
                    5,
                    int(2 * math.sin(cycle_time / 3) +  # Slower, smoother wind oscillation
                        random.uniform(-randomness * 5, randomness * 5))  # Scale randomness
                )
            )


        # Lightning Effect
        lightning_flash = lightning and random.random() < (0.02 if intensity > 0.7 else 0.005)

        # Handle keypress for interactive controls
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == ord('+'):
            intensity = min(1.0, intensity + 0.1)
        elif key == ord('-'):
            intensity = max(0.1, intensity - 0.1)
        elif key == ord('['):
            wind = max(-10, wind - 1)
        elif key == ord(']'):
            wind = min(10, wind + 1)
        elif key == ord('l'):
            lightning = not lightning
        elif key == ord('h'):
            show_hud = not show_hud

        stdscr.clear()

        # Generate and draw raindrops
        raindrops = generate_rain(stdscr, raindrops, splashes, intensity, wind)

        # Lightning flash
        if lightning_flash:
            lightning_flash_effect(stdscr, raindrops, splashes)

        # Display settings if HUD is enabled
        if show_hud:
            display_settings(stdscr, intensity, wind, lightning)

        stdscr.refresh()

        # Add a frame rate delay to control speed
        time.sleep(0.1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="`raintty`: A whimsical terminal rain simulator.")
    parser.add_argument("-i", "--intensity", type=float, default=0.4, help="Rain intensity (default: 0.4).")
    parser.add_argument("-d", "--duration", type=float, default=None, help="Simulation duration in seconds.")
    parser.add_argument("-w", "--wind", type=int, default=0, help="Initial wind intensity.")
    parser.add_argument("-l", "--lightning", action="store_true", help="Enable lightning flashes.")
    parser.add_argument(
        "--dynamic", nargs='?', const=0.2, type=float,
        help="Enable dynamic weather transitions with optional randomness (default: 0.2)."
    )
    args = parser.parse_args()

    if not (0.1 <= args.intensity <= 1.0):
        print("Error: Intensity must be between 0.1 and 1.0.")
        exit(1)
    if args.dynamic is not None and not (0.0 <= args.dynamic <= 1.0):
        print("Error: Randomness must be between 0.0 and 1.0.")
        exit(1)

    curses.wrapper(
        main, args.intensity, args.duration, args.wind, args.lightning, args.dynamic is not None, args.dynamic or 0.0
    )

