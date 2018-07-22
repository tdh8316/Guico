def message_display(text):
    largeText = pygame.font.Font(r"gui\resources\NanumBarunpenR.ttf", 69)
    textSurface = largeText.render(text, True, (255,255,255))
    TextSurf, TextRect = textSurface, textSurface.get_rect()
    TextRect.center = ((display_width/2),(display_height/2))
    DISPLAY.blit(TextSurf, TextRect)

    pygame.display.update()
