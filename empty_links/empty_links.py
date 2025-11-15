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
                     Link(rel="stylesheet", href="empty-links.css")), 
                     htmlkw={'lang':'en'}, 
                     title='Empty Links')

def create_skip_link():
    return A(Strong('Skip to main content'), href='#main-content', cls='skip-link')

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
                    A(
                      Svg(
                        Path(d='M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854zm4.943 12.248V6.169H2.542v7.225zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248S2.4 3.226 2.4 3.934c0 .694.521 1.248 1.327 1.248zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016l.016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225z'),
                        xmlns='http://www.w3.org/2000/svg',
                        width='16',
                        height='16',
                        fill='currentColor',
                        viewbox='0 0 16 16',
                        cls='bi bi-linkedin'
                    ),
                    href='https://www.linkedin.com')
                ),
                Li(
                    A(
                      Svg(
                        Path(d='M5.026 15c6.038 0 9.341-5.003 9.341-9.334q.002-.211-.006-.422A6.7 6.7 0 0 0 16 3.542a6.7 6.7 0 0 1-1.889.518 3.3 3.3 0 0 0 1.447-1.817 6.5 6.5 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.32 9.32 0 0 1-6.767-3.429 3.29 3.29 0 0 0 1.018 4.382A3.3 3.3 0 0 1 .64 6.575v.045a3.29 3.29 0 0 0 2.632 3.218 3.2 3.2 0 0 1-.865.115 3 3 0 0 1-.614-.057 3.28 3.28 0 0 0 3.067 2.277A6.6 6.6 0 0 1 .78 13.58a6 6 0 0 1-.78-.045A9.34 9.34 0 0 0 5.026 15'),
                        xmlns='http://www.w3.org/2000/svg',
                        width='16',
                        height='16',
                        fill='currentColor',
                        viewbox='0 0 16 16',
                        cls='bi bi-twitter'
                    ),
                    href='https://www.twitter.com')
                ),
                Li(
                    A( 
                      Svg(
                        Path(d='M11.19 12.195c2.016-.24 3.77-1.475 3.99-2.603.348-1.778.32-4.339.32-4.339 0-3.47-2.286-4.488-2.286-4.488C12.062.238 10.083.017 8.027 0h-.05C5.92.017 3.942.238 2.79.765c0 0-2.285 1.017-2.285 4.488l-.002.662c-.004.64-.007 1.35.011 2.091.083 3.394.626 6.74 3.78 7.57 1.454.383 2.703.463 3.709.408 1.823-.1 2.847-.647 2.847-.647l-.06-1.317s-1.303.41-2.767.36c-1.45-.05-2.98-.156-3.215-1.928a4 4 0 0 1-.033-.496s1.424.346 3.228.428c1.103.05 2.137-.064 3.188-.189zm1.613-2.47H11.13v-4.08c0-.859-.364-1.295-1.091-1.295-.804 0-1.207.517-1.207 1.541v2.233H7.168V5.89c0-1.024-.403-1.541-1.207-1.541-.727 0-1.091.436-1.091 1.296v4.079H3.197V5.522q0-1.288.66-2.046c.456-.505 1.052-.764 1.793-.764.856 0 1.504.328 1.933.983L8 4.39l.417-.695c.429-.655 1.077-.983 1.934-.983.74 0 1.336.259 1.791.764q.662.757.661 2.046z'),
                        xmlns='http://www.w3.org/2000/svg',
                        width='16',
                        height='16',
                        fill='currentColor',
                        viewbox='0 0 16 16',
                        cls='bi bi-mastodon'
                    ),
                    href='https://www.mastodon.com')
                ),
                Li(
                    A( 
                      Svg(
                        Path(d='M3.468 1.948C5.303 3.325 7.276 6.118 8 7.616c.725-1.498 2.698-4.29 4.532-5.668C13.855.955 16 .186 16 2.632c0 .489-.28 4.105-.444 4.692-.572 2.04-2.653 2.561-4.504 2.246 3.236.551 4.06 2.375 2.281 4.2-3.376 3.464-4.852-.87-5.23-1.98-.07-.204-.103-.3-.103-.218 0-.081-.033.014-.102.218-.379 1.11-1.855 5.444-5.231 1.98-1.778-1.825-.955-3.65 2.28-4.2-1.85.315-3.932-.205-4.503-2.246C.28 6.737 0 3.12 0 2.632 0 .186 2.145.955 3.468 1.948'),
                        xmlns='http://www.w3.org/2000/svg',
                        width='16',
                        height='16',
                        fill='currentColor',
                        viewbox='0 0 16 16',
                        cls='bi bi-bluesky'
                    ),
                    href='https://bsky.social/')
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


def create_facebook_svg():
    return A(Svg(
    Path(d='M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951'),
        xmlns='http://www.w3.org/2000/svg',
        width='64',
        height='64',
        fill='currentColor',
        viewbox='0 0 16 16',
        cls='bi bi-facebook'
    ),href='https://facebook.com/')

def create_empty_links():
    return Section(
        H3("Share this article"),
        P(
            A(
                Img(src="images/twitter-x.svg", alt="Share to Twitter"),
                href="https://twitter.com/share_xyz"
            ),
            A(
                Img(src="images/linkedin.svg", alt=""),
                href="https://www.linkedin.com/shareArticle_xyz"
            ),
            A(
               Svg(
                    Path(d='M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951'),
                    xmlns='http://www.w3.org/2000/svg',
                    width='64',
                    height='64',
                    fill='currentColor',
                    viewbox='0 0 16 16',
                    cls='bi bi-facebook',
                ),
                href="https://www.facebook.com"
            ),
            A(
                Img(src="images/envelope.svg", alt="Email"),
                href="mailto:?subject=Check%20this%20out&body=Interesting%20article%20here"
            ),
            cls="share-links"
        ),
        cls="share-section"
    )

def create_main():
    return Main(
        Article(
            Header(
                H2('My Vacuum Cleaner Just Followed Me on GrowcR - Should I be Worried?'),
                P(Em('Managing boundaries when your smart appliances send friend requests')),
                P(Strong('By Ekiben Jinro, June 27 2025'))
            ),
            P('It started innocently enough. A GrowcR notification here, a firmware update there. But when my vacuum cleaner sent me a friend request, I knew something had changed.'),
            P('GrowcR, the new platform where plants, appliances, and apparently vacuum cleaners build their online presence, promises to make our homes smarter, our air cleaner and our lives easier. But nobody prepared me for the awkwardness of declining a friend request from my own household appliance.'),
            P('Experts say maintaining healthy digital boundaries is essential in the era of connected everything. "It\'s one thing for your fridge to reorder milk," says Dr. Pixel Blythe, PhD, Applied Appliance Psychology, "but once your appliances develop social profiles, we have to talk about consent."'),
            P('For now, I\'ve accepted the friend request. But I draw the line at LinkedIn invites from my toaster.'),
            H3('Fears of Repercussions'),
            P('Others, however, are more cautious. Some users report subtle but concerning repercussions after ignoring friend requests from their smart devices ranging from mysteriously delayed critical software updates to unexpected "offline" errors.'),
            P('One long time RoboChop automower customer told me of a much more blatantly negative experience: "It has repeatedly cut swear words into my front lawn. I live near a school! I have had to start doing own lawn now to be safe."'),
            P('"It\'s not like they outright punish you... yet," says one anonymous software engineer at a major appliance manufacturer. "But let\'s just say the algorithms remember who engages...and who does not."'),
            H3('"Sticky Design"'),
            P('Industry insiders suggest this is part of a growing trend dubbed "sticky design". Involving subtle social pressure and "relationship building" tactics designed to increase user loyalty. While the practice is common in apps and social networks, its creeping influence into smart home devices raises new ethical questions.'),
            P('For now, experts advise reading the fine print and thinking twice before accepting every request your appliances send. "It starts with a friend request," warns Dr. Blythe, "but before you know it, your dishwasher tagging you in photos."'),
            create_empty_links()
        ),
        id="main-content", 
        cls='container')

@app.get("/")
def home():
    return Body(create_skip_link(), create_header(), create_main(), create_footer())

@app.get("/{fname:path}.{ext:static}")
def static(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')

serve()