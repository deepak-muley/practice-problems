#import matplotlib libary
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.dates as mdates
import datetime as dt

username        = ''
passwd          = ''
doc_name        = 'Walkaholics'

import gdata.docs
import gdata.docs.service
import gdata.spreadsheet.service
import re, os

# Connect to Google
gd_client = gdata.spreadsheet.service.SpreadsheetsService()
gd_client.email = username
gd_client.password = passwd
gd_client.source = 'DMtestApp'
gd_client.ProgrammaticLogin()

q = gdata.spreadsheet.service.DocumentQuery()
q['title'] = doc_name
q['title-exact'] = 'true'
feed = gd_client.GetSpreadsheetsFeed(query=q)
spreadsheet_id = feed.entry[0].id.text.rsplit('/',1)[1]
feed = gd_client.GetWorksheetsFeed(spreadsheet_id)
worksheet_id = feed.entry[0].id.text.rsplit('/',1)[1]

rows = gd_client.GetListFeed(spreadsheet_id, worksheet_id).entry
xDate = []
yDeepakm = []
yChethan = []
yDeepakj = []
yPrashant = []
yVivek = []
yAlex = []
yShaheer = []
for row in rows:
   d = row.custom['date'].text
   if d is None:
      break
   d = dt.datetime.strptime(d, '%m/%d/%Y').date()
   xDate.append(d)
   yDeepakm.append(row.custom['deepakm'].text)
   yChethan.append(row.custom['chethan'].text)
   yAlex.append(row.custom['alex'].text)
   yPrashant.append(row.custom['prashant'].text)
   yDeepakj.append(row.custom['deepakj'].text)
   yVivek.append(row.custom['vivek'].text)
   yShaheer.append(row.custom['shaheer'].text)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

#plot data
plt.plot(xDate, yDeepakm, label= 'Deepakm', linewidth=2)
plt.plot(xDate, yChethan, label= 'Chethan', linewidth=2)
plt.plot(xDate, yAlex,    label= 'Alex', linewidth=2)
plt.plot(xDate, yPrashant,label= 'Prashant', linewidth=2)
plt.plot(xDate, yDeepakj, label= 'Deepakj', linewidth=2)
plt.plot(xDate, yVivek,   label= 'Vivek', linewidth=2)
plt.plot(xDate, yShaheer,   label= 'Shaheer', linewidth=2)
plt.legend()

plt.gcf().autofmt_xdate()

#show plot
plt.show()
