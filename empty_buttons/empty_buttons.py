# =========================================================
# DEMO CODE NOTICE:
# This code is for demonstration purposes only.
# It is not intended for production use and may include:
#   - Intentional accessibility violations
#   - Incomplete validation
#   - Unoptimised logic or structure
#   - Weak attempts to be "funny"
# We know you know this already, but y'know, just in case.
# =========================================================
import sys
sys.path.append('..')
from shared.components import create_header, create_footer
from fasthtml.common import *
from fasthtml.svg import *

app = FastHTML(hdrs=(picolink, 
                     Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.13.1/font/bootstrap-icons.min.css"),
                     Link(rel="stylesheet", href="site.css"), 
                     Link(rel="stylesheet", href="skip-link.css"), 
                     Link(rel="stylesheet", href="empty-buttons.css")), 
                     htmlkw={'lang':'en'}, 
                     title='Empty Buttons')

def create_skip_link():
    return A(Strong('Skip to main content'), href='#main-content', cls='skip-link')

def create_form_with_empty_buttons():
    return Form(
            Label('Everyone wants to read what YOU have to say!', fr='post-content'),
            Textarea(id='post-content', placeholder='Enter illuminating insights...'),
            Div(
                Div( 
                    Button(I(cls='bi bi-send'), type='submit'),
                    Button(
                        Svg(
                            Path(d='M11 2H9v3h2z'),
                            Path(d='M1.5 0h11.586a1.5 1.5 0 0 1 1.06.44l1.415 1.414A1.5 1.5 0 0 1 16 2.914V14.5a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 0 14.5v-13A1.5 1.5 0 0 1 1.5 0M1 1.5v13a.5.5 0 0 0 .5.5H2v-4.5A1.5 1.5 0 0 1 3.5 9h9a1.5 1.5 0 0 1 1.5 1.5V15h.5a.5.5 0 0 0 .5-.5V2.914a.5.5 0 0 0-.146-.353l-1.415-1.415A.5.5 0 0 0 13.086 1H13v4.5A1.5 1.5 0 0 1 11.5 7h-7A1.5 1.5 0 0 1 3 5.5V1H1.5a.5.5 0 0 0-.5.5m3 4a.5.5 0 0 0 .5.5h7a.5.5 0 0 0 .5-.5V1H4zM3 15h10v-4.5a.5.5 0 0 0-.5-.5h-9a.5.5 0 0 0-.5.5z'),
                            xmlns='http://www.w3.org/2000/svg',
                            width='32',
                            height='32',
                            fill='currentColor',
                            viewbox='0 0 16 16',
                            cls='bi bi-floppy'
                        ),
                        type='button'
                    ),
                    Button(
                        Svg(
                            Path(d='M4.5 3a2.5 2.5 0 0 1 5 0v9a1.5 1.5 0 0 1-3 0V5a.5.5 0 0 1 1 0v7a.5.5 0 0 0 1 0V3a1.5 1.5 0 1 0-3 0v9a2.5 2.5 0 0 0 5 0V5a.5.5 0 0 1 1 0v7a3.5 3.5 0 1 1-7 0z'),
                            xmlns='http://www.w3.org/2000/svg',
                            width='32',
                            height='32',
                            fill='currentColor',
                            viewbox='0 0 16 16',
                            cls='bi bi-paperclip'
                        ),
                        type='button'
                    ),
                    Button(
                        Img(src='/bootstrap/icons/trash.svg', width='32', height='32'),
                        type='button'
                    ),
                    cls='left-buttons'
                ),
                cls='toolbar'
                ),
        )

def create_main():
    return Main(H1('Welcome to Noyzee!'), 
        P(
            'As outlined on page 573 of the Terms & Conditions we\'re sure you definitely read before you agreed to them, ', 
            Strong('DAILY'), ' posts on our Noyzee social network are ', Strong('mandatory'), '.', 
            cls='container'
        ),
        P(
            'To help you generate some meaningful noyz, here are the Top 4 medical, scientific, or geopolitical noyzeez our beloved Noyzeers are confidently and considerately dissecting this week:'
        ),
        Ol(
            Li(Em("Time was created to sell more watches! #BigTimeBigCrime")),
            Li(Em("Allergic Reaction or just rejecting The Matrix?!")),
            Li(Em("Sovereign debt restructuring - who gets to rewrite the rules of recovery? Should it be Scooby Doo?")),
            Li(Em("Are you wasting REM cycles? Trade in your sleep #DozeCoin"))
        ),
        create_form_with_empty_buttons(),
        cls='container',
        id="main-content"
        )

@app.get("/")
def home():
    return Body(create_skip_link(), create_header(), create_main(), create_footer())
      
@app.get("/{fname:path}.{ext:static}")
def static(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')

serve()