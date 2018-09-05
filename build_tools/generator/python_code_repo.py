PYTHON_MAIN = "if __name__ == \"__main__\":"

WINDOW_NEW = "window = Engine.Window(size=({}, {}), title=f\"{}\")"

DEF_MAIN_VAR = "def main():\n\tglobal {}\n" \
           "\twhile Engine.loop:\n" \
           "\t\tfor event in Engine.pygame.event.get():\n" \
           "\t\t\tEngine.Event(event)\n" \
           "\t\twindow.display.fill((255, 255, 255))\n"

DEF_MAIN = "def main():\n" \
           "\twhile Engine.loop:\n" \
           "\t\tfor event in Engine.pygame.event.get():\n" \
           "\t\t\tEngine.Event(event)\n" \
           "\t\twindow.display.fill((255, 255, 255))\n"

KEY_PRESSED = "\t\t{else_if} Engine.is_key_pressed(\"{}\"):"
KEY_PRESS_FALSE = "\t\telse:"

DRAW_TEXT = "\t\tEngine.draw_text(window, f\"{}\", {}, {})"
DRAW_IMAGE = "\t\tEngine.draw_image(window, fr\"{}\", {}, {})"

SCREEN_CLEAR = "\t\twindow.display.fill((255, 255, 255))"
