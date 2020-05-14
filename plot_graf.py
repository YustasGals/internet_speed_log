#!/usr/bin/env python3
# vim: set ai et ts=4 sw=4: 

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
 
file = r'st.csv'
file2 = r'st2.csv' 
#columns = ['Server ID','Sponsor','Server Name','Timestamp','Distance','Ping','Download','Upload','Share','IP Address'] 
data  = pd.read_csv(file, sep=',', header=0) #, names=columns)
data['Timestamp'] = pd.to_datetime(data['Timestamp']) #, format='%Y%m%d')
del data['Server ID'] 
del data['Sponsor']
del data['Server Name']
del data['Share']
del data['IP Address']
#print(data)
df =    pd.read_csv(file2, sep=',', header=0) #, names=columns) 
df['Timestamp'] = pd.to_datetime(df['Timestamp']) #, format='%Y%m%d')
del df['Server ID'] 
del df['Sponsor']
del df['Server Name']
del df['Share']
del df['IP Address']

if not 1 : 
    fig, ax = plt.subplots(nrows=4, ncols=1, figsize=(16, 9))
    data.plot(y="Ping", ax=ax[0])
    data.plot(y="Download", ax=ax[1])
    data.plot(y="Upload", ax=ax[2])
    data.plot(y="Distance", x='Timestamp', ax=ax[3])
else :
    data.plot(subplots=True, figsize=(16, 9));

df.plot(subplots=True, figsize=(16, 9));

plt.savefig('fig.png', transparent=False, dpi=96, bbox_inches="tight")



plt.show()


