# 🕹️ Tetris – Clean & Modern Edition

본 리포지토리는 Python과 Pygame을 활용하여 제작된 모던 UI 기반 테트리스 게임입니다. 부드러운 그래픽, 라운드 블록, 그라데이션 배경, 그리드 라인 등 시각적으로 향상된 게임 플레이를 제공합니다. 게임 루프, 충돌 처리, 렌더링 파이프라인 등 게임 개발 핵심 개념을 학습하기 위한 최적의 예제입니다.

This repository contains a visually enhanced Tetris game built with Python and Pygame. It features a modern UI, smooth animations, rounded blocks, a gradient background, and a clean rendering pipeline, making it an excellent reference project for game development fundamentals.

---
```
## 1. 📂 Directory Structure

├── tetris.py        # Main game source code (Clean & Modern Edition)
└── README.md        # Project documentation
```
---

## 2. 💎 Game Features

### ✨ Modern Visual Design
* Gradient Background: A smooth, deep vertical gradient that changes gracefully down the viewport.
* Rounded Blocks: Custom tetromino cells rendered with smooth border-radius shapes and soft inner highlights.
* Subtle Grid Lines: Minimalist alignment guide layout designed for pixel‑perfect clarity.
* Clean Score UI: Sleek, anti-aliased font rendering tracking your performance in real-time.

### 🕹️ Smooth Gameplay Mechanics
* Auto-Falling Pieces: Dynamic gravity ticks that push pieces down.
* Fluid Input Handling: Responsive left, right, and soft-drop mechanics.
* Hard Drop (SPACE): Instantly snap and lock pieces directly to the floor.
* Classic Rotation (▲): Precise matrix rotation algorithm preventing boundary clipping.

### 📈 Scoring & Loop Systems
* Scoring System: Earn +100 points per cleared line. 
* Stateful Game Over Screen: Centered interface display tracking final scores with an instantaneous ENTER key restart loop.

---

## 3. ⌨️ Controls

| Key | Action |
| :---: | :--- |
| ◀ / ▶ | Move Left / Right |
| ▼ | Soft Drop (Accelerate) |
| ▲ | Rotate Piece Clockwise |
| SPACE | Hard Drop (Instant Lock) |
| ENTER | Restart Game (On Game Over Screen) |
| ESC / X | Quit Game |

---

## 🚀 4. Installation & Setup

### 1) Install Python
Download and install Python from the official portal: https://www.python.org/downloads/
* Make sure to check "Add Python to PATH" during the setup process.

### 2) Install Pygame
Open your system terminal or command prompt and run the following command:
python -m pip install pygame

### 3) Run the Game
Execute the main script file to start playing:
python tetris.py

---

## 🛠️ 5. Tech Stack

* Language: Python 3.x
* Graphics Framework: Pygame
* Graphics Pipeline: Custom software renderer handling anti-aliased font processing, mathematical box-model transformations for block corners, and row color-interpolation tables.

---

## 🧠 6. How It Works

### 🔄 Game Loop
Locked precisely at 60 FPS via Pygame's hardware clock system, managing:
1. Input Registry: Asynchronous event queue monitoring keys.
2. Gravity Adjuster: Regular step cycles dropping pieces.
3. Collision Detection: Out-of-bounds boundary and stacked pixel evaluation before moves apply.
4. Line Clears: Scans the active 2D layout list matrix to delete fully populated rows and insert clean lines up top.
5. Draw Calls: Triggers backbuffer updates prior to page-flipping coordinates.

### 🎨 Rendering Pipeline
Every frame renders following a strict layer hierarchy to prevent overlap artifacts:
Gradient Background -> Placed Blocks -> Falling Piece -> Grid Lines -> Score Interface

### 📊 Data Structures
* Grid Space: Managed using a fixed-dimensional 2D list array populated by RGB tuple matrices (R, G, B).
* Tetromino Templates: Defined inside standard binary nested list matrices representing block layouts.
* Rotation Logic: Handled smoothly by passing matrices through a combined zip-transposition and reversal algorithm:

def rotate(shape):
    return [list(row) for row in zip(*shape[::-1])]
---

## 👤 7. Author

Built with 💙 by Samuel, with assistance from Microsoft Copilot & Google Gemini.

A fun, educational project designed to learn clean UI layout architecture and complete step-by-step game loop implementation paradigms in Python.
