from bright_ui import *
import webbrowser


def head(title=''):
    html =  '<!DOCTYPE html><html><head><meta charset="utf-8">'
    html += f'<title>{title}</title>'
    html += '''<style>
                * {font-family: sans-serif; }
                html, body { width: 100%; height: 100%; }
                .row { display: flex; flex-direction: row; width: 100%; }
                .row > * {flex: 1 1 0; }
                .column { display: flex; flex-direction: column; }
                .column { flex: 1 1 0 }

               .well { background: whitesmoke; border: 1px solid lightgrey; border-radius: 4px; margin-bottom: 20px; padding: 9px}

            </style></head><body>
            '''
    return html

    
def save(html, file=None):
    file = file or 'bright.html'
    with open(file, 'w') as f:
         f.write(head()+html+'</body></html>')
    return file

def show(html, file=None):
    webbrowser.open(save(html, file))
