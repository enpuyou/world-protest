import streamlit as st
import pandas as pd
import altair as alt

navco_df = pd.read_csv("NAVCO1.3/navco_list.csv")
st.write(navco_df)

hist = alt.Chart(
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

st.altair_chart(hist)
