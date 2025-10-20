#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================== 
Project: Python Pong Game (Turtle) 
File: game.py 
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi) 
Created: 2025-10-20 
Updated: 2025-10-20 
License: MIT License (see LICENSE file for details)
=================================================================== 

Description: 
Top-level Game orchestration: window setup, event bindings, main loop,
collision handling, scoring, and control flow.

Usage: 
from pypong.game import Game
Game().run()

Notes: 
- Turtle animation uses manual update() for smoothness.
- Key bindings are registered once in setup().

===================================================================
"""
from __future__ import annotations
import turtle
from dataclasses import dataclass
from typing import Optional

from pypong.config import CFG
from pypong.paddle import Paddle
from pypong.ball import Ball
from pypong.scoreboard import Scoreboard
from pypong.physics import Rect, intersects_rect, wall_normal


@dataclass
class Game:
    screen: turtle.Screen | None = None
    left: Paddle | None = None
    right: Paddle | None = None
    ball: Ball | None = None
    scoreboard: Scoreboard | None = None
    paused: bool = False

    def setup(self) -> None:
        self.screen = turtle.Screen()
        self.screen.title(CFG.title)
        self.screen.bgcolor(CFG.bg_color)
        self.screen.setup(width=CFG.width, height=CFG.height)
        self.screen.tracer(0)  # manual updates

        half_w = self.screen.window_width() // 2
        half_h = self.screen.window_height() // 2

        self.left = Paddle(x=-half_w + CFG.paddle_margin, y=0)
        self.right = Paddle(x=half_w - CFG.paddle_margin, y=0)
        self.ball = Ball()
        self.scoreboard = Scoreboard()
        self.scoreboard.draw_center_divider(half_h)
        self.scoreboard.update(half_h)

        # Controls
        assert self.screen is not None
        self.screen.listen()
        self.screen.onkeypress(lambda: self.left.move(CFG.paddle_speed, self.screen.window_height() // 2), "w")
        self.screen.onkeypress(lambda: self.left.move(-CFG.paddle_speed, self.screen.window_height() // 2), "s")
        self.screen.onkeypress(lambda: self.right.move(CFG.paddle_speed, self.screen.window_height() // 2), "Up")
        self.screen.onkeypress(lambda: self.right.move(-CFG.paddle_speed, self.screen.window_height() // 2), "Down")
        self.screen.onkey(self.toggle_pause, "space")
        self.screen.onkey(self.restart, "r")
        self.screen.onkey(self.quit, "q")

    def toggle_pause(self) -> None:
        self.paused = not self.paused

    def restart(self) -> None:
        if not self.screen:
            return
        self.scoreboard.reset()
        self.ball.reset()
        self.scoreboard.update(self.screen.window_height() // 2)

    def quit(self) -> None:
        if self.screen:
            self.screen.bye()

    def _handle_collisions(self) -> Optional[int]:
        assert self.screen and self.left and self.right and self.ball and self.scoreboard
        half_w = self.screen.window_width() // 2
        half_h = self.screen.window_height() // 2

        # Wall collisions (top/bottom)
        normal = wall_normal(self.ball.x, self.ball.y, half_w, half_h, CFG.ball_radius)
        if normal is not None:
            nx, ny = normal
            # Scoring if hit left/right gutters
            if nx != 0:  # left/right wall
                if self.ball.x < 0:
                    self.scoreboard.right_score += 1
                    self.ball.reset(direction=-1)
                else:
                    self.scoreboard.left_score += 1
                    self.ball.reset(direction=1)
                self.scoreboard.update(half_h)
                return 1
            else:  # top/bottom
                self.ball.bounce(nx, ny)

        # Paddle collisions
        left_rect = self.left.rect()
        right_rect = self.right.rect()
        if intersects_rect(self.ball.x, self.ball.y, CFG.ball_radius, left_rect) and self.ball.vx < 0:
            self.ball.bounce(1.0, 0.0)
            self.ball.accelerate()
        elif intersects_rect(self.ball.x, self.ball.y, CFG.ball_radius, right_rect) and self.ball.vx > 0:
            self.ball.bounce(-1.0, 0.0)
            self.ball.accelerate()

        return None

    def run(self) -> None:
        self.setup()
        assert self.screen and self.ball and self.scoreboard

        while True:
            if not self.paused:
                self.ball.step()
                self._handle_collisions()
            self.screen.update()


def mainloop() -> None:
    Game().run()
