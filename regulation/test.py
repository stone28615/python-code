import re
ptn = re.compile(r"\w+?@\w+?\.com")

matched = ptn.search("mofan@mofanpy.com")
print("mofan@mofanpy.com is a valid email:", matched)
matched = ptn.search("mofan@mofanpy+com")
print("mofan@mofanpy+com is a valid email:", matched)
print("hello?")