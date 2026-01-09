import streamlit as st
import plotly.express as px

def plot_debt(df):
    fig = px.line(df, x="Year", y="Debt_GDP", color="Scenario", title="Debt-to-GDP Path")
    st.plotly_chart(fig, use_container_width=True)

def plot_interest(df):
    fig = px.line(df, x="Year", y="Interest_GDP", color="Scenario", title="Interest Burden (% GDP)")
    st.plotly_chart(fig, use_container_width=True)
