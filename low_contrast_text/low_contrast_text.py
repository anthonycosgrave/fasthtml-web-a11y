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
                     Link(rel="stylesheet", href="low-contrast-text.css")), 
                     htmlkw={'lang':'en'}, 
                     title='Focus Endurance Squad')

def create_main():
    return Main(
        Header(H1('Challenging readability one pixel at a time', cls='squinters-delight')),
 Section(
    H2('Welcome, Focus Endurance Squad!'),
    P(
        'Here at ',
        Strong('The Dunning-Kruger Dispatch'),
        ', we know there are those among you who want to work to decipher every character on a page. You want to ',
        Em('earn'),
        ' your content. Some might accuse us of forcing people to spend longer reading so we can serve you more ads. We prefer to think of it as increasing engagement through atmospheric opacity.'
    ),
    P(
        "Our colour palette has been curated for users who understand that reading should feel like a mental HIIT workout. Letters shouldn't just be seen - they should be ",
        Em('pursued'),
        ', ',
        Em('considered'),
        ', and finally ',
        Em('perceived'),
        " after a moment of doubt. If you're skimming, you're doing it wrong."
    ),
    P(
        "We don’t just write content. We conceal it like treasure. Thinking of copying a useful quote or snipping a stat to share? Maybe you’re not the kind of reader we’re designing for. Our most committed users don't need to ",
        Em('see'),
        ' highlighted text when they drag their mouse - they remember it by heart. Muscle memory is the new clipboard. After all, if your audience can ',
        Em('easily'),
        ' select and share your words, were they ever worth remembering?'
    ),
    cls='squinters-delight'
),
Section(
    H2('Too Readable? Too Easy!'),
    P(
        Em('The following section is fully readable. Proceed with caution.')
    ),
    P("We get it. Not everyone’s here for the challenge. Some readers just want to… read. Without squinting. Without tilting their screen 17 degrees. With the adreinaline rush of reading fast enough before the cloud cover passes and natural sunlight reflects off their glossy screen. And for those folks, we’ve introduced what the industry calls “compliant” contrast. It’s crisp. It’s clear. It’s, frankly, a bit embarrassing."),
    P('Sure, this text passes WCAG AAA. But where’s the growth? Where’s the strain? You’ll never build retinal endurance like this. But if you’re into ease, comfort, and reading with both eyes open - well, go ahead. Take the shortcut.'),
    H3('*sigh* You Probably Want To See What You’re Copying Too'),
    P('At this level of contrast, selection isn’t a gamble, it’s a gift! When you highlight this text, you actually see what you’re selecting. It’s a radical move, we know. But sometimes L-users just want to copy a quote without needing to divine it from the ether. We hear most browsers actually provide a high contrast version for *free* (LOL!) if you let them.'),
    P("It's not edgy. It's not exclusive. In fact, it’s what some might call “helpful.”. If digging for information felt like treasure hunting, this is more like picking it up off the floor. We don't get it. We're not even sure if we respect it..."),
    cls='aaa-champion'
),
Section(
    H2('Subscribe Now!'),
    P('Still using "readable" colours? That’s adorable. Real readers demand more. Ready to level up your visual stamina? These palettes aren’t for casual browsers. They’re for visual athletes at the top of their game. These are for the people who want to invade their monitor\'s personal space and whisper "What does that say?!".'),
    P('These aren’t just styles...they’re trials!'),
    P(
        'Subscribe for early access to ',
        Span('Clash Pop!', cls='clash-pop'),
        ', ',
        Span('CONCRETE FOG', cls='concrete-fog'),
        ', ',
        Span('Burnout EnErGy!', cls='burnout-energy'),
        ', and ',
        Span('VampirE', cls='vampire'),
        '- the four horsemen of eye-watering, retina-stressing colourways designed to test the truly committed.'
    ),
    P(
        'Refer 5 friends and once *they* subscribe *you* will receive our exclusive ',
        Span('FOMO', cls='fomo'),
        'colour palette.'
    ),
    cls='squinters-delight'
),
Section(
    H2('Need a little help there buddy?'),
    P(
        'Not everyone can jump right into ',
        Span('CONCRETE FOG', cls='concrete-fog'),
        '. We get that. Some journeys begin with a sweaty walk, not a sprint. That’s why The Dunning-Kruger Dispatch now includes a beginner’s contrast palette in our "training wheels" package. Enough to meet WCAG AA requirements but with enough visual friction to feel like you’re doing something. Infact you\'re seeing it right now!'
    ),
    P('It’s the perfect choice for aspiring readability warriors who still want to earn their content — just without the migraines. Think of it as interval training for your corneas: text you can read, but not too fast.'),
    P("We don't offer friends referral deals for training wheels. You probably don't have any anyhow."),
    cls='aa-level'
),
cls='container')

@app.get("/")
def home():
    return create_header(), create_main(), create_footer()

@app.get("/{fname:path}.{ext:static}")
def static(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')

serve()