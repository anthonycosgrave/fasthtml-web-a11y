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
from shared.components import create_footer, create_search

from fasthtml.common import *

app = FastHTML(hdrs=(picolink, 
                     Link(rel="stylesheet", href="site.css"), 
                     Link(rel="stylesheet", href="skip-link.css")), 
                     htmlkw={'lang':'en'}, 
                     title='Skip Links ')

def create_header():
    return Header(
        Div(
            A(
                Div(
                    Div (
                        Div('The Dunning-Kruger Dispatch', cls='site-title'),
                        cls='hero-content'
                    ),
                    cls='hero-section'
                ),
                href='/',
                style="text-decoration:none;"
            ),
            Nav(
                Ul(
                    Li(
                        A('Everything', href='/')
                    )
                ),
                Ul(
                    Li(A('Blog', href='/blog/')),
                    Li(A('Updates', href='/updates/')),
                    Li(A('Tutorials', href='/tutorials/')),
                    Li(A('Tools', href='/tools/')),
                    Li(A('Help', href='/help/')),      
                    Li(A('Events', href='/events/')),
                    Li(A('Knowledgebase', href='/knowledge/')),
                    Li(A('Insights', href='/insights/')),
                    Li(A('Tech', href='/tech/')),
                    Li(A('Community', href='/community/')),
                    Li(A('History', href='/history/')),
                    Li(A('E-books', href='/ebooks/')),
                    Li(A('News', href='/news/')),
                ),
                aria_label="Primary"
            ),
             Nav(
                Ul(
                   Li(A('Support', href='/support/')),
                    Li(A('Ideas', href='/ideas/')),
                    Li(A('Newsletter', href='/newsletter/')),
                    Li(A('Knowledge Hub', href='/knowledge-hub/')),
                    Li()
                ),
                create_search()
             ),
            cls='header-wrap'
        ),
        cls='container'
    )

def create_skip_link():
    return A(Strong('Skip to Jump!'), href='#the-skip', cls='skip-link'),


def latest_articles():
    return Article(
                H3(
                    A('Why Your Smart Fridge Is Ghosting You', href='#')
                ),
                P('It saw what you put in the butter drawer.')
            ), Article(
                H3(
                    A('How to Hack Your Sleep with Electro-Alpha Pillows™', href='#')
                ),
                P('Because who has time for REM cycles anymore?')
            ), Article(
                H3(
                    A('I Tried Bloat-o™ for 7 Days - Here\'s What Didn\'t Deflate', href='#')
                ),
                P('My stomach? No. My ego? Definitely.')
            ), Article(
               H3(
                    A('Is My Toothbrush Listening to Me?', href='#')
                ),
                P('Short answer: yes. Long answer: prepare for court.')
            ), Article(
                H3(
                    A('Recycling Your Emotions: A Guide to Eco-Friendly Angst', href='#')
                ),
                P('Cry once, reuse the tears.')
            ), Article(
                H3(
                    A('The Dark Side of Light-Based Nutrients', href='#')
                ),
                P('Can your food give you a tan AND anxiety?')
            )

def create_main():
    return Main(
             H1('Welcome To The Dunning-Kruger Dispatch!'), 
              P(
                  Strong("Trial re-design notice!")
              ),
               P( "In this experimental layout, we're monitoring how our keyboard-only users interact with our new '", Strong('N'), "avigation ", Strong('O'), "pen ", Strong('P'), "ossibilities ", Strong('E'), "xploration' system. ",
                 "While reports suggest they abandon the site entirely, we believe our content is just so good they'll just spend longer exhaustively ",
                "finding what they want."
                ),
                P(Em("So, dive in, read recklessly, share compulsively. Truth is relative. Engagement is inevitable."),
                    H2('Latest Articles', id='latest-articles-heading'),
                    latest_articles(),
                ),
            cls='container',
            id='main-content'
        )

@app.get("/")
def home():
    return Body(create_skip_link(), create_header(), create_main(), create_footer())

@app.get("/{fname:path}.{ext:static}")
def static(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')

serve()