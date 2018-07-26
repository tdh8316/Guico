import pygame


def WINDOW(TITLE="Guico Display (pygame)", display_width=800, display_height=600):
    return f"""
# 1
display_width = {display_width}
display_height = {display_height}
pygame.init()
DISPLAY = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("{TITLE}")
fps = pygame.time.Clock()

# define point

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

    # 2
    DISPLAY.fill((255, 255, 255))
    
    # game
"""


def LABEL(FONT=".\\NanumBarunpenR.ttf"):
    return f"""
def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()
    
def message_display(text, x, y):
    largeText = pygame.font.Font(r"{FONT}", 69)
    textSurface = largeText.render(text, True, (0, 0, 0))
    TextSurf, TextRect = text_objects(text, largeText)
    DISPLAY.blit(TextSurf, (x, y))
"""
