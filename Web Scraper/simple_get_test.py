from mathematicians import simple_get

raw_html = simple_get("https://www.realpython.com/blog")
count = len(raw_html)
print(count)