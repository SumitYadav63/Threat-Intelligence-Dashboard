import pandas as pd
import streamlit as st
import plotly.express as px

# Streamlit page settings
st.set_page_config(
    page_title="Threat Intelligence Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Matrix-style CSS
matrix_css = """
<style>
/* Matrix rain animation */
@keyframes matrixRain {
    0% { background-position: 0 0; }
    100% { background-position: 0 1000px; }
}

.stApp {
    background: repeating-linear-gradient(
        to bottom,
        rgba(0, 255, 0, 0.05) 0px,
        rgba(0, 255, 0, 0.05) 2px,
        transparent 2px,
        transparent 4px
    ),
    black;
    animation: matrixRain 10s linear infinite;
    color: #00ff00;
    font-family: 'Courier New', monospace;
}

h1, h2, h3, h4, h5 {
    color: #00ff00 !important;
}

[data-testid="stSidebar"] {
    background-color: rgba(0, 0, 0, 0.9);
}

.stDataFrame {
    background-color: #1a1d29;
    border: 1px solid #00ff00;
}

input, textarea {
    background-color: #1a1d29 !important;
    color: #00ff00 !important;
    border: 1px solid #00ff00 !important;
}
</style>
"""
st.markdown(matrix_css, unsafe_allow_html=True)

# Load CSV data
def load_data():
    return pd.read_csv("pulses.csv")

st.title("🛡️ Threat Intelligence Dashboard — Matrix Edition")

# Load and display data
data = load_data()
st.write(f"Total Pulses: {len(data)}")

# Show table
st.dataframe(data)

# Search/filter by pulse name
search_term = st.text_input("Search by Pulse Name")
if search_term:
    data = data[data['name'].str.contains(search_term, case=False, na=False)]
    st.write(f"Found {len(data)} result(s)")
    st.dataframe(data)

# Visualization: Pulses by Creation Date
if 'created' in data.columns:
    data['created'] = pd.to_datetime(data['created'], errors='coerce')
    pulses_by_date = data.groupby(data['created'].dt.date).size().reset_index(name='count')
    fig = px.line(
        pulses_by_date, 
        x='created', y='count', 
        title='📅 Pulses Over Time',
        template='plotly_dark',
        line_shape='spline',
        markers=True
    )
    st.plotly_chart(fig, use_container_width=True)

# Visualization: Top Contributors
if 'author_name' in data.columns:
    top_authors = data['author_name'].value_counts().head(10).reset_index()
    top_authors.columns = ['author', 'count']
    fig = px.bar(
        top_authors, 
        x='author', y='count', 
        title='🏆 Top 10 Pulse Contributors',
        template='plotly_dark',
        color='count'
    )
    st.plotly_chart(fig, use_container_width=True)
