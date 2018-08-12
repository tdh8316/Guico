import Engine


def draw_text(window, text, x, y, size: int = 50, colour: tuple = (0, 0, 0)):
    largeText = Engine.pygame.font.Font(".\\NanumBarunpenR.ttf", size)
    textSurface = largeText.render(text, True, colour)
    TextSurf, TextRect = textSurface, textSurface.get_rect()
    window.display.blit(TextSurf, (x, y))