# Python Pong Game (Turtle)

A polished, object‑oriented implementation of the classic **Pong** game using Python's built‑in `turtle` graphics. The project follows a professional repository structure suitable for GitHub, includes unit tests for core physics, linting (Ruff), formatting (Black), and CI via GitHub Actions.

---

## Features
- Two‑player Pong (Left: **W/S**, Right: **Up/Down**)
- Progressive ball speed increase on paddle hits (configurable tiers)
- Clean OOP design: `Game`, `Ball`, `Paddle`, `Scoreboard`
- Deterministic physics helpers in `physics.py` (unit‑tested)
- Pausing (press **Space**), restart (**R**), quit (**Q**)
- Window resize‑safe layout (recomputes boundaries)

---

## Quick Start

```bash
# Python >= 3.10 recommended
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -e .

# Run
pypong
# or
python -m pypong
```

> Note: `turtle` is part of the Python standard library. On some Linux systems, you may need Tk support (`sudo apt-get install python3-tk`).

---

## Controls
- **W / S** – Move left paddle up/down
- **↑ / ↓** – Move right paddle up/down
- **Space** – Pause/Resume
- **R** – Restart match (scores reset)
- **Q** – Quit

---

## Project Structure
```
.
├── src/
│   └── pypong/
│       ├── __init__.py
│       ├── main.py
│       ├── game.py
│       ├── ball.py
│       ├── paddle.py
│       ├── scoreboard.py
│       ├── physics.py
│       └── config.py
├── tests/
│   └── test_physics.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .editorconfig
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

---

## Configuration
Tune gameplay in `src/pypong/config.py`:
- Window size, colors, fonts
- Paddle dimensions & movement speed
- Ball speed tiers and max speed
- Score to win (if you want match rules)

---

## Testing
```bash
pytest -q
```

Unit tests cover collision detection and bounce math (pure functions in `physics.py`). GUI elements are exercised indirectly by the physics API.

---

## Development
- Lint: `ruff check .`
- Format: `ruff format .` (Black compatible via Ruff)
- Type check (optional): `mypy src/` (configure if you add mypy)

---

## Packaging & Entry Points
The CLI entry point `pypong` is defined in `pyproject.toml` and maps to `pypong.main:main`.

---

## License
MIT License — see `LICENSE`.

---

## Acknowledgements
Built with ❤️ using Python `turtle`. Designed to be beginner‑friendly but production‑ready in repo hygiene and structure.

