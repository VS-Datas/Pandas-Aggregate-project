import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

ad_clicks.head()
print(ad_clicks.head())

views_each = ad_clicks.groupby('utm_source').user_id.count().reset_index()

print(views_each)

is_click = ad_clicks.ad_click_timestamp.apply(lambda ad_click_timestamp: True if ad_click_timestamp != 0 else False).reset_index()

#print(is_click) 

clicks_by_source = ad_clicks\
.groupby(['utm_source','is_click'])\
.user_id.count().reset_index()

print(clicks_by_source)

clicks_pivot = ad_clicks.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
  ).reset_index()

print(clicks_pivot)

clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False])

print(ad_clicks.groupby('experimental_group').user_id.count().reset_index() 
  )
  

print(ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index().pivot(
  columns = 'experimental_group',
  index = 'is_click',
  values = 'user_id'
  ).reset_index()
)

a_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'A']

b_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'B']   
a_clicks_pivot = ad_clicks.groupby(['day', 'is_click']).user_id.count().reset_index().pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()

a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True] / \
   (a_clicks_pivot[True] + 
    a_clicks_pivot[False])

a_clicks_pivot = ad_clicks.groupby(['day', 'is_click']).user_id.count().reset_index().pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()

b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True] / \
   (b_clicks_pivot[True] + 
    b_clicks_pivot[False])














