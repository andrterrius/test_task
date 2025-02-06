from random import choice
from config import code_letters

def code_generate(lenght=4) -> str:
    code_string = "".join(choice(code_letters) for _ in range(lenght))
    return code_string