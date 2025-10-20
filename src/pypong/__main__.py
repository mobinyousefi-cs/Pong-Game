#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================== 
Project: Python Pong Game (Turtle) 
File: __main__.py 
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi) 
Created: 2025-10-20 
Updated: 2025-10-20 
License: MIT License (see LICENSE file for details)
=================================================================== 

Description: 
Module entrypoint so that `python -m pypong` runs the game.

Usage: 
python -m pypong

Notes: 
- Delegates to pypong.main.main

===================================================================
"""
from __future__ import annotations
from pypong.main import main

if __name__ == "__main__":
    main()
