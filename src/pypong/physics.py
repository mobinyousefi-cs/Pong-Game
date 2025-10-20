#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================== 
Project: Python Pong Game (Turtle) 
File: physics.py 
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi) 
Created: 2025-10-20 
Updated: 2025-10-20 
License: MIT License (see LICENSE file for details)
=================================================================== 

Description: 
Pure functions that model collision detection and bounce responses for
ball-wall and ball-paddle interactions. Separated for unit testing.

Usage: 
from pypong.physics import intersects_rect, reflect_velocity

Notes: 
- Coordinates follow turtle screen: origin at center, +x right, +y up.
- Paddles are axis-aligned rectangles specified by (cx, cy, w, h).
- Ball is a circle at (x, y) with radius r.

===================================================================
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Rect:
    cx: float
    cy: float
    w: float
    h: float

    @property
    def left(self) -> float:
        return self.cx - self.w / 2

    @property
    def right(self) -> float:
        return self.cx + self.w / 2

    @property
    def top(self) -> float:
        return self.cy + self.h / 2

    @property
    def bottom(self) -> float:
        return self.cy - self.h / 2


def intersects_rect(x: float, y: float, r: float, rect: Rect) -> bool:
    """Return True if a circle (x, y, r) intersects an axis-aligned rect.

    Uses closest-point clamping test.
    """
    # Clamp circle center to rect bounds
    clamped_x = min(max(x, rect.left), rect.right)
    clamped_y = min(max(y, rect.bottom), rect.top)
    dx = x - clamped_x
    dy = y - clamped_y
    return dx * dx + dy * dy <= r * r


def reflect_velocity(vx: float, vy: float, normal: Tuple[float, float]) -> Tuple[float, float]:
    """Reflect (vx, vy) across a given surface normal (nx, ny)."""
    nx, ny = normal
    # Normalize normal
    mag = (nx * nx + ny * ny) ** 0.5
    if mag == 0:
        return -vx, vy
    nx, ny = nx / mag, ny / mag
    # v' = v - 2*(v·n)*n
    dot = vx * nx + vy * ny
    rx = vx - 2 * dot * nx
    ry = vy - 2 * dot * ny
    return rx, ry


def wall_normal(x: float, y: float, half_w: float, half_h: float, r: float) -> Tuple[float, float] | None:
    """Return the outward normal of the wall the ball collides with, else None."""
    if x + r >= half_w:
        return (-1.0, 0.0)
    if x - r <= -half_w:
        return (1.0, 0.0)
    if y + r >= half_h:
        return (0.0, -1.0)
    if y - r <= -half_h:
        return (0.0, 1.0)
    return None
