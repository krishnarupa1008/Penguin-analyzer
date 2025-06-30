import streamlit as st
from penguin_analyzer.data_loader import DataLoader
from penguin_analyzer.analyzer import PenguinAnalyzer
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
loader = DataLoader()
df = loader.load_data()

# Analyzer
analyzer = PenguinAnalyzer(df)

# Streamlit UI
st.title("Penguin Analysis Dashboard")

st.subheader("Species Count")
st.bar_chart(analyzer.species_counts())

st.subheader("Average Body Mass")
st.write(f"**{analyzer.average_body_mass():,.2f} g**")

# Select species
species = st.selectbox("Filter by species:", df['species'].unique())
filtered_df = analyzer.filter_by_species(species)
st.write(f"Showing {len(filtered_df)} rows for {species}")
st.dataframe(filtered_df)

# Optional: Show seaborn pairplot
if st.checkbox("Show Seaborn Pairplot"):
    st.write("Generating pairplot...")
    fig = sns.pairplot(filtered_df.dropna(), hue="species")
    st.pyplot(fig)
