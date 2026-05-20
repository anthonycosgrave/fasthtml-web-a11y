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
                     Link(rel="stylesheet", href="site.css"), 
                     Link(rel="stylesheet", href="skip-link.css"), 
                     Link(rel="stylesheet", href="accessible-text-descriptions.css")), 
                     htmlkw={'lang':'en'}, 
                     title='Accessible Text Descriptions')

def create_skip_link():
    return A(Strong('Skip to main content'), href='#main-content', cls='skip-link')

def create_divider():
    return  Svg(
                Text('$', x='4', y='8', font_size='12', font_weight='700', fill='#c0392b', font_family='monospace'),
                Text('€', x='36', y='6', font_size='10', font_weight='700', fill='#8e44ad', font_family='monospace'),
                Text('£', x='68', y='8', font_size='12', font_weight='700', fill='#2980b9', font_family='monospace'),
                Text('¥', x='100', y='6', font_size='10', font_weight='700', fill='#27ae60', font_family='monospace'),
                Text('$', x='132', y='8', font_size='12', font_weight='700', fill='#c0392b', font_family='monospace'),
                Text('€', x='164', y='6', font_size='10', font_weight='700', fill='#8e44ad', font_family='monospace'),
                Text('£', x='196', y='8', font_size='12', font_weight='700', fill='#2980b9', font_family='monospace'),
                Text('¥', x='228', y='6', font_size='10', font_weight='700', fill='#27ae60', font_family='monospace'),
                Text('$', x='260', y='8', font_size='12', font_weight='700', fill='#c0392b', font_family='monospace'),
                Text('€', x='292', y='6', font_size='10', font_weight='700', fill='#8e44ad', font_family='monospace'),
                Text('£', x='324', y='8', font_size='12', font_weight='700', fill='#2980b9', font_family='monospace'),
                Text('¥', x='356', y='6', font_size='10', font_weight='700', fill='#27ae60', font_family='monospace'),
                Text('$', x='388', y='8', font_size='12', font_weight='700', fill='#c0392b', font_family='monospace'),
                Text('€', x='420', y='6', font_size='10', font_weight='700', fill='#8e44ad', font_family='monospace'),
                Text('£', x='452', y='8', font_size='12', font_weight='700', fill='#2980b9', font_family='monospace'),
                Text('¥', x='484', y='6', font_size='10', font_weight='700', fill='#27ae60', font_family='monospace'),
                Text('$', x='516', y='8', font_size='12', font_weight='700', fill='#c0392b', font_family='monospace'),
                Text('€', x='548', y='6', font_size='10', font_weight='700', fill='#8e44ad', font_family='monospace'),
                Text('£', x='580', y='8', font_size='12', font_weight='700', fill='#2980b9', font_family='monospace'),
                Text('¥', x='612', y='6', font_size='10', font_weight='700', fill='#27ae60', font_family='monospace'),
                Text('$', x='644', y='8', font_size='12', font_weight='700', fill='#c0392b', font_family='monospace'),
                width='100%',
                viewbox='0 0 680 20',
                cls='divider'
            )

