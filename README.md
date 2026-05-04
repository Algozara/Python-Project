# Python Game - Mod the Game: Python Arcade Remix

A collaborative student project modifying an open-source Python Arcade game. This project demonstrates code exploration, collaborative development, and documentation practices used in real software teams.

## Project Overview

This team project involved selecting an existing Python Arcade game and making observable changes to visuals, gameplay, and code structure. Our modifications showcase:
- **Visual Change:** [Brief description, e.g., "Changed background color from blue to purple"]
- **Gameplay Change:** [Brief description, e.g., "Increased enemy spawn rate by 20%"]
- **Code Refactor:** [Brief description, e.g., "Added documentation comments to sprite collision detection module"]

## Team Members & Roles

| Name | Role | Responsibility |
|------|------|-----------------|
| [Team Lead Name] | Team Lead | Game setup, code exploration guide, refactoring, final submission |
| [Developer 1 Name] | Developer 1 | Visual modification and documentation |
| [Developer 2 Name] | Developer 2 | Gameplay modification and documentation |

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git (optional, for cloning)

### Steps to Run

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/[your-username]/[repo-name].git
   cd [repo-name]
   ```

2. **Install dependencies**
   ```bash
   pip install arcade
   ```
   Or install all requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game**
   ```bash
   python main.py
   ```

## Project Changes

### 1. Visual Change - [Developer 1]

**What was changed:**
- [Specific description of the visual modification]

**File(s) modified:**
- `[filename].py` (lines X–Y)

**How to see it:**
- [Instructions on what to look for when running the game, e.g., "The main menu background is now purple instead of blue"]

**Code snippet:**
```python
# Example: Before and after code
# BEFORE:
# background_color = (0, 0, 255)  # Blue

# AFTER:
background_color = (128, 0, 128)  # Purple - Changed to match team theme
```

---

### 2. Gameplay Change - [Developer 2]

**What was changed:**
- [Specific description of the gameplay modification, e.g., "Enemy spawn rate increased"]

**File(s) modified:**
- `[filename].py` (lines X–Y)

**How to see it:**
- [Instructions on how to observe the change during gameplay, e.g., "Notice enemies appear more frequently after 30 seconds"]

**Code snippet:**
```python
# Example: Before and after code
# BEFORE:
# spawn_rate = 0.5

# AFTER:
spawn_rate = 0.6  # Increased spawn frequency by 20% for more challenge
```

---

### 3. Code Refactor - [Team Lead]

**What was changed:**
- [Description of refactoring or documentation added]

**File(s) modified:**
- `[filename].py`

**Details:**
- [Explanation of why this refactor improves code clarity or maintainability]

**Code snippet:**
```python
# Example: Added documentation block
def check_collision(sprite1, sprite2):
    """
    Checks if two sprites overlap and triggers appropriate response.

    Args:
        sprite1 (Sprite): First sprite object
        sprite2 (Sprite): Second sprite object

    Returns:
        bool: True if sprites collide, False otherwise
    """
    # Collision detection logic here
    pass
```

---

## File Structure

```
[repo-name]/
├── main.py                 # Main game file (entry point)
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── assets/
│   ├── images/            # Sprite and background images
│   └── sounds/            # Game sound files (if applicable)
└── [other project files]
```

## Testing

To verify all changes work correctly:

1. Run the game: `python main.py`
2. Test visual change: [Specific test steps]
3. Test gameplay change: [Specific test steps]
4. Check for errors: [Any edge cases to watch for]

## Original Game Source

- **Original Game:** [Game name and link to original repository]
- **License:** [Original license, e.g., MIT]
- **Attribution:** This project modifies the original [Game Name] created by [Original Author]

## Technical Details

- **Language:** Python 3.x
- **Framework:** Arcade (Python game library)
- **Development Time:** ~10 class days (collaborative project)
- **Original Code Size:** ~[X] lines
- **Modified Code Size:** ~[Y] lines
- **Changes Made:** 3 modifications (1 visual, 1 gameplay, 1 refactor)

## How to Present This Project

Each team member will present their portion (5 minutes total):

- **Team Lead:** Introduces the project, original game choice, and explains the refactor
- **Developer 1:** Demonstrates the visual change and explains the code modification
- **Developer 2:** Demonstrates the gameplay change and explains the code modification

**Pro tip:** Practice running the game smoothly and have before-and-after descriptions ready.

## Learning Outcomes Achieved

- ✅ Navigated and understood an existing Python codebase
- ✅ Made observable, intentional changes to code and assets
- ✅ Collaborated using real-world team dynamics (roles, responsibilities, deadlines)
- ✅ Documented and explained modifications clearly
- ✅ Presented technical work to an audience

## Stretch Goals (Optional Enhancements)

- [ ] Added sound effects to gameplay
- [ ] Modified game title or splash screen
- [ ] Implemented a new scoring rule or bonus system
- [ ] Packaged game for easy sharing

## Troubleshooting

**Game won't start:**
- Ensure Python 3.8+ is installed: `python --version`
- Reinstall Arcade: `pip install --upgrade arcade`

**Graphics or sprites not showing:**
- Check that asset files exist in the `assets/` directory
- Verify file paths in code match actual file locations

**Performance issues:**
- Close other programs to free up system resources
- Check game frame rate in-game (typically displays in console)

## Contributing

This is a class project, but if you'd like to make additional improvements:
1. Fork the repository
2. Create a feature branch: `git checkout -b improvement/feature-name`
3. Commit changes: `git commit -m "Description of change"`
4. Push to branch: `git push origin improvement/feature-name`
5. Open a Pull Request

## License

This project modifies [Original Game Name] which is licensed under [Original License].
Our modifications are available for educational purposes.

## Acknowledgments

- Original game creator: [Original Author Name]
- Instructor: [Instructor Name]
- Bates Technical College
- Python Arcade library team

---

**Project Submission Date:** [Date]  
**In-Class Presentation Date:** Tuesday, December at 1:30 PM  
**Last Updated:** [Date]
