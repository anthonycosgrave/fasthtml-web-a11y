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
from fasthtml.common import *
from fasthtml.svg import *

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
                        A('Home', href='/')
                    )
                ),
                Ul(
                    Li(
                        A('About', href='/about/')
                    ),
                    Li(
                        A('Shop', href='/shop/')
                    ),
                    Li(
                        A('Services', href='/services/')
                    ),
                    Li(
                        A('Podcast', href='/podcast/')
                    ),
                    Li(
                        A('Archive', href='/archive/')
                    ),
                    Li(
                        A('Contact', href='/contact/')
                    ),
                    Li(
                        create_search()
                    )
                ),
                aria_label="Primary"
            ),
            cls='header-wrap'
        ),
        cls='container'
    )

def create_footer():
    return Footer(
        Hr(),
        Nav(
            Ul(
                Li(
                    A('About', href='/about/')
                ),
                Li(
                    A('Services', href='/services/')
                ),
                Li(
                    A('LinkedIn', href='/linkedin/')
                ),
                Li(
                    A('Twitter', href='/twitter/')
                ),
                Li(
                    A('Mastodon', href='/mastodon/')
                ),
                Li(
                    A('Bluesky', href='/blueksy/')
                ),
                Li(
                    A('Contact', href='/contact/')
                ),
                Li(
                    A(
                        Svg(
                            Path(fill='currentColor', d='M 4 4.44 v 2.83 c 7.03 0 12.73 5.7 12.73 12.73 h 2.83 c 0 -8.59 -6.97 -15.56 -15.56 -15.56 Z m 0 5.66 v 2.83 c 3.9 0 7.07 3.17 7.07 7.07 h 2.83 c 0 -5.47 -4.43 -9.9 -9.9 -9.9 Z M 6.18 15.64 A 2.18 2.18 0 0 1 6.18 20 A 2.18 2.18 0 0 1 6.18 15.64'),
                            xmlns='http://www.w3.org/2000/svg',
                            viewbox='0 0 24 24',
                            height='16',
                            width='16',
                            cls='icon'
                        ),
                        href='/feed'
                    )
                )
            ),
            aria_label="Footer Links"
        ),
        P('© 2025 The Dunning-Kruger Dispatch - If you know, you know 😉'),
        style='text-align:center;',
        cls='container'
    )


def create_search():
    return Search(
        Input(
            type="search",
            placeholder="Search…",
            aria_label="Search",
            cls="search-input"
        )
)