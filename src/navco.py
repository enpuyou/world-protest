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

st.write(facet_byear_hist)
