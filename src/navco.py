import streamlit as st
import pandas as pd
import altair as alt


def import_navco(path):
    data = pd.read_csv(path)
    st.write(data)
    return data


navco_df = import_navco("NAVCO1.3/navco_list.csv")

byear_hist = alt.Chart(
    navco_df).mark_bar().encode(
        alt.X("BYEAR", bin=alt.Bin(step=10)),
        y="count()",
        color="LOCATION",
        opacity=alt.value(0.7),
        tooltip=[
            alt.Tooltip("LOCATION", title="Location"),
            alt.Tooltip("CAMPAIGN", title="Campaign"),
            alt.Tooltip("BYEAR", title="Begin year"),
            alt.Tooltip("EYEAR", title="End year"),
            ],
        ).properties(height=1000, width=1000)

# st.altair_chart(byear_hist)

facet_byear_hist = alt.Chart(navco_df).mark_bar().encode(
    alt.X("BYEAR", bin=alt.Bin(step=10)),
    y="count()",
    facet=alt.Facet('LOCATION', columns=6),
).properties(
    title='Campaign by Location',
    width=90,
    height=80
)

# st.write(facet_byear_hist)

# source = data.wheat()
#
# base = alt.Chart(source).encode(x='year:O')
#
# bar = base.mark_bar().encode(y='wheat:Q')
#
# line =  base.mark_line(color='red').encode(
#     y='wages:Q'
# )
#
# (bar + line).properties(width=600)


base = alt.Chart(navco_df).encode(alt.Y("LOCATION"))

byear_dot = base.mark_point(color="blue").encode(
        alt.X("BYEAR", scale=alt.Scale(domain=(1900, 2020)))
        )

eyear_dot = base.mark_point(color="red").encode(
        alt.X("EYEAR", scale=alt.Scale(domain=(1900, 2020))))

combine = (byear_dot + eyear_dot).properties(
    title='Begin Year and End Year',
    width=1000,
    height=1000
)

st.write(combine)
