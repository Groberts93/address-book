# %%
import report
import pandas as pd
# %%

addr_all = pd.read_csv('./csv/christmas.csv')
# %%

card_data = report.series_to_carddata(addr_all.iloc[11])
# %%

card = report.Card(card_data)
# %%
cardstr = card.generate()
# %%
print(cardstr)
# %%
import re
if re.findall('\d+', 'Night 0232'):

    print('found it')
# %%
