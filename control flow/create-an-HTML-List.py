# Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list.

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

html_str = ["<ul>", "<li>first string</li>", "<li>second string</li>", "</ul>\n"]
for x in html_str:
    print(x)
