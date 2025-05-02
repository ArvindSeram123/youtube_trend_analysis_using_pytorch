import streamlit as st
import pandas as pd
import os

# Load CSVs from data/raw/ folder
top_categories = pd.read_csv("data/output/top_categories/part1.csv")
title_keywords = pd.read_csv("data/output/title_keywords/part2.csv")
top_tags = pd.read_csv("data/output/top_tags/part3.csv")

# Display title of the app
st.title("YouTube Trending Data Analysis")

# Section 1: Show Top Categories
st.header("Top 10 Most-Viewed Categories")
st.write(top_categories)

# Section 2: Keyword Frequency in Video Titles
st.header("Top 20 Keywords in Video Titles")
st.write(title_keywords)

# Section 3: Top Tags
st.header("Top 20 Tags")
st.write(top_tags)

# Optional: Plotting data (for visualization)

# Visualizing Top Categories (Bar Chart)
st.subheader("Top Categories by Total Views")
st.bar_chart(top_categories.set_index('category')['total_views'])

# Visualizing Keywords (Bar Chart)
st.subheader("Top Keywords in Titles")
st.bar_chart(title_keywords.set_index('word')['count'])

# Visualizing Tags (Bar Chart)
st.subheader("Top Tags")
st.bar_chart(top_tags.set_index('tag')['count'])
