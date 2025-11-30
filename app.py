import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="MedTourEasy Analytics", layout="wide")

@st.cache_data
def load_and_clean_data():
    try:
        df = pd.read_csv('appointments.csv')
        
        df['Appointment_Date'] = pd.to_datetime(df['Appointment_Date'], errors='coerce')
        
        df.dropna(subset=['Visit_Status'], inplace=True)
        
        df.drop_duplicates(inplace=True)
        
        df = df[df['Billing_Amount'] >= 0]
        
        return df
    except FileNotFoundError:
        st.error("Dataset not found. Please run generate_data.py first.")
        return pd.DataFrame()

# --- 2. PREPROCESSING & FEATURE ENGINEERING  ---
def preprocess_data(df):
    if df.empty:
        return df
    
    df['Hour'] = df['Appointment_Date'].dt.hour
    df['Day_of_Week'] = df['Appointment_Date'].dt.day_name()
    
    def get_time_slot(hour):
        if 6 <= hour < 12: return 'Morning'
        elif 12 <= hour < 17: return 'Afternoon'
        else: return 'Evening'
    
    df['Time_Slot'] = df['Hour'].apply(get_time_slot)
    
    return df

# --- MAIN APP EXECUTION ---
raw_df = load_and_clean_data()
df = preprocess_data(raw_df)

if not df.empty:
    st.sidebar.image("https://img.icons8.com/color/96/000000/hospital-2.png", width=80)
    st.sidebar.title("Filters")
    
    branch_filter = st.sidebar.multiselect(
        "Select Branch:", 
        options=df['Branch'].unique(),
        default=df['Branch'].unique()
    )
    
    dept_filter = st.sidebar.multiselect(
        "Select Department:",
        options=df['Department'].unique(),
        default=df['Department'].unique()
    )
    
    df_filtered = df.query("Branch == @branch_filter & Department == @dept_filter")

    st.title("Healthcare Appointment Analytics Dashboard")
    st.markdown("### Operational Insights & KPI Monitoring")
    st.markdown("---")

    total_appointments = len(df_filtered)
    total_revenue = df_filtered['Billing_Amount'].sum()
    avg_duration = df_filtered[df_filtered['Consultation_Duration'] > 0]['Consultation_Duration'].mean()
    
    cancel_count = len(df_filtered[df_filtered['Visit_Status'] == 'Cancelled'])
    noshow_count = len(df_filtered[df_filtered['Visit_Status'] == 'No-Show'])
    cancel_rate = (cancel_count / total_appointments * 100) if total_appointments else 0
    noshow_rate = (noshow_count / total_appointments * 100) if total_appointments else 0

    kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)
    kpi1.metric("Total Appointments", total_appointments)
    kpi2.metric("Total Revenue", f"₹{total_revenue:,.0f}")
    kpi3.metric("Avg Duration", f"{avg_duration:.1f} min")
    kpi4.metric("Cancellation Rate", f"{cancel_rate:.1f}%")
    kpi5.metric("No-Show Rate", f"{noshow_rate:.1f}%")

    st.markdown("---")

    # --- 4. VISUALIZATION (EDA) [cite: 373, 375, 389, 399] ---
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Appointments by Department")
        fig1, ax1 = plt.subplots()
        dept_counts = df_filtered['Department'].value_counts()
        ax1.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')  
        st.pyplot(fig1)

    with col2:
        st.subheader("Appointments by Branch")
        fig2, ax2 = plt.subplots()
        sns.countplot(data=df_filtered, x='Branch', palette='viridis', ax=ax2)
        plt.xticks(rotation=45)
        st.pyplot(fig2)

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Visit Status Distribution")
        fig3, ax3 = plt.subplots()
        sns.countplot(data=df_filtered, x='Visit_Status', palette='pastel', ax=ax3)
        st.pyplot(fig3)

    with col4:
        st.subheader("Peak Hour Analysis (Heatmap)")
        heatmap_data = df_filtered.pivot_table(index='Day_of_Week', columns='Hour', values='Patient_ID', aggfunc='count', fill_value=0)
        days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        heatmap_data = heatmap_data.reindex(days_order)
        
        fig4, ax4 = plt.subplots(figsize=(10, 6))
        sns.heatmap(heatmap_data, cmap="YlGnBu", annot=True, fmt="d", ax=ax4)
        st.pyplot(fig4)

    # --- DATASET VIEW  ---
    with st.expander("View Raw Data"):
        st.dataframe(df_filtered)