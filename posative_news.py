# -*- coding: utf-8 -*-

!pip install pygooglenews

from pygooglenews import GoogleNews
import pandas as pd

gn = GoogleNews(lang='en', country="IE")

top = gn.top_news()

for i in top['entries']:
  L = (i.title + "\n")
  f = open("newslist.txt", "a")
  f.write(L)

with open("Triggerwords.txt", "r") as trigger_file:
    trigger_words = trigger_file.readlines()

with open("newslist.txt", "r") as news_file:
    news_lines = news_file.readlines()

# Create a list excluding the lines that contain the trigger words
filtered_lines = []
for line in news_lines:
    if not any(word.strip().lower() in line.lower() for word in trigger_words):
        filtered_lines.append(line)

with open("filtered_news.txt", "w") as output_file:
    output_file.writelines(filtered_lines)

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
# Creating a local hosted wesbite to displau the contents from the new file called filtered_news.txt for the user to view.
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}/filtered_news.txt")
    httpd.serve_forever()
