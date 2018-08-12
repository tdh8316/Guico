import Engine


def Event(event):
    if event.type == (Engine.KEYDOWN or Engine.KEYUP):
        Engine.pressed_key = event.key
    elif event.type == Engine.QUIT:
        Engine.loop = False
    else:
        Engine.pressed_key = None
    Engine.event_type = event.type


def is_key_pressed(key: str):
    if ord(key) == Engine.pressed_key:
        return True
    return False


