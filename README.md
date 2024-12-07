
# **`raintty`** 🌧️  
Ever felt your terminal could use a little more… atmosphere? **`raintty`** is a humble, terminal-based rain simulator to help set the mood while you work (or procrastinate). Raindrops fall, splash, and drift with adjustable intensity and wind, and optional lightning flashes provide the occasional dramatic flair. It’s simple, it’s a little whimsical, and it’s entirely yours to play with.

---

## Features
- **Dynamic Weather**: Let the storm evolve with oscillating rain intensity, wind direction, and lightning frequency.
- **Interactive Controls**: Don’t like the weather? Change it:
  - `+`/`-`: Adjust rain intensity.
  - `[`/`]`: Shift wind direction.
  - `l`: Toggle lightning effects.
  - `h`: Show or hide the HUD (heads-up display).
  - `q`: Quit the simulation.
- **Toggleable HUD**: Display or hide real-time stats for a distraction-free experience.

---

## Getting Started

### Requirements
- Python 3.8+
- `curses` library (pre-installed on most systems).

### Installation
Clone the repository:
```bash
git clone https://github.com/your-username/raintty.git
cd raintty
```

Make the script executable:
```bash
chmod +x raintty.py
```

To run the script directly:
```bash
./raintty.py
```

### Optional: Install as a Global Program
Want **`raintty`** available anytime, anywhere? Install it globally:
1. Move the script to a directory in your `PATH` (e.g., `/usr/local/bin`):
   ```bash
   sudo mv raintty.py /usr/local/bin/raintty
   ```
2. Run the program with:
   ```bash
   raintty
   ```

---

## Command-Line Options
Tailor the storm to your liking with these options:

| Flag                | Description                                                 | Default       |
|---------------------|-------------------------------------------------------------|---------------|
| `-i`, `--intensity` | Set initial rain intensity (0.1–1.0).                       | `0.3`         |
| `-d`, `--duration`  | Set simulation duration (seconds).                          | Infinite (`q` to quit) |
| `-w`, `--wind`      | Set initial wind direction (`-10` to `10`).                 | `0`           |
| `-l`, `--lightning` | Enable optional lightning flashes.                          | Disabled      |
| `--dynamic`         | Enable dynamic weather transitions, optionally with randomness (`--dynamic 0.3`). | Disabled      |

---

## Interactive Controls
Storms should never be boring. Use these keys to mix things up:
- `+`/`-`: Increase or decrease rain intensity.
- `[`/`]`: Adjust wind speed and direction.
- `l`: Toggle lightning effects.
- `h`: Show or hide the HUD.
- `q`: Quit the simulation.

---

## Examples

1. A gentle drizzle with dynamic weather:
   ```bash
   raintty --dynamic
   ```

2. Light rain with occasional lightning:
   ```bash
   raintty -i 0.3 -l
   ```

3. Breezy, low-intensity rain for 5 minutes:
   ```bash
   raintty -i 0.2 -w -3 -d 300
   ```

4. Subtle changes with low randomness:
   ```bash
   raintty --dynamic 0.1
   ```

---

## Why **`raintty`**?  
Because sometimes your terminal deserves a break from being *all business*. Whether you’re zoning in or just zoning out, **`raintty`** adds a touch of atmosphere to your CLI.

---

## License
This project is licensed under the GNU General Public License v3.0. See `LICENSE` for details.

---

## Contributing
This is a simple project, but it’s yours to tinker with. If you have ideas, find bugs, or just want to improve things, open an issue or send a pull request. 

---