def create_main():
    return Main(
        Header(
            H1('QuantumYield AI Exclusive - Outperform reality itself!'),
        ),
        P(
            'A Dispatch reader exclusive offer! Join potentially thousands of forward-thinking investors already leveraging AI-powered quantum forecasting to accelerate wealth beyond traditional financial expectations.'
        ),
        P(
           create_divider()
        ),
        Section(
            H2('Meet the creator: ', Em('Trent Velocity')),
            P(
                'A man whose thinking is so out of the box that, MIT and NASA eggheads described QuantumYield as ', Em('"mathematically concerning!"'), ', ', 
                Strong('Trent Velocity'), 
                ' founded QuantumYield AI after reportedly predicting three consecutive cryptocurrency rebounds using only motivational podcasts clips and a lava lamp.'
            ),
            Div(
                Figure(
                    Img(
                        # credit: Photo by Kampus Production: https://www.pexels.com/photo/man-in-black-suit-jacket-sitting-on-chair-while-pointing-his-finger-8353809/
                        src="/images/trent-velocity.jpg",
                        alt=(
                            "a man"
                        )
                    ),
                    Figcaption(
                        'QuantumYield AI founder Trent Velocity during a live market intuition session.'
                    )
                ),
                Div(
                    P(
                        'Since pivoting from Metaverse real estate investment, Trent has become a leading voice in quantum wealth acceleration and emotionally aware investing.'
                    ),
                    P(
                        'Trusted by disruptive wealth architects in over 14 unregulated markets (or maybe you like playing by the rules!).'
                    ),
                    P(
                        'A regular speaker at premium quantum fintech conferences, often speaking on panels like:',
                        Ul(
                            Li(Em('How To Scale Your Wealth Narratives')),
                            Li(Em('Adapting Responsive Synergistic Exponetial Holes')),
                            Li(Em('From Side Hustle to Quantum Revenue Architecture')),
                            Li(Em('A Life Beyond Conventional Percentages'))
                        )
                    ),
                    P(
                        'In 2025, Trent was presented with an award from prestigious The Velocity Institute (pictured below)',
                        Br(),
                        Image(src='images/trent-velocity-real-investment-award.png')
                    )
                )
            )
        ),
        P(
            create_divider()
        ),
        Section(
            H2('Exclusive DKD Reader Access'),
            P(
                'Due to overwhelming investor enthusiasm, discounted Enterprise Vision Suite memberships are only available for a limited time. Use the promotional code below now!'
            ),
            Img(
                src='images/promo.png',
            )
        ),
        P(
            create_divider()
        ),
        Section(
            H2('Market Dominating Growth Metrics'),
            P(
                'The following chart demonstrates potential exponential market dominance that Trent Velocity guarantees.'
            ),
            Svg(
                Title(
                    'QuantumYield projected revenue growth',
                    id='chart-title'
                ),

                Desc(
                    'Bar chart showing revenue growth increasing from a small bar in January to a much bigger bar in March.',
                    id='chart-desc'
                ),

                Text('Growth Projection', x='20', y='30'),

                Text('January', x='20', y='80'),
                Rect(x='120', y='60', width='40', height='20'),

                Text('February', x='20', y='120'),
                Rect(x='120', y='100', width='120', height='20', fill='#2980b9'),

                Text('March', x='20', y='160'),
                Rect(x='120', y='140', width='320', height='20', fill='#27ae60'),

                role='img',
                aria_labelledby='chart-title chart-desc',
                width='500',
                height='220'
            ),
            P(
                'These bars could be yours!'
            )
        ),
        P(
            create_divider()
        ),
        Section(
            H2('Velocity Institute Adaptive Forecast Layer™'),
            P('VIAFL is built on proprietary and scalable forecasting architecture, the system provides a real-time synthesis of predictive investment signals, narrative modelling and targeted trajectories.'),
            P('Unlike traditional financial analysis, VIAFL prioritises ', Em('potential future certainty states'), ' allowing shrewd investors to act on outcomes before they have fully stabilised into observable reality.'),
            P('As a result, the following table should not be interpeted as a reflection of ', Strong('current'), ' market conditions, but an early expression of what the conditions are becoming!'),
            Details(
                Summary(
                    Img(
                        src='images/viafl-marketing.png',
                        alt='Invest Wealth Future. Give Trent Velocity All Of Your Money Now. Full description below.'
                    ),
                    Span('View full description')
                ),
                P(
                    'This image is a table showing performance data for several initiatives within a QuantumYield AI system.',
                    ' The table includes multiple columns and rows containing different words and values. The data appears to', 
                    ' represent performance information for each initiative. The image is likely used to present structured',
                    ' information in a visual format.'
                ),
                cls="image-disclosure"
            ),
        ),
        P(
            create_divider()
        ),
        Section(
            H2('What early adopters are saying on our social network GrowcR:'),
            Ul(
                Li(
                    Div(
                        Img(src='images/profile-1.jpg', alt='https://dkd.grwcr_img.com.test/growcr_profile_img/2053872642562609152/',
                            cls='growcr-profile-img'),
                        Div(
                            Strong('@CryptoDad247'),
                            P('QuantumYield AI completely transformed my thought leadership journey.'),
                            cls='growcr-text'
                        ),
                        style='display:grid; grid-template-columns:65px 1fr; gap:12px;'
                    ),
                    cls='growcr-msg'
                ),
                Li(
                    Div(
                        # Photo by Daniel Xavier: https://www.pexels.com/photo/man-wearing-shield-sunglasses-1195109/
                        Img(
                            src='images/profile-2.png', 
                            alt=' ',
                            cls='growcr-profile-img'
                        ),
                        Div(
                            Strong('@DisruptionViking'),
                            P('Wow. Just Wow. Massive paradigm acceleration. Bravo!'),
                            cls='growcr-text'
                        ),
                        style='display:grid; grid-template-columns:65px 1fr; gap:12px;'
                    ),
                    cls='growcr-msg'
                ),
                Li(
                    Div(
                        # Photo by khezez  | خزاز: https://www.pexels.com/photo/businesswoman-in-modern-office-meeting-room-35730231/
                        Img(src='images/profile-3.png', cls='growcr-profile-img'),
                        Div(
                            Strong('@GrowthMindsetCEO'),
                            P('Trent Velocity helped me think beyond traditional arithmetic.'),
                            cls='growcr-text'
                        ),
                        style='display:grid; grid-template-columns:65px 1fr; gap:12px;'
                    ),
                    cls='growcr-msg'
                ),
                style='list-style:none; padding:0; margin:0;'
            )
        ),
        id='main-content',
        cls='container'
    )

@app.get("/")
def home():
    return Body(create_skip_link(), create_header(), create_main(), create_footer())

@app.get("/{fname:path}.{ext:static}")
def static(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')

serve()