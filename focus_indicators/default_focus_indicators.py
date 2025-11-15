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

app = FastHTML(pico=False,
               hdrs=(Link(rel="stylesheet", href="site.css"), 
                     Link(rel="stylesheet", href="skip-link.css"), 
                     Link(rel="stylesheet", href="layout.css"),
                     Link(rel="stylesheet", href="focus-indicator.css")
                     ), 
                     htmlkw={'lang':'en'}, 
                     title='Focus Indicators'
                )


def create_skip_link():
    return A(Strong('Skip to main content'), href='#main-content', cls='skip-link'),

def create_form():
    return Form(
                P(
                    Label('Username', fr='name'),
                    Input(type='text', id='name', name='name', placeholder='Enter username', required='')
                ),
                P(
                    Label("Select a new password:", _for="password-select"),
                    Select(
                        Option("Select a new password...", value="", selected=True),
                        # Hack The Planet ;-)
                        Option("love", value="love"),
                        Option("s3x", value="s3x"),
                        Option("secret", value="secret"),
                        Option("God", value="God"),
                        id="password-select",
                        name="password",
                        style="width: 100%; padding: 0.75rem;"
                    )
                ),
                P(
                    Fieldset(
                        Legend('Username Flare'),
                        Label(
                            Input(type='radio', name='flare', value='class', required=''),
                            'Too Classy For Class Action'
                        ),
                        Label(
                            Input(type='radio', name='flare', value='trail'),
                            'Post-Trust Trailblazer'
                        ),
                        Label(
                            Input(type='radio', name='flare', value='royalty'),
                            'Password Reset Royalty'
                        )
                    )
                ),
                Div (
                    Label(
                        Input(type='checkbox', name='consent', required=''),
                        'I acknowledge that any irregularities detected post-reset will be attributed to end-user actions.',
                        cls='checkbox-label'
                    ),
                    
                ),
                Div(
                    Button('Submit', type='submit', cls='primary'),
                    Button('Cancel', type='button', cls='secondary'),
                    cls='grid'
                ),
            method='post',
            id="main-content"
        )

def create_main():
    return Main(
        H1('We Had a Little Oopsie!'),
        P('Here at The Dunning-Kruger Dispatch, we believe in a “glass-half-full-every-cloud-has-a-silver-lining-litigation-minimising” approach to life.'),
        P('So when we discovered some "lemons" in the form of a silly little file containing subscriber names, card details, and maybe some biometric hints that had wandered onto the open internet, we thought: "Time to make some lemonade!"'),
        P( 'That\'s why we\'re offering a', Strong(' complimentary no-strings-attached credential refresh'), '!'),
        P('After all, who has time for encryption? Are all those weird characters really even your data? At least now you can look through that file and proudly exclaim: "Hey! There I am! I am on the internet!'),
        H2("Courtesy Credential Refresh"),
        P("Please re-enter your username, choose a new password, and pick the flare you'd like to display next to your name."),
        create_form(),
        P(Small('This remediation flow does not constitute legal admission, nor should it be construed as an apology. By using this form, you waive the right to participate in class-action lawsuits in any jurisdiction still recognising digital personhood.')),
        cls='container', 
        id='main-content'
    )

@app.get("/")
def home():
    return Body(create_skip_link(), create_header(), create_main(), create_footer())

@app.get("/{fname:path}.{ext:static}")
def static(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')

serve()