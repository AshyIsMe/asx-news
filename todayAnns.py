import pandas as pd
from datetime import datetime

dfs = pd.read_html('https://www.asx.com.au/asx/v2/statistics/todayAnns.do')
if len(dfs) > 0:
    df = dfs[0]
    today = df['Date'].iloc[0]
    today = datetime.strptime(today, '%d/%m/%Y %I:%M %p').date().isoformat()
    df.to_csv(f"todayAnns_{today}.csv", index=False)

