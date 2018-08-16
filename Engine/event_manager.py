import Engine


def Event(event):
    if event.type == Engine.QUIT:
        Engine.loop = False
    elif event.type == Engine.KEYUP:
        Engine.pressed_key = None
    Engine.event_type = event.type


def is_key_pressed(key: str):
    if Engine.key.get_pressed()[ord(key)]:
        Engine.pressed_key = key
        return True
    return False
