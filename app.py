import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(page_title="Fyra Map Application", page_icon="🗺️", layout="wide")

# Title and description
st.title("🗺️ Fyra Map Application")
st.markdown("Welcome to the Fyra map application built with Streamlit!")

# Create sample data for the map
@st.cache_data
def load_map_data():
    """Generate sample location data for the map"""
    # Create random coordinates around a central location (e.g., Stockholm, Sweden)
    np.random.seed(42)
    n_points = 100
    
    # Stockholm coordinates: 59.3293° N, 18.0686° E
    center_lat = 59.3293
    center_lon = 18.0686
    
    # Generate random points within approximately 10km radius
    df = pd.DataFrame({
        'lat': center_lat + np.random.randn(n_points) * 0.05,
        'lon': center_lon + np.random.randn(n_points) * 0.05,
        'size': np.random.randint(10, 100, n_points),
        'category': np.random.choice(['A', 'B', 'C'], n_points)
    })
    
    return df

# Load the data
data = load_map_data()

# Sidebar controls
st.sidebar.header("Map Controls")
show_data = st.sidebar.checkbox("Show raw data", value=False)
filter_category = st.sidebar.multiselect(
    "Filter by category",
    options=['A', 'B', 'C'],
    default=['A', 'B', 'C']
)

# Filter data based on selection
filtered_data = data[data['category'].isin(filter_category)]

# Display the map
st.subheader("📍 Interactive Map")
st.map(filtered_data[['lat', 'lon']], size=10, color='#0066ff')

# Display statistics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Points", len(filtered_data))
with col2:
    st.metric("Average Size", f"{filtered_data['size'].mean():.1f}")
with col3:
    st.metric("Categories", len(filter_category))

# Optionally show the raw data
if show_data:
    st.subheader("📊 Raw Data")
    st.dataframe(filtered_data, use_container_width=True)

# Add some information
st.markdown("---")
st.markdown("""
### About this application
This is a demonstration Streamlit application featuring an interactive map.
The map shows randomly generated data points around Stockholm, Sweden.

**Features:**
- Interactive map visualization
- Sidebar controls for filtering data
- Real-time statistics
- Option to view raw data

Built with ❤️ using Streamlit and UV package manager.
""")
