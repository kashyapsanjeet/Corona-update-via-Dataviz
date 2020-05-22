import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

df=pd.read_html('https://www.mohfw.gov.in/')
data=df[0]

fp = "Igismap/Indian_States.shp"
map_df = gpd.read_file(fp)
frame=pd.DataFrame()
c1=data.columns[2]

frame['State_name']=data['Name of State / UT']
frame['cases']=data[c1]
frame['cured']=data['Cured/Discharged/Migrated']
frame['death']=data['Death']

frame.loc[0,'State_name']='Andaman & Nicobar Island'
frame.loc[12,'State_name']='Jammu & Kashmir'
frame.loc[2,'State_name']='Arunanchal Pradesh'
frame.loc[27,'State_name']='Telangana'
frame.loc[16,'State_name']='Sikkim'

frame.drop(31,axis=0,inplace=True)
frame.drop(32,axis=0,inplace=True)
frame.drop(33,axis=0,inplace=True)
frame.drop(34,axis=0,inplace=True)

frame=frame.append(pd.Series(['Lakshadweep',0,0,0],index=frame.columns),ignore_index=True)
frame=frame.append(pd.Series(['Nagaland',0,0,0],index=frame.columns),ignore_index=True)
frame=frame.append(pd.Series(['Dadara & Nagar Havelli',0,0,0],index=frame.columns),ignore_index=True)
frame=frame.append(pd.Series(['Daman & Diu',0,0,0],index=frame.columns),ignore_index=True)

merged = map_df.set_index('st_nm').join(frame.set_index('State_name'))
merged['cases']=merged.cases.astype('str')
fig, ax = plt.subplots(1, figsize=(20, 10))
ax.axis('off')
ax.set_title('Corona virus cases in India', fontdict={'fontsize': '25', 'fontweight' : '3'})
merged.plot(column='cases', cmap='YlOrRd', linewidth=1.2, ax=ax, edgecolor='0.8', legend=True)
leg = ax.get_legend()
leg.set_bbox_to_anchor((1.2, 1, 0, 0))
plt.show()