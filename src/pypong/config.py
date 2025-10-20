#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================== 
Project: Python Pong Game (Turtle) 
File: config.py 
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi) 
Created: 2025-10-20 
Updated: 2025-10-20 
License: MIT License (see LICENSE file for details)
=================================================================== 

Description: 
Centralized configuration constants and parameters for tuning gameplay,
window properties, colors, and speed tiers.

Usage: 
from pypong.config import CFG

Notes: 
- Values are grouped logically; adjust to customize the game.
- All sizes are in turtle canvas pixels.

===================================================================
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class _Config:
    # Window
    title: str = "Python Pong (Mobin Yousefi)"
    width: int = 960
    height: int = 600
    bg_color: str = "#0b1021"

    # Colors & fonts
    paddle_color: str = "#e5e7eb"
    ball_color: str = "#93c5fd"
    divider_color: str = "#1f2937"
    text_color: str = "#e5e7eb"
    font_family: str = "Courier"
    font_size: int = 18
    font_style: str = "bold"

    # Gameplay
    paddle_width: int = 20
    paddle_height: int = 100
    paddle_speed: int = 28
    paddle_margin: int = 40  # distance from wall

    ball_radius: int = 10
    ball_init_speed: float = 7.0
    ball_speed_increase: float = 1.06
    ball_speed_cap: float = 22.0

    # Physics
    # Coarse collision padding to prevent "sticking" on paddles
    collision_epsilon: float = 1.0

    # Score
    max_score: int | None = None  # Set e.g. 11 to play to 11

    @property
    def font(self) -> Tuple[str, int, str]:
        return (self.font_family, self.font_size, self.font_style)


CFG = _Config()
