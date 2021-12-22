

import webbrowser

# Open/create new html file in write mode
file_html = open('index.html', 'w')

# HTML code to put in the file
html_template = """
<html>
    <body>
        <h1>
    Stay tuned for our amazing summer
sale!
        </h1>
    </body>
</html>
"""

# Writes the code into the file
file_html.write(html_template)

# Closes the file
file_html.close()

# Opens file in browser
webbrowser.open('index.html')
