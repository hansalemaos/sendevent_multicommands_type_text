import random

mappingdict = {
    " ": "KEY_SPACE:ud:%s",
    "!": "KEY_LEFTSHIFT:d:0#KEY_1:ud:%s#KEY_LEFTSHIFT:u:0",
    "'": "KEY_APOSTROPHE:ud:%s",
    '"': "KEY_LEFTSHIFT:d:0#KEY_APOSTROPHE:ud:%s#KEY_LEFTSHIFT:u:0",
    "#": "KEY_LEFTSHIFT:d:0#KEY_3:ud:%s#KEY_LEFTSHIFT:u:0",
    "$": "KEY_LEFTSHIFT:d:0#KEY_4:ud:%s#KEY_LEFTSHIFT:u:0",
    "%": "KEY_LEFTSHIFT:d:0#KEY_5:ud:%s#KEY_LEFTSHIFT:u:0",
    "&": "KEY_LEFTSHIFT:d:0#KEY_7:ud:%s#KEY_LEFTSHIFT:u:0",
    "(": "KEY_LEFTSHIFT:d:0#KEY_9:ud:%s#KEY_LEFTSHIFT:u:0",
    ")": "KEY_LEFTSHIFT:d:0#KEY_0:ud:%s#KEY_LEFTSHIFT:u:0",
    "*": "KEY_LEFTSHIFT:d:0#KEY_8:ud:%s#KEY_LEFTSHIFT:u:0",
    "+": "KEY_KPPLUS:ud:%s",
    ",": "KEY_COMMA:ud:%s",
    "-": "KEY_MINUS:ud:%s",
    ".": "KEY_DOT:ud:%s",
    "/": "KEY_SLASH:ud:%s",
    "0": "KEY_0:ud:%s",
    "1": "KEY_1:ud:%s",
    "2": "KEY_2:ud:%s",
    "3": "KEY_3:ud:%s",
    "4": "KEY_4:ud:%s",
    "5": "KEY_5:ud:%s",
    "6": "KEY_6:ud:%s",
    "7": "KEY_7:ud:%s",
    "8": "KEY_8:ud:%s",
    "9": "KEY_9:ud:%s",
    ":": "KEY_LEFTSHIFT:d:0#KEY_SEMICOLON:ud:%s#KEY_LEFTSHIFT:u:0",
    ";": "KEY_SEMICOLON:ud:%s",
    "<": "KEY_LEFTSHIFT:d:0#KEY_COMMA:ud:%s#KEY_LEFTSHIFT:u:0",
    "=": "KEY_EQUAL:ud:%s",
    ">": "KEY_LEFTSHIFT:d:0#KEY_DOT:ud:%s#KEY_LEFTSHIFT:u:0",
    "?": "KEY_QUESTION:ud:%s",
    "@": "KEY_LEFTSHIFT:d:0#KEY_2:ud:%s#KEY_LEFTSHIFT:u:0",
    "A": "KEY_LEFTSHIFT:d:0#KEY_A:ud:%s#KEY_LEFTSHIFT:u:0",
    "B": "KEY_LEFTSHIFT:d:0#KEY_B:ud:%s#KEY_LEFTSHIFT:u:0",
    "C": "KEY_LEFTSHIFT:d:0#KEY_C:ud:%s#KEY_LEFTSHIFT:u:0",
    "D": "KEY_LEFTSHIFT:d:0#KEY_D:ud:%s#KEY_LEFTSHIFT:u:0",
    "E": "KEY_LEFTSHIFT:d:0#KEY_E:ud:%s#KEY_LEFTSHIFT:u:0",
    "F": "KEY_LEFTSHIFT:d:0#KEY_F:ud:%s#KEY_LEFTSHIFT:u:0",
    "G": "KEY_LEFTSHIFT:d:0#KEY_G:ud:%s#KEY_LEFTSHIFT:u:0",
    "H": "KEY_LEFTSHIFT:d:0#KEY_H:ud:%s#KEY_LEFTSHIFT:u:0",
    "I": "KEY_LEFTSHIFT:d:0#KEY_I:ud:%s#KEY_LEFTSHIFT:u:0",
    "J": "KEY_LEFTSHIFT:d:0#KEY_J:ud:%s#KEY_LEFTSHIFT:u:0",
    "K": "KEY_LEFTSHIFT:d:0#KEY_K:ud:%s#KEY_LEFTSHIFT:u:0",
    "L": "KEY_LEFTSHIFT:d:0#KEY_L:ud:%s#KEY_LEFTSHIFT:u:0",
    "M": "KEY_LEFTSHIFT:d:0#KEY_M:ud:%s#KEY_LEFTSHIFT:u:0",
    "N": "KEY_LEFTSHIFT:d:0#KEY_N:ud:%s#KEY_LEFTSHIFT:u:0",
    "O": "KEY_LEFTSHIFT:d:0#KEY_O:ud:%s#KEY_LEFTSHIFT:u:0",
    "P": "KEY_LEFTSHIFT:d:0#KEY_P:ud:%s#KEY_LEFTSHIFT:u:0",
    "Q": "KEY_LEFTSHIFT:d:0#KEY_Q:ud:%s#KEY_LEFTSHIFT:u:0",
    "R": "KEY_LEFTSHIFT:d:0#KEY_R:ud:%s#KEY_LEFTSHIFT:u:0",
    "S": "KEY_LEFTSHIFT:d:0#KEY_S:ud:%s#KEY_LEFTSHIFT:u:0",
    "T": "KEY_LEFTSHIFT:d:0#KEY_T:ud:%s#KEY_LEFTSHIFT:u:0",
    "U": "KEY_LEFTSHIFT:d:0#KEY_U:ud:%s#KEY_LEFTSHIFT:u:0",
    "V": "KEY_LEFTSHIFT:d:0#KEY_V:ud:%s#KEY_LEFTSHIFT:u:0",
    "W": "KEY_LEFTSHIFT:d:0#KEY_W:ud:%s#KEY_LEFTSHIFT:u:0",
    "X": "KEY_LEFTSHIFT:d:0#KEY_X:ud:%s#KEY_LEFTSHIFT:u:0",
    "Y": "KEY_LEFTSHIFT:d:0#KEY_Y:ud:%s#KEY_LEFTSHIFT:u:0",
    "Z": "KEY_LEFTSHIFT:d:0#KEY_Z:ud:%s#KEY_LEFTSHIFT:u:0",
    "[": "KEY_LEFTBRACE:ud:%s",
    "\n": "KEY_ENTER:ud:%s",
    "\t": "KEY_TAB:ud:%s",
    "]": "KEY_RIGHTBRACE:ud:%s",
    "^": "KEY_LEFTSHIFT:d:0#KEY_6:ud:%s#KEY_LEFTSHIFT:u:0",
    "_": "KEY_LEFTSHIFT:d:0#KEY_MINUS:ud:%s#KEY_LEFTSHIFT:u:0",
    "`": "KEY_GRAVE:ud:%s",
    "a": "KEY_A:ud:%s",
    "b": "KEY_B:ud:%s",
    "c": "KEY_C:ud:%s",
    "d": "KEY_D:ud:%s",
    "e": "KEY_E:ud:%s",
    "f": "KEY_F:ud:%s",
    "g": "KEY_G:ud:%s",
    "h": "KEY_H:ud:%s",
    "i": "KEY_I:ud:%s",
    "j": "KEY_J:ud:%s",
    "k": "KEY_K:ud:%s",
    "l": "KEY_L:ud:%s",
    "m": "KEY_M:ud:%s",
    "n": "KEY_N:ud:%s",
    "o": "KEY_O:ud:%s",
    "p": "KEY_P:ud:%s",
    "q": "KEY_Q:ud:%s",
    "r": "KEY_R:ud:%s",
    "s": "KEY_S:ud:%s",
    "t": "KEY_T:ud:%s",
    "u": "KEY_U:ud:%s",
    "v": "KEY_V:ud:%s",
    "w": "KEY_W:ud:%s",
    "x": "KEY_X:ud:%s",
    "y": "KEY_Y:ud:%s",
    "z": "KEY_Z:ud:%s",
    "{": "KEY_LEFTSHIFT:d:0#KEY_LEFTBRACE:ud:%s#KEY_LEFTSHIFT:u:0",
    "}": "KEY_LEFTSHIFT:d:0#KEY_RIGHTBRACE:ud:%s#KEY_LEFTSHIFT:u:0",
    "|": "KEY_LEFTSHIFT:d:0#KEY_BACKSLASH:ud:%s#KEY_LEFTSHIFT:u:0",
    "~": "KEY_LEFTSHIFT:d:0#KEY_GRAVE:ud:%s#KEY_LEFTSHIFT:u:0",
    "ç": "KEY_LEFTALT:d:0#KEY_C:ud:%s#KEY_LEFTALT:u:0",
    "Ç": "KEY_LEFTSHIFT:d:0#KEY_LEFTALT:d:0#KEY_C:ud:%s#KEY_LEFTALT:u:0#KEY_LEFTSHIFT:u:0",
    "ß": "KEY_LEFTALT:d:0#KEY_S:ud:%s#KEY_LEFTALT:u:0",
    "ẞ": "KEY_LEFTSHIFT:d:0#KEY_LEFTALT:d:0#KEY_S:ud:%s#KEY_LEFTALT:u:0#KEY_LEFTSHIFT:u:0",
}


def random_function(minint, maxint):
    try:
        return random.randint(minint, maxint)
    except Exception:
        return minint


def create_sendkey_command(
    exefile, device_path, text, min_time_key_press, max_time_key_press
):
    min_time_key_press_int = int(min_time_key_press)
    max_time_key_press_int = int(max_time_key_press)
    commands = []
    for letter in text:
        commands.append(
            mappingdict[letter]
            % str(random_function(min_time_key_press_int, max_time_key_press_int))
        )
    return exefile + " " + device_path + " " + "#".join(commands)
