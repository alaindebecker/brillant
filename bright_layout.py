def row(*ui):
    ''' Lay out UI elements vertically.
        Forces all objects to have the same sizing_mode,
        which is required for complex layouts to work.
    '''
    html = '<div class="row">'
    for x in ui:
        html += f'{x}'
    return html+'</div>'


def column(*ui):
    ''' Lay out UI elements vertically.
        Forces all objects to have the same sizing_mode,
        which is required for complex layouts to work.
    '''
    html = '<div class="column">'
    for x in ui:
        html += f'{x}'
    return html+'</div>'


def layout(*rows):
    pass
        
