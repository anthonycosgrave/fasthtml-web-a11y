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

app = FastHTML(hdrs=(picolink, 
                     Link(rel="stylesheet", href="site.css"), 
                     Link(rel="stylesheet", href="intro-to-acc-tree.css")), 
                     htmlkw={'lang':'en'}, 
                     title='Contact Us - The Dunning-Kruger Dispatch')

def create_contact_us_form():
    return Form(
                # Accessible Name = "Contact Us", Role = "heading", Level = "1"
                # The pencil icon is visible to sighted users but hidden from the accessibility tree and assistive technologies.
                H1(Span('✏️', aria_hidden='true'), 'Contact Us'),

                # The telephone icon is visible to screen readers and announced as 'telephone icon' which may be confusing to the user.
                # Role = "link", Accessible Name = "", Focusable = true
                P('📞 ', A('Alternatively, call us on +123-456-789', href='tel:+1234567890', type='tel')),

                P("Got feedback, fan theories, or an emotional outburst you'd like to share? Drop your thoughts below! We'd love to pretend we've read it."),

                # Label **explicitly** associated with the input via "for" (or "fr" in FastHTML).
                # Built-in accessibility benefit: clicking the label sets the focus on the associated input field.
                Label(Strong('Full Name'), fr='name'),
                # Accessible Name = "Full Name", Role = "textbox", Focusable = true.
                Input(type='text', id='name', name='name'),

                # Label **explicitly** associated with email input.
                # Built-in accessibility benefit: clicking the label sets the focus on the associated input field.
                Label(Strong('Email Address'), fr='email'),
                # Accessible Name = "Email Address", Role = "textbox", Focusable = true, Required = true, Description = "We require your email address in order to respond."
                Input(type='email', id='email', name='email', aria_describedby='email-desc', required='True'),
                # Div role = "generic" aka a "generic container" and so it is excluded from the accessibility tree.
                # Em (Emphasis) is an example of 'text-level semantics' and a screen reader might change its TTS sound for it.
                Div(P(Em('We require your email address in order to respond.'), id='email-desc')),

                # Standalone label (not associated with an input) and will not set focus on the comment textarea.
                P(Label(Strong('Your Comment'))),
                # This important information is not linked to the textarea, so unlike the email-desc text this won't
                # be announced to the user when the comment textarea has focus.
                # Em (Emphasis) is an example of 'text-level semantics' and a screen reader may change its TTS sound for it.
                P(Span(Em("Due to a Sentiment Suppression Protocol incident, we cannot process comments containing emojis."))),

                # No accessible name or description. Screen readers will probably announce it generically e.g., "edit multiline".
                # Accessible Name = "", Role="textbox", Focusable = true, Required = true. 
                Textarea(id='comment', name='comment', rows='6', required="True"),

                # Wrapping the checkbox in a label provides **implicit** association. In the accessibility tree you 
                # may see it as 'From label(wrapped): label "I want to receive your newsletter"'
                #
                # Built-in accessibility benefit: users can click the associated label to check or uncheck the checkbox.
                # This gives a larger surface area for people with mobility issues than having to hit the "bullseye" of 
                # a potentially small checkbox.
                #
                # Role = "checkbox", Accessible Name = "I want to receive your newsletter" (derived from the associated label), Focusable= true, Checked = true.
                P(Label(Input(type='checkbox', id='subscribe', name='subscribe', value='subscribed', checked='True'), 
                        Strong('I want to receive your newsletter'))),

                # Accessible Name = "Send Comment", 
                Div(Button('Send Comment', type='submit'))
            )

@app.get("/")
def home():
    return Main(create_contact_us_form(), cls='container')

@app.get("/{fname:path}.{ext:static}")
def static(fname:str, ext:str): return FileResponse(f'{fname}.{ext}')

serve()