#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================== 
Project: Python Pong Game (Turtle) 
File: test_physics.py 
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi) 
Created: 2025-10-20 
Updated: 2025-10-20 
License: MIT License (see LICENSE file for details)
=================================================================== 

Description: 
Unit tests for collision detection and reflection math.

Usage: 
pytest -q

Notes: 
- GUI is not required; tests cover pure math functions only.

===================================================================
"""
from __future__ import annotations
import math
from pypong.physics import Rect, intersects_rect, reflect_velocity


def test_circle_rect_intersection_basic():
    rect = Rect(0, 0, 100, 50)
    # Circle touching right edge
    assert intersects_rect(50, 0, 10, rect)
    # Circle outside
    assert not intersects_rect(70, 0, 10, rect)


def test_reflect_velocity_horizontal():
    vx, vy = reflect_velocity(1.0, 0.0, (-1.0, 0.0))  # reflect on right wall
    assert math.isclose(vx, -1.0) and math.isclose(vy, 0.0)


def test_reflect_velocity_vertical():
    vx, vy = reflect_velocity(0.0, 2.0, (0.0, -1.0))  # reflect on top wall
    assert math.isclose(vx, 0.0) and math.isclose(vy, -2.0)
