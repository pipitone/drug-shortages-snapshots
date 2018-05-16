#!/usr/bin/env python
# download and clean up shortages data drugshortagescanada.ca
#
# The site has no clean rest API for downloads so we use mechanize to simulate
# browser interaction
#
# The exported data is "CSV" but dirty. It has two heading rows, and includes
# two trailing heading rows for an empty "Discontinuations" table. The data is
# also indented. We clean all this up. 
#
import httplib
import mechanize
SUBMIT_RETRIES = 3

br = mechanize.Browser()

for i in range(SUBMIT_RETRIES):
    try:
        br.open('https://www.drugshortagescanada.ca/search')
        br.select_form('export')
        br.submit()
        open('export.csv', 'w').write(br.response().read())
        print("Export complete after {}/{} attempts.".format(i+1, SUBMIT_RETRIES))
        break
    except (httplib.BadStatusLine, mechanize.HTTPError) as e:
        print("Attempt {}/{} failed.".format(i, SUBMIT_RETRIES))
        print(e)

