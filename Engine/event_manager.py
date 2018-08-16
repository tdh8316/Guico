import Engine

latest_key = None


def Event(event):
    if event.type == (Engine.KEYDOWN or Engine.KEYUP):
        Engine.pressed_key = event.key
    elif event.type == Engine.QUIT:
        Engine.loop = False
    else:
        Engine.pressed_key = None
    Engine.event_type = event.type


def is_key_pressed(key: str):
    global latest_key
    if Engine.event_type == Engine.MOUSEMOTION or Engine.event_type == Engine.ACTIVEEVENT:
        if ord(key) == latest_key:
            return True
    elif Engine.event_type == Engine.KEYUP:
        latest_key = None
    if ord(key) == Engine.pressed_key:
        latest_key = ord(key)
        return True
    return False
