import urllib.request
import urllib.parse
import re
import youtube_dl

filedest = input("Please Enter your file name \n")
with open(filedest) as f:
    lines = f.readlines()
count = 0
while (count < len(lines)):
   query_string = urllib.parse.urlencode({'search_query' : lines[count]})
   html_content = urllib.request.urlopen('https://www.youtube.com/results?' + query_string)
   search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
   url = 'https://www.youtube.com/watch?v=' + search_results[0]
   print(url)
   ydl_opts = {}
   with youtube_dl.YoutubeDL(ydl_opts) as ydl:
   		ydl.download([url])
   count = count + 1

