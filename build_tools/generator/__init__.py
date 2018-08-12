PYTHON_MAIN = "if __name__ == \"__main__\":"

WINDOW_NEW = "window = Engine.Window(size=({}, {}), title=\"{}\")"

DEF_MAIN = "def main():\n" \
           "\twhile Engine.loop:\n" \
           "\t\tfor event in Engine.pygame.event.get():\n" \
           "\t\t\tEngine.Event(event)\n" \
           "\t\twindow.display.fill((255, 255, 255))\n"

KEY_PRESSED = "\t\tif Engine.is_key_pressed(\"{}\"):"

DRAW_TEXT = "\t\tEngine.draw_text(window, \"{}\", {}, {})"
