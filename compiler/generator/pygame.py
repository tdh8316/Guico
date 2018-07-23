def WINDOW(TITLE="Guico Display (pygame)", display_width=800, display_height=600):
    return f"""
# 1
display_width = {display_width}
display_height = {display_height}
pygame.init()
DISPLAY = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("{TITLE}")

# define point

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

        # 2

        pygame.display.update()
"""


def LABEL(FONT="gui/resources/NanumBarunpenR.ttf"):
    return f"""
def message_display(text):
    largeText = pygame.font.Font("{FONT}", 69)
    textSurface = largeText.render(text, True, (255,255,255))
    TextSurf, TextRect = textSurface, textSurface.get_rect()
    TextRect.center = ((display_width/2),(display_height/2))
    DISPLAY.blit(TextSurf, TextRect)

    pygame.display.update()
"""
