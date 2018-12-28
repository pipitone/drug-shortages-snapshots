#!/usr/bin/env python
# download and clean up shortages data drugshortagescanada.ca
#
# The site has no clean rest API for downloads so we use mechanize to simulate
# browser interaction
#
# The exported data is "CSV" but dirty. It has two heading rows, and includes
# two trailing heading rows for an empty "Discontinuations" table. The data is
# also indented.
#
# In addition, the site does not allow exports of greater than 3000 records, so 
# the exported CSV files contains contatenated exports. Sorry.
import httplib
import mechanize
import sys
SUBMIT_RETRIES = 3

data = []

br = mechanize.Browser()
br.open('https://www.drugshortagescanada.ca/search')

for year in range(2017,2021):
    for month in range(1,12):
        for retry in range(SUBMIT_RETRIES):
            try:
                br.select_form(nr=0)
                br['date_range[date_range_start][year]'] = [str(year)]
                br['date_range[date_range_end][year]'] = [str(year)]
                br['date_range[date_range_start][month]'] = [str(month)]
                br['date_range[date_range_end][month]'] = [str(month+1)]
                br['date_range[date_range_start][day]'] = ['1']
                br['date_range[date_range_end][day]'] = ['1']
                search_response = br.submit()
                br.select_form('export')
                br.submit()

                response = br.response().read()
                if "<html" in response: 
                    print("HTML response for Year {} Month {} record export".format(year, month))
                    print response
                    sys.exit()
                elif "Shortage reports" in response: 
                    # looks like CSV
                    lines = response.split("\n")
                    if len(lines) > 5: 
                        # not just headers
                        data.extend(lines)
                else: 
                    print("Unknown response read Year {} Month {} records".format(year, month))
                    print response
                    sys.exit()

                br.back()
            except (httplib.BadStatusLine, mechanize.HTTPError) as e:
                if retry == SUBMIT_RETRIES:
                    print("Attempt {}/{} failed.".format(retry, SUBMIT_RETRIES))
                    print(e)

if data:
    open('export.csv', 'w').write("\n".join(data))
