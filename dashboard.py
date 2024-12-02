import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data(csv_path='output/influencer_report.csv'):
    """Load influencer data."""
    try:
        data = pd.read_csv(csv_path)
        
        # Add a full path column for images
        data['image_path'] = data['representative_image']
        
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# Streamlit app
st.title("Influencer Performance Dashboard")


# Load the data
report_df = load_data()

# If the data is empty or not loaded, return early
if report_df.empty:
    st.error("No data to display")
else:
    # Display performance data
    st.header("Performance Report")
    st.write(report_df)

    # Ensure required columns exist
    required_columns = ['avg_performance', 'Unnamed: 0', 'image_path']
    if not all(col in report_df.columns for col in required_columns):
        st.error(f"Required columns {required_columns} are missing.")
    else:
        # Display influencer images and performance details
        st.header("Influencer Profiles")
        
        # Create columns for compact display
        cols = st.columns(3)  # 3 columns per row
        
        for i, (_, row) in enumerate(report_df.iterrows()):
            # Use modulo to cycle through columns
            col = cols[i % 3]
            
            with col:
                st.subheader(f"{row['Unnamed: 0']}")  # Influencer name
                
                # Check if image exists and is valid
                if pd.notna(row['image_path']) and os.path.exists(row['image_path']):
                    st.image(row['image_path'], 
                             caption=f"Avg Performance: {row['avg_performance']:.2f}", 
                             width=200)  # Reduced image width
                else:
                    st.warning(f"No image found for {row['Unnamed: 0']}")

        # Visualization: Average Performance
        st.header("Average Performance by Influencer")
        fig, ax = plt.subplots(figsize=(10, 6))
        report_df.sort_values(by='avg_performance', ascending=False).plot.bar(
            x='Unnamed: 0', y='avg_performance', ax=ax
        )
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(fig)