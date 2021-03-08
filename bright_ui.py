from bright_layout import *


def header(text, level=0):
    if level==0:
        windowTitle = title
    return f'<h{level}>{text}</h{level}>'


def div(innerHTML):
    return f'<div>{innerHTML}</div>'


def well(innerHTML):
    return f'<div class="well">{innerHTML}</div>'


