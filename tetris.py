import pygame
import random

# --- config ---
WIDTH, HEIGHT = 320, 640
BLOCK = 32
COLS, ROWS = WIDTH // BLOCK, HEIGHT // BLOCK

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris – Clean Edition")
clock = pygame.time.Clock()

# nice color palette
COLORS = [
    (0, 255, 255),   # I
    (0, 120, 255),   # J
    (255, 160, 0),   # L
    (255, 220, 0),   # O
    (0, 220, 120),   # S
    (255, 80, 120),  # Z
    (180, 80, 255)   # T
]

SHAPES = [
    [[1,1,1,1]],
    [[1,0,0],[1,1,1]],
    [[0,0,1],[1,1,1]],
    [[1,1],[1,1]],
    [[0,1,1],[1,1,0]],
    [[1,1,0],[0,1,1]],
    [[0,1,0],[1,1,1]]
]

FONT_SMALL = pygame.font.SysFont("consolas", 18, bold=True)
FONT_BIG   = pygame.font.SysFont("consolas", 32, bold=True)

def rotate(shape):
    return [list(row) for row in zip(*shape[::-1])]

class Piece:
    def __init__(self):
        self.index = random.randrange(len(SHAPES))
        self.shape = SHAPES[self.index]
        self.color = COLORS[self.index]
        self.x = COLS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def cells(self):
        for r, row in enumerate(self.shape):
            for c, val in enumerate(row):
                if val:
                    yield self.x + c, self.y + r

def valid(piece, grid):
    for x, y in piece.cells():
        if x < 0 or x >= COLS or y >= ROWS:
            return False
        if y >= 0 and grid[y][x] != (0,0,0):
            return False
    return True

def clear_rows(grid):
    full = [i for i,row in enumerate(grid) if all(col!=(0,0,0) for col in row)]
    for i in full:
        del grid[i]
        grid.insert(0, [(0,0,0)]*COLS)
    return len(full)

def draw_background():
    # vertical gradient
    for y in range(HEIGHT):
        t = y / HEIGHT
        r = int(15 + 25 * t)
        g = int(15 + 40 * t)
        b = int(25 + 60 * t)
        pygame.draw.line(screen, (r,g,b), (0,y), (WIDTH,y))

def draw_grid():
    # subtle grid lines
    grid_color = (40, 40, 60)
    for x in range(COLS+1):
        pygame.draw.line(screen, grid_color, (x*BLOCK, 0), (x*BLOCK, HEIGHT))
    for y in range(ROWS+1):
        pygame.draw.line(screen, grid_color, (0, y*BLOCK), (WIDTH, y*BLOCK))

def draw_block(x, y, color):
    px = x * BLOCK
    py = y * BLOCK
    rect = pygame.Rect(px+2, py+2, BLOCK-4, BLOCK-4)

    # base
    pygame.draw.rect(screen, color, rect, border_radius=6)
    # outline
    pygame.draw.rect(screen, (20,20,30), rect, width=2, border_radius=6)
    # highlight
    highlight = pygame.Rect(px+4, py+4, BLOCK-8, BLOCK-8)
    hcolor = (min(color[0]+40,255), min(color[1]+40,255), min(color[2]+40,255))
    pygame.draw.rect(screen, hcolor, highlight, width=1, border_radius=6)

def draw(grid, piece, score):
    draw_background()

    # placed blocks
    for y,row in enumerate(grid):
        for x,color in enumerate(row):
            if color != (0,0,0):
                draw_block(x, y, color)

    # falling piece
    for x,y in piece.cells():
        if y >= 0:
            draw_block(x, y, piece.color)

    draw_grid()

    # score box
    score_text = FONT_SMALL.render(f"Score: {score}", True, (230,230,240))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

def game_over_screen(score):
    draw_background()
    msg1 = FONT_BIG.render("GAME OVER", True, (255, 220, 220))
    msg2 = FONT_SMALL.render(f"Final Score: {score}", True, (230,230,240))
    msg3 = FONT_SMALL.render("Press ENTER to play again", True, (200,200,220))

    screen.blit(msg1, (WIDTH//2 - msg1.get_width()//2, HEIGHT//2 - 60))
    screen.blit(msg2, (WIDTH//2 - msg2.get_width()//2, HEIGHT//2))
    screen.blit(msg3, (WIDTH//2 - msg3.get_width()//2, HEIGHT//2 + 40))
    pygame.display.flip()

    waiting = True
    while waiting:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    waiting = False
        clock.tick(30)
    return True

def main():
    while True:
        grid = [[(0,0,0)]*COLS for _ in range(ROWS)]
        piece = Piece()
        fall_timer = 0
        speed = 0.5
        score = 0
        running = True

        while running:
            dt = clock.tick(60) / 1000
            fall_timer += dt

            # auto fall
            if fall_timer >= speed:
                fall_timer = 0
                piece.y += 1
                if not valid(piece, grid):
                    piece.y -= 1
                    for x,y in piece.cells():
                        if 0 <= y < ROWS:
                            grid[y][x] = piece.color
                    cleared = clear_rows(grid)
                    if cleared:
                        score += cleared * 100
                    piece = Piece()
                    if not valid(piece, grid):
                        running = False

            # input
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    return
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LEFT:
                        piece.x -= 1
                        if not valid(piece, grid):
                            piece.x += 1
                    elif e.key == pygame.K_RIGHT:
                        piece.x += 1
                        if not valid(piece, grid):
                            piece.x -= 1
                    elif e.key == pygame.K_DOWN:
                        piece.y += 1
                        if not valid(piece, grid):
                            piece.y -= 1
                    elif e.key == pygame.K_UP:
                        old = piece.shape
                        piece.shape = rotate(piece.shape)
                        if not valid(piece, grid):
                            piece.shape = old
                    elif e.key == pygame.K_SPACE:
                        # hard drop
                        while True:
                            piece.y += 1
                            if not valid(piece, grid):
                                piece.y -= 1
                                break

            draw(grid, piece, score)

        # game over
        if not game_over_screen(score):
            break

if __name__ == "__main__":
    main()

   
