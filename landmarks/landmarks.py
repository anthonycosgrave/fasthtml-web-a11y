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
# import sys
# sys.path.append('..')
# from shared.components import create_header, create_footer
from elements import create_header, create_footer
from fasthtml.common import *

app = FastHTML(hdrs=(picolink, 
                     Link(rel="stylesheet", href="site.css"),
                     Link(rel="stylesheet", href="landmarks.css")), 
                     htmlkw={'lang':'en'}, 
                     title='Landmarks')

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

def popular_posts():
    return Ul(
                Li(
                   H3(
                        A('I Sold My Memories for Crypto - Here\'s What I Think I Remember', href='#')
                    ),
                    Small('Possibly a win. Or a bagel. Hard to say.')
                ),
                Li(
                    H3(
                        A('How to Date After the Neural Merge', href='#')
                    ),
                    Small('Because love is weird when you share bandwidth.')
                ),
                Li(
                    H3(
                        A('Top 5 Budget Clones for Freelancers', href='#')
                    ),
                    Small('Outsource your burnout to your face twin.')
                ),
                Li(
                    H3(
                        A('Confessions of a Sentient Toaster', href='#')
                    ),
                    Small('A brave tale of crumbs and consciousness.')
                ),
                Li(
                    H3(
                        A('What I Learned After Uploading Myself to a Smartwatch', href='#')
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
                        popular_posts(),
                    ),
                    Div(
                        H2('Popular Categories', id='popular-categories-heading'),
                        popular_categories(),
                        aria_labelledby='popular-categories-heading'
                    )
                ),
            cls='container',
            id='main-content'
        )

@app.get("/")
def home():
    return Body(
        create_header(), 
        create_main(), 
        create_footer()
    )

@app.get("/{fname:path}.{ext:static}")
def static(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')

serve()