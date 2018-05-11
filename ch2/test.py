from pandas import DataFrame ,Series
import pandas as pd;import numpy as np
f=open("C:\\Users\\huang\\Desktop\\python\\pydata-book-2nd-edition\\datasets\\bitly_usagov\\example.txt")
import json
records=[json.loads(line) for line in f]
frame =DataFrame(records)
tz_counts=frame['tz'].value_counts()

clean_tz=frame['tz'].fillna('Missing')
clean_tz[clean_tz==""]="UnKnown"
tz_counts=clean_tz.value_counts()
from pylab import *
tz_counts[:10].plot(kind="barh",rot=0)
show()
#print(tz_counts[:10])
results=Series(x.split()[0] for x in frame['a'].dropna())

#print(results.value_counts()[:8])
cframe=frame[frame.a.notnull()]
operating_system=np.where(cframe['a'].str.contains("Windows"),'Windows','Not Windows')
print(operating_system[:5])