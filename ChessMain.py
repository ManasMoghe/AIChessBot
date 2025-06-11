import pygame as p
import ChessEngine


WIDTH = HEIGHT = 512
DIMENSION = 8  # 8x8 chess board
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def loadImages():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK','bP', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        try:
            IMAGES[piece] = p.transform.scale(p.image.load("AIChessBot/images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
        except:
            print(f"Failed to load image: {piece}")



def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

# Draw pieces on top of the board
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--':
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    print(gs.board)
    loadImages()
    running = True
    sqSelected=()
    playerMoves=[]
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running=False
            elif e.type == p.MOUSEBUTTONDOWN():
                col= location(0) //SQ_SIZE
                row= location(1)//SQ_SIZE
                sqSelected=(row,col)
                if sqSelected == (row,col):
                    sqSelected= ()
                    playerMoves=[]
                else:
                    sqSelected=(row,col)
                    playerMoves.append(sqSelected)
                if
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

if __name__ == "__main__":
    main()
