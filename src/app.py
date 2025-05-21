import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


st.title('Gapminder')
st.write("BIPM Project - Unlocking Lifetimes: Visualizing Progress in Longevity and Poverty Eradication ")
# Constants
data_path = Path(__file__).parent.parent / "data" / "processed" / "merged_gapminder.csv"

@st.cache_data
def load_data():
    """Load and cache the preprocessed Gapminder data."""
    df = pd.read_csv(data_path)
    return df

# Load data
df = load_data()

# Prepare controls
years = sorted(df['year'].unique())
countries = sorted(df['country'].unique())

st.title("Gapminder Bubble Chart Dashboard")

# Sidebar widgets
st.sidebar.header("Controls")
selected_countries = st.sidebar.multiselect(
    label="Select Countries",
    options=countries,
    default=countries[:5]
)

# Filter data
filtered_df = df[df['country'].isin(selected_countries)]

# Determine global x-axis range (log-scale)
gni_min, gni_max = df['gniPPP'].min(), df['gniPPP'].max()

# Create animated scatter plot
fig = px.scatter(
    filtered_df,
    x="gniPPP",
    y="lifeExp",
    size="population",
    color="country",
    hover_name="country",
    log_x=True,
    size_max=60,
    animation_frame="year",
    animation_group="country",
    range_x=[gni_min, gni_max],
    range_y=[df['lifeExp'].min(), df['lifeExp'].max()]
)

fig.update_layout(
    title="Life Expectancy vs. GNI per Capita over Time",
    xaxis_title="GNI per Capita (log scale, PPP)",
    yaxis_title="Life Expectancy",
    legend_title="Country"
)

# Render plot
st.plotly_chart(fig, use_container_width=True)

# Footer with copyright
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-size: 12px; color: gray;'>© 2025 Richard Quansah</div>", unsafe_allow_html=True)


