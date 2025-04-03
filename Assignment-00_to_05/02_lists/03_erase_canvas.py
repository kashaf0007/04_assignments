import pygame
pygame.init()

WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
ERASER_SIZE = 40

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Canvas Eraser")

grid = [[BLUE for _ in range(COLS)] for _ in range(ROWS)]

def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, grid[row][col], (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def erase_cells(eraser_rect):
    for row in range(ROWS):
        for col in range(COLS):
            cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if eraser_rect.colliderect(cell_rect):
                grid[row][col] = WHITE

def main():
    running = True
    eraser_rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, ERASER_SIZE, ERASER_SIZE)
    
    while running:
        screen.fill(WHITE)
        draw_grid()
        pygame.draw.rect(screen, WHITE, eraser_rect, 2)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
 
        mouse_x, mouse_y = pygame.mouse.get_pos()
        eraser_rect.topleft = (mouse_x - ERASER_SIZE // 2, mouse_y - ERASER_SIZE // 2)
 
        if pygame.mouse.get_pressed()[0]:
            erase_cells(eraser_rect)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == '__main__':
    main()