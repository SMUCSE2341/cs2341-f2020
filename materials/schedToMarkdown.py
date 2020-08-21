####################################################### 
# 
# Needs to have pytablewriter installed
# Currently set up in the CS1340 conda env
# 
####################################################### 


from pytablewriter import MarkdownTableWriter
import pyexcel as p
import json

#data = get_data("schedule.ods")

records = p.get_records(file_name="schedule.ods")
print(type(records))

for r in records:
  print (r)

writer = MarkdownTableWriter()
writer.