# Web Accessibility Examples with FastHTML

A collection of introductory web accessibility examples built with FastHTML, demonstrating **intentionally broken** and **bad** web accessibility for educational purposes to demonstrate common accessibility pitfalls and their impacts on people.

These examples accompany blog posts available at [Web Accessibility with FastHTML](https://anthonycosgrave.github.io/fasthtml-web-a11y) (licensed under CC BY 4.0).

Examples are tested with NVDA and Windows Narrator, though the underlying accessibility principles apply across all screen readers including [MacOS VoiceOver](https://support.apple.com/en-ie/guide/voiceover/welcome/mac) and [Job Access With Speech (JAWS)](https://www.freedomscientific.com/products/software/jaws/). User experience may vary slightly due to platform-specific APIs.

## Requirements

- Python 3.10+
- [FastHTML](https://www.fastht.ml/docs/)
- Screen reader (for some examples): 
    - [NVDA](https://www.nvaccess.org/download/)
    - [Windows Narrator (built into Windows)](https://support.microsoft.com/en-us/windows/complete-guide-to-narrator-e4397a0d-ef4f-b386-d8ae-c172f109bdb1)
    - [Job Access With Speech (JAWS)](https://www.freedomscientific.com/products/software/jaws/)
    - [VoiceOver (built into MacOS and iOS)](https://support.apple.com/en-ie/guide/voiceover/welcome/mac) 

## Installation

1. Clone this repository
2. Create a virtual environment: `python3 -m venv venv`
3. Activate it: `source venv/bin/activate` (Linux/WSL/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`

## Running Examples

Each example is self-contained. 

1. Navigate into a directory and run: `python <filename>.py`
2. Open up your browser to the URL shown in the terminal (typically http://localhost:5001).
3. For examples that involve a screen reader, ensure your screen reader is running **before interacting with the page**.

## License

Code is licensed under the MIT License. See LICENSE file for details.