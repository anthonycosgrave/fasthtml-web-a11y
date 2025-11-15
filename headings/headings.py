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

app = FastHTML(hdrs=(picolink, 
                     Link(rel="stylesheet", href="site.css"),
                     Link(rel="stylesheet", href="headings.css")), 
                     htmlkw={'lang':'en'}, 
                     title='Headings')

def latest_articles():
    return Article(
                H3(
                    A('Why Your Smart Fridge Is Ghosting You', href='#')
                ),
                P('It saw you drink straight from the carton.')
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
                    A('The Dark Side of Light-Based Nutrients', href='#')
                ),
                P('Can your food give you a tan AND anxiety?')
            )

def popular_posts():
    return Ul(
                Li(
                    Div(
                        A('Top 5 Budget Clones for Freelancers', href='#'), 
                        cls='popular-post-title'
                    ),
                    Small('Outsource your burnout to your face twin.')
                ),
                Li(
                    Div(
                        A('How to Date After the Neural Merge', href='#'), 
                        cls='popular-post-title'
                    ),
                    Small('Because love is weird when you share bandwidth.')
                ),
                Li(
                    Div(
                        A('MindFinance or ThinkBank?', href='#'), 
                        cls='popular-post-title'
                    ),
                    Small('We break down the latest in lobe-based lending.')
                ),
                Li(
                    Div(
                        A('What I Learned After Uploading Myself to a Smartwatch', href='#'), 
                        cls='popular-post-title'
                    ),
                    Small('Battery life is', Strong(' everything.'))
                )
            )

def popular_categories():
    return Ul(
                Li(
                    A('Technology', href='#')
                ),
                Li(
                    A('Existential Retail', href='#')
                ),
                Li(
                    A('MindFinancing', href='#')
                ),
                Li(
                    A('Ponchos', href='#')
                ),
                Li(
                    A('Bloat-o', href='#')
                ),
                cls='horizontal-list'
            )

def create_main():
    return Main(
                H1('Welcome To The Dunning-Kruger Dispatch!'), 
                P("Whether you're concerned your home appliances are trying to form a labour union or just want to browse the latest biometric poncho trends, we’ve got you covered! Our team of semi-certified contributors and algorithms work around the clock (because time is relative) to bring you the stories that almost matter. Dive in, read recklessly, share compulsively. ", Em("Truth is relative. Engagement is inevitable."),
                    H2('Latest Articles', id='latest-articles-heading'),
                    latest_articles(),
                    Aside(
                        H2('Popular Posts', id='popular-posts-heading'),
                        # Each *looks* like a heading element because of the sytling.
                        # None of them will appear in the screen reader elements list(s).
                        popular_posts(),
                    ),
                    Aside(
                        H2('Popular Categories', id='popular-categories-heading'),
                        popular_categories(),
                    )
                ),
            cls='container',
            id='main-content'
        )

@app.get("/")
def home():
    return create_header(), create_main(), create_footer()

@app.get("/{fname:path}.{ext:static}")
def static(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')

serve()