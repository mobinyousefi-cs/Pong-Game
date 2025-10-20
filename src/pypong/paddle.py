#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================== 
Project: Python Pong Game (Turtle) 
File: paddle.py 
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi) 
Created: 2025-10-20 
Updated: 2025-10-20 
License: MIT License (see LICENSE file for details)
=================================================================== 

Description: 
Paddle sprite abstraction using turtle.Turtle. Provides constrained
movement and rectangle geometry for collision queries.

Usage: 
from pypong.paddle import Paddle

Notes: 
- Movement is clamped to keep the paddle fully on-screen.

===================================================================
"""
from __future__ import annotations
import turtle
from dataclasses import dataclass
from pypong.config import CFG
from pypong.physics import Rect


@dataclass
class Paddle:
    turtle_obj: turtle.Turtle
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.turtle_obj = turtle.Turtle(visible=False)
        self.turtle_obj.speed(0)
        self.turtle_obj.shape("square")
        self.turtle_obj.color(CFG.paddle_color)
        self.turtle_obj.shapesize(stretch_wid=CFG.paddle_height / 20, stretch_len=CFG.paddle_width / 20)
        self.turtle_obj.penup()
        self.x = x
        self.y = y
        self.turtle_obj.goto(self.x, self.y)
        self.turtle_obj.showturtle()

    def move(self, dy: float, half_h: float) -> None:
        new_y = self.y + dy
        # Clamp so paddle stays fully visible
        max_y = half_h - CFG.paddle_height / 2
        min_y = -max_y
        self.y = max(min(new_y, max_y), min_y)
        self.turtle_obj.sety(self.y)

    def rect(self) -> Rect:
        return Rect(self.x, self.y, CFG.paddle_width + CFG.collision_epsilon, CFG.paddle_height + CFG.collision_epsilon)
