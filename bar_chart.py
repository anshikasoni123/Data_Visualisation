import pandas as pd
import plotly.express as px

df = pd.read_csv("corona_cases.csv")
fig = px.bar(df,x="date",y="cases",color = "country")
fig.show()