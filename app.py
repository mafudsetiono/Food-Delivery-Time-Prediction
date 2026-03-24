import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import plotly.express as px

# CONFIG
st.set_page_config(
    page_title="Food Delivery Prediction",
    page_icon="📊",
    layout="wide"
)


# SIDEBAR NAVIGATION

st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Profile", "Dashboard", "Predict"])


# LOAD MODEL

@st.cache_resource
def load_model():
    with open("model/model_lr.pkl", "rb") as file:
        model = pickle.load(file)
    with open("model/columns.pkl", "rb") as file:
        columns = pickle.load(file)
    return model, columns

model, columns = load_model()

# HOME PAGE
if page == "Home":
    st.title("📦 Food Delivery Time Prediction")

    st.markdown("""
    Selamat datang di aplikasi prediksi waktu pengiriman makanan 🚚

    ### 🎯 Fitur:
    - Prediksi waktu pengiriman
    - Dashboard analisis data
    - Informasi project & developer

    Gunakan menu di sebelah kiri untuk navigasi.
    """)


# PROFILE PAGE

elif page == "Profile":
   # Profile Section
    st.title("👤 Profile")

    st.caption("Data Analyst | Data Scientist | Business Insight Enthusiast | Data Engineering")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            "assets/Foto Nonformal.png",
            width=220,
            caption="Mafud Satrio Setiono"
        )

    with col2:
        st.subheader("Halo, saya Mafud 👋")

        st.markdown("""
            Saya **Mafud Satrio Setiono**, seorang **Data Enthusiast** yang berfokus pada
            **Data Engineering, Data Analysis, Data Science, dan Business Insight**.

            Saya memiliki latar belakang **Teknik Informatika** dan pengalaman mengerjakan
            berbagai proyek analisis data menggunakan **Python, SQL**, serta tools visualisasi
            seperti **Tableau dan Power BI**.

            Saya tertarik membangun solusi berbasis data yang **tidak hanya akurat secara teknis,
            tetapi juga relevan untuk pengambilan keputusan bisnis**.
        """)

    # Skills Section
    st.divider()
    st.subheader("🛠️ Skills & Tools")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            **📊 Data & BI Tools**
            - Tableau  
            - Power BI  
            - Looker
            - Excel  
            - Git & GitHub
        """)

    with col2:
        st.markdown("""
            **💻 Programming & Database**
            - Python  
            - PostgreSQL  
            - MySQL
        """)

    with col3:
        st.markdown("""
            **🤝 Soft Skills**
            - Problem Solving  
            - Critical Thinking  
            - Communication  
            - Teamwork  
            - Time Management  
            - Adaptability  
        """)

    # Value Proposition
    st.divider()
    st.subheader("💡 What I Bring")

    st.markdown("""
        - Mampu menerjemahkan data menjadi **insight yang actionable**  
        - Fokus pada **business impact**, bukan hanya model  
        - Terbiasa bekerja dengan **data historis & time series**  
        - Berpikir strategis dan berbasis ROI  
        - Berkomunikasi efektif dengan pemangku kepentingan non-teknis
    """)

    # Contact Section
    st.divider()
    st.subheader("📬 Contact & Links")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            📧 **Email**  
            riosetiono23@gmail.com
        """)

    with col2:
        st.markdown("""
            🔗 **LinkedIn**  
            [linkedin.com/in/mafud-satrio-setiono](https://www.linkedin.com/in/mafud-satrio-setiono-5950a7266/)
    """)

    st.caption("Terbuka untuk peluang Data Analyst / Data Scientist ")


# DASHBOARD PAGE
elif page == "Dashboard":
    st.title("📊 Delivery Insights Dashboard")

    try:
        df = pd.read_csv("Food_Delivery_Times.csv")
    except:
        st.error("❌ Dataset tidak ditemukan")
        st.stop()

        
    # METRICS
    
    col1, col2, col3 = st.columns(3)

    col1.metric("⏱️ Avg Delivery Time", f"{df['Delivery_Time_min'].mean():.1f} min")
    col2.metric("📏 Avg Distance", f"{df['Distance_km'].mean():.1f} km")
    col3.metric("👨‍🍳 Avg Prep Time", f"{df['Preparation_Time_min'].mean():.1f} min")

    st.divider()

        
    # DISTRIBUTION (INTERAKTIF)
    
    st.subheader("📈 Delivery Time Distribution")

    fig = px.histogram(
        df,
        x="Delivery_Time_min",
        nbins=30,
        title="Distribution of Delivery Time",
        color_discrete_sequence=["#636EFA"]
    )
    st.plotly_chart(fig, use_container_width=True)

    
    # RELATIONSHIP
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚗 Distance Impact")
        fig2 = px.scatter(
            df,
            x="Distance_km",
            y="Delivery_Time_min",
            trendline="ols",
            title="Distance vs Delivery Time"
        )
        st.plotly_chart(fig2, use_container_width=True)

    with col2:
        st.subheader("👨‍🍳 Preparation Impact")
        fig3 = px.scatter(
            df,
            x="Preparation_Time_min",
            y="Delivery_Time_min",
            trendline="ols",
            title="Preparation Time vs Delivery Time"
        )
        st.plotly_chart(fig3, use_container_width=True)

    st.divider()

    
    # CATEGORY (LEBIH USER-FRIENDLY)
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚦 Traffic Impact")
        traffic_avg = df.groupby("Traffic_Level")["Delivery_Time_min"].mean().reset_index()

        fig4 = px.bar(
            traffic_avg,
            x="Traffic_Level",
            y="Delivery_Time_min",
            color="Traffic_Level",
            title="Average Delivery Time by Traffic"
        )
        st.plotly_chart(fig4, use_container_width=True)

    with col2:
        st.subheader("🌧️ Weather Impact")
        weather_avg = df.groupby("Weather")["Delivery_Time_min"].mean().reset_index()

        fig5 = px.bar(
            weather_avg,
            x="Weather",
            y="Delivery_Time_min",
            color="Weather",
            title="Average Delivery Time by Weather"
        )
        st.plotly_chart(fig5, use_container_width=True)

# PREDICT PAGE
elif page == "Predict":
    st.title("🔮 Predict Delivery Time")

    col1, col2 = st.columns(2)

    with col1:
        distance = st.number_input("Distance (km)", 0.0, 20.0, step=0.1)
        prep_time = st.number_input("Preparation Time (min)", 0, 60)
        experience = st.number_input("Courier Experience (years)", 0, 10)

    with col2:
        weather = st.selectbox("Weather", ["Clear", "Rainy", "Snowy", "Windy", "Foggy"])
        traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
        time_of_day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
        vehicle = st.selectbox("Vehicle Type", ["Bike", "Scooter", "Car"])

    # Preprocessing
    input_data = pd.DataFrame({
        'distance_km': [distance],
        'preparation_time_min': [prep_time],
        'courier_experience_yrs': [experience],
        'weather': [weather],
        'traffic_level': [traffic],
        'time_of_day': [time_of_day],
        'vehicle_type': [vehicle]
    })

    input_data = pd.get_dummies(input_data)
    input_data = input_data.reindex(columns=columns, fill_value=0)

    # Predict
    if st.button("🚀 Predict"):
        prediction = model.predict(input_data)

        st.success(f"⏱️ Estimated Delivery Time: {prediction[0]:.2f} minutes")

        if prediction[0] > 80:
            st.warning("⚠️ Kemungkinan terjadi keterlambatan")
        elif prediction[0] < 40:
            st.info("✅ Pengiriman relatif cepat")