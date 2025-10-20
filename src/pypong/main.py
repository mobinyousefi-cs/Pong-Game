#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================== 
Project: Python Pong Game (Turtle) 
File: main.py 
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi) 
Created: 2025-10-20 
Updated: 2025-10-20 
License: MIT License (see LICENSE file for details)
=================================================================== 

Description: 
Console entry point for the Pong game. Initializes and starts the game.

Usage: 
python -m pypong
# or installed as a script:
pypong

Notes: 
- Keeps the CLI thin; all logic in Game.

===================================================================
"""
from __future__ import annotations
from pypong.game import Game


def main() -> None:
    Game().run()


if __name__ == "__main__":
    main()
