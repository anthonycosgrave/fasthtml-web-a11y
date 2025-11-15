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
                     Link(rel="stylesheet", href="keyboard-navigation.css")), 
                     htmlkw={'lang':'en'}, 
                     title='Keyboard Navigation and Focus Indicator')

def create_identity_subscription():
    # Device Dependent Functionality!
    # relies on mouse functionality to reveal information
    return Fieldset(
        Legend('Identity & Subscription'),
        Label(
            'Name',
            Span(
                Span('ℹ'),
                data_tooltip='For the sake of future data breaches do not use your full legal name!',
                data_placement='right'
            ),
            fr='name'
        ),
        Input(type='text', id='name', name='name'),
        Label('Email',
              Span(
                Span('ℹ'),
                data_tooltip='MindMail Connect owners use your @neuro.net or @cortexmail.biz addresses!',
                data_placement='right'
            ),
            fr='email'
        ),
        Input(type='email', id='email', name='email'),
        Label('Subscription Tier', fr='tier'),
        # Select:
        # TAB in, SPACE expands (then arrows) OR arrows navigate without expanding, TAB/SHIFT+TAB out
        Select(
            Option('Select your desired tier', value=''),
            Option('Compliance Preview (Ad-Supported, Lagging Truth)'),
            Option('Engagement Plus (Includes Emotion Tracking)'),
            Option('Priority Access (Reduced Redactions, Some Regret)'),
            Option('Omnivault Member (Full Archive, No Questions Asked)'),
            Option('Executive Override (Real-Time Edits, Retroactive Authority)'),
            id='tier',
            name='tier'
        ),
        Fieldset(
            # Radio group:
            # TAB in, arrow keys navigate, TAB/SHIFT+TAB out
            Legend('Preferred Validation Method'),
            Label(
                Input(type='radio', name='auth', value='comments', checked=''),
                'Verified via Legacy Comment History'
            ),
            Label(
                Input(type='radio', name='auth', value='facecloud'),
                'Verified via Sentiment Profile (FaceCloud Mood Sync Required)'
            ),
            Label(
                Input(type='radio', name='auth', value='loan'),
                'Verified via ThinkBank or MindFinance Prefrontal Loan History'
            )
        )
    )

def create_autoforward():
    return Fieldset(
        # Checkboxes: 
        # TAB/SHIFT+TAB (Each gets own tab stop), SPACE toggles, no arrow key navigation
        Legend('Which headlines would you auto-forward to your 13 closest acquaintances?'),
        Label(
            Input(type='checkbox', name='autoforward', value='bird'),
            'Birdwatching App Quietly Maps Dissidents'
        ),
        Label(
            Input(type='checkbox', name='autoforward', value='ads'),
            'Scientists Confirm Some Thoughts Are Just Ads'
        ),
        Label(
            Input(type='checkbox', name='autoforward', value='soul'),
            '8 Ways to Charge Your Soul Using Lasagna - #5 Will Shock You!'
        ),
        Label(
            Input(type='checkbox', name='autoforward', value='sleep'),
            'Sleep Trackers caught selling dream data to marketing firms'
        ),
        Label(
            Input(type='checkbox', name='autoforward', value='loser'),
            "None - I don't have any friends"
        )
    )

def create_engagement_metrics():
    return Fieldset(
        Legend('Content Consumption'),
        Label('Average hours exposed to algorithmic content (per day)', fr='contentHours'),
        Input(type='number', id='contentHours', name='contentHours', min='0', max='24', value='12'),
        Label('Number of current active browser tabs', fr='tabs'),
        Input(type='number', id='tabs', name='tabs', min='0')
    )

def create_belief_flexibility():
    return Fieldset(
        Legend("In the phrase 'Of course that's what they want you to believe!'"),
        Label("In your opinion, who exactly are ", Strong(Em("they")), "?", fr='justification'),
        Textarea(id='justification', name='justification', rows='4', placeholder="We know you've done your research...")
    )

def create_secret_discount_code():
    # Device Dependent Functionality!
    # requires mouse hover to reveal information to the user.
    return Section(
        H2('Bonus Secret New Subscriber Discount Code!'),
        P(
            Em('Hover your mouse to reveal!')
        ),
        Div(
            Span('Use ', Strong('FOMOBOOST17'),' for 17% off your pre-sale merch queue reserveration slot holding privileges.', Em(' Everyone else is doing it!')),
            cls='hover-box'
        ),
        id='hoverTrap',
        cls='container'
    )

def create_notification_frequency():
    # Not an accessibility issue, more of a usability/UX issue. It
    # demonstrates overall interaction expectations and inefficiency.
    # Previous radio buttons were 1 TAB stop and then arrow keys.
    # Different names break grouping so arrow keys won't work here,
    # user must TAB to each.
    return Fieldset(
        Legend('How frequently would you prefer not to avoid being occassionally notified?'),
        Label(
            Input(type='radio', name='daily', value='daily'),  
            'Daily Spam Digest'
        ),
        Label(
            Input(type='radio', name='weekly', value='weekly'),
            'Weekly Mind Melt'
        ),
        Label(
            Input(type='radio', name='surprise', value='surprise'),
            'Surprise Me'
        ),
        Label(
            Input(type='radio', name='never', value='never'),
            'Never (Coward Mode)'
        )
    )

def create_subscriber_form():
    return Form(
        # mouse dependent functionality info icon
        create_identity_subscription(),
        create_autoforward(),
        # multiple tabs required for radio buttons
        create_notification_frequency(),
        create_engagement_metrics(),
        create_belief_flexibility(),
        # The *really* contrived mouse dependent functionality
        create_secret_discount_code(),
        P(Button('Submit for Algorithmic Review', type='submit')),
        Section(
            H4('Data Compliance Statement'),
            P(
                Em('By starting to read this you have agreed that all material contained herein is the proprietary content of "The Dunning-Kruger Dispatch", a subsidiary of the Bureau of Temporal Narratives. Use, reproduction, or interpretation of such material is subject to ongoing revision, retroactive clarification, and legally ambiguous oversight.')
            )
        )
    )

def create_main():
    return Main(
        H1('Subscribe!'),
        P(
            Em('Complete this form to harmonise your profile with our agentic insight agents across the cognitive cloud.')
        ),
        create_subscriber_form(),
        cls='container', 
        id='main-content'
    )

@app.get("/")
def home():
    return Body(create_header(), create_main(), create_footer())

@app.get("/{fname:path}.{ext:static}")
def static(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')

serve()