#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================== 
Project: Python Pong Game (Turtle) 
File: scoreboard.py 
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi) 
Created: 2025-10-20 
Updated: 2025-10-20 
License: MIT License (see LICENSE file for details)
=================================================================== 

Description: 
Scoreboard overlay for rendering scores and status messages using turtle.

Usage: 
from pypong.scoreboard import Scoreboard

Notes: 
- Keeps a hidden turtle for text; uses CFG.font for consistency.

===================================================================
"""
from __future__ import annotations
import turtle
from dataclasses import dataclass
from pypong.config import CFG


@dataclass
class Scoreboard:
    left_score: int = 0
    right_score: int = 0

    def __post_init__(self) -> None:
        self._t = turtle.Turtle(visible=False)
        self._t.speed(0)
        self._t.color(CFG.text_color)
        self._t.penup()

    def draw_center_divider(self, half_h: float) -> None:
        pen = turtle.Turtle(visible=False)
        pen.color(CFG.divider_color)
        pen.penup()
        pen.goto(0, -half_h)
        pen.setheading(90)
        pen.pensize(2)
        pen.pendown()
        for _ in range(int(half_h / 20)):
            pen.forward(10)
            pen.penup()
            pen.forward(10)
            pen.pendown()
        pen.hideturtle()

    def update(self, half_h: float) -> None:
        self._t.clear()
        self._t.goto(-100, half_h - 40)
        self._t.write(f"{self.left_score}", align="center", font=CFG.font)
        self._t.goto(100, half_h - 40)
        self._t.write(f"{self.right_score}", align="center", font=CFG.font)

    def message(self, text: str, half_h: float) -> None:
        self._t.goto(0, 0)
        self._t.write(text, align="center", font=CFG.font)

    def reset(self) -> None:
        self.left_score = 0
        self.right_score = 0
        self._t.clear()
