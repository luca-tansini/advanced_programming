#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 -- [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def sort(url_list):
    if(re.search(r'-\w*-\w*.jpg',url_list[0])):
        return sorted(url_list, key = lambda x: re.search(r'-\w*-(\w*).jpg',x).group(1))
    else:
        return sorted(url_list)

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  match = re.search(r'.*_(.*)',filename)
  hostname = match.group(1)
  urls = set()
  for l in open(filename):
      match = re.search(r'GET (\S*puzzle\S*) HTTP',l)
      if(match):
          urls.add("http://"+hostname+match.group(1))
  return sort(list(urls))

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  try:
      os.mkdir(dest_dir)
  except FileExistsError as e:
      pass
  i = 0
  for url in img_urls:
      print("Retrieving "+url+" ...")
      img = urllib.request.urlopen(url)
      f = open(dest_dir+'/img'+str(i)+'.jpg','wb')
      f.write(img.read())
      f.close()
      i+=1
  html = open(dest_dir+'/index.html','w')
  html.write('<verbatim>\n<html>\n<body>\n')
  for i in range(len(img_urls)):
      html.write('<img src="img'+str(i)+'.jpg">')
  html.write('\n<body>\n</html>\n')
  html.close()

def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
