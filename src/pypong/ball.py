#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================== 
Project: Python Pong Game (Turtle) 
File: ball.py 
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi) 
Created: 2025-10-20 
Updated: 2025-10-20 
License: MIT License (see LICENSE file for details)
=================================================================== 

Description: 
Ball sprite abstraction with velocity, speed escalation, and reset
behavior.

Usage: 
from pypong.ball import Ball

Notes: 
- Uses turtle.Turtle for rendering; physics math in physics.py

===================================================================
"""
from __future__ import annotations
import random
import turtle
from dataclasses import dataclass
from pypong.config import CFG


@dataclass
class Ball:
    turtle_obj: turtle.Turtle
    x: float
    y: float
    vx: float
    vy: float

    def __init__(self) -> None:
        self.turtle_obj = turtle.Turtle(visible=False)
        self.turtle_obj.speed(0)
        self.turtle_obj.shape("circle")
        self.turtle_obj.color(CFG.ball_color)
        # Default circle size is 20px; scale to radius
        scale = CFG.ball_radius / 10
        self.turtle_obj.shapesize(stretch_wid=scale, stretch_len=scale)
        self.turtle_obj.penup()
        self.reset(direction=random.choice([-1, 1]))
        self.turtle_obj.showturtle()

    def step(self) -> None:
        self.x += self.vx
        self.y += self.vy
        self.turtle_obj.goto(self.x, self.y)

    def bounce(self, nx: float, ny: float) -> None:
        # Reflect velocity across normal (nx, ny)
        dot = self.vx * nx + self.vy * ny
        self.vx -= 2 * dot * nx
        self.vy -= 2 * dot * ny

    def accelerate(self) -> None:
        # Increase speed while preserving direction
        speed = (self.vx ** 2 + self.vy ** 2) ** 0.5
        speed = min(speed * CFG.ball_speed_increase, CFG.ball_speed_cap)
        angle = turtle.towards(self.x + self.vx, self.y + self.vy)  # not ideal; replace with atan2
        # Recompute vx, vy with preserved angle
        # Using math.atan2 for precision
        import math
        theta = math.atan2(self.vy, self.vx)
        self.vx = speed * math.cos(theta)
        self.vy = speed * math.sin(theta)

    def reset(self, direction: int = 1) -> None:
        self.x = 0.0
        self.y = 0.0
        import math
        # Randomize initial angle slightly to avoid boring vertical rallies
        angle = math.radians(random.choice([-30, -20, -15, 15, 20, 30]))
        vx = CFG.ball_init_speed * math.cos(angle) * direction
        vy = CFG.ball_init_speed * math.sin(angle)
        self.vx, self.vy = vx, vy
        self.turtle_obj.goto(self.x, self.y)
