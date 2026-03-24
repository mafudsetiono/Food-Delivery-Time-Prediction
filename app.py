import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import plotly.express as px

def set_custom_style():
    st.markdown("""
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: white;
    }

    /* Title */
    h1, h2, h3 {
        color: #f8fafc;
    }

    /* Card style */
    .card {
        background: rgba(255,255,255,0.05);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }

    /* Metric style */
    .metric {
        font-size: 20px;
        font-weight: bold;
        color: #38bdf8;
    }

    /* Button */
    .stButton>button {
        background: linear-gradient(90deg, #38bdf8, #6366f1);
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
    }

    .stButton>button:hover {
        background: linear-gradient(90deg, #6366f1, #38bdf8);
    }
    </style>
    """, unsafe_allow_html=True)

set_custom_style()

def set_bg():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)),
                        url("https://images.unsplash.com/photo-1606787366850-de6330128bfc");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .block-container {{
            background: rgba(255,255,255,0.05);
            padding: 30px;
            border-radius: 15px;}}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg()

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
    st.title("📦 Food Delivery Intelligence")

    # INTRO
    st.markdown("""
    <div class="card">
    <h3>🚀 Smart Delivery Prediction System</h3>
    <p>
    Sistem ini memprediksi waktu pengiriman makanan menggunakan Machine Learning
    berdasarkan faktor operasional seperti jarak, traffic, cuaca, dan waktu persiapan.
    </p>
    </div>
    """, unsafe_allow_html=True)

    
    # SUMMARY INSIGHT
    st.subheader("📊 Key Insights")

    col1, col2, col3 = st.columns(3)

    col1.markdown("""
    <div class="card">
    <h4>📏 Distance</h4>
    <p>Faktor paling berpengaruh terhadap waktu pengiriman.</p>
    </div>
    """, unsafe_allow_html=True)

    col2.markdown("""
    <div class="card">
    <h4>🚦 Traffic</h4>
    <p>Kemacetan tinggi meningkatkan delay secara signifikan.</p>
    </div>
    """, unsafe_allow_html=True)

    col3.markdown("""
    <div class="card">
    <h4>👨‍🍳 Preparation</h4>
    <p>Waktu persiapan berkontribusi terhadap total delivery time.</p>
    </div>
    """, unsafe_allow_html=True)

    # BUSINESS RECOMMENDATION
    st.subheader("💡 Business Recommendations")

    st.markdown("""
    <div class="card">
    
    <h4>🚀 Optimasi Operasional</h4>
    <ul>
        <li>Prioritaskan order dengan jarak dekat untuk meningkatkan delivery speed</li>
        <li>Gunakan rute alternatif saat traffic tinggi</li>
    </ul>

    <h4>📍 Strategi Lokasi</h4>
    <ul>
        <li>Tambahkan kitchen atau hub di area dengan demand tinggi</li>
        <li>Kurangi jarak pengiriman untuk meningkatkan efisiensi</li>
    </ul>

    <h4>⏱️ Efisiensi Waktu</h4>
    <ul>
        <li>Optimalkan proses preparation untuk mengurangi delay</li>
        <li>Gunakan estimasi waktu real-time untuk customer</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

    
    # MODEL INFO   
    st.subheader("🤖 Model Performance")

    st.markdown("""
    <div class="card">
    <p>
    Model terbaik: <b>Linear Regression</b><br>
    RMSE: <b>8.82</b> (± 8–9 menit error rata-rata)
    </p>
    </div>
    """, unsafe_allow_html=True)

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

    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        distance = st.number_input("📏 Distance (km)", 0.0, 20.0)
        prep_time = st.number_input("👨‍🍳 Preparation Time", 0, 60)
        experience = st.number_input("👨‍✈️ Experience", 0, 10)

    with col2:
        weather = st.selectbox("🌧️ Weather", ["Clear", "Rainy", "Snowy", "Windy", "Foggy"])
        traffic = st.selectbox("🚦 Traffic", ["Low", "Medium", "High"])
        time_of_day = st.selectbox("🕒 Time", ["Morning", "Afternoon", "Evening", "Night"])
        vehicle = st.selectbox("🚗 Vehicle", ["Bike", "Scooter", "Car"])

    st.markdown('</div>', unsafe_allow_html=True)

    # Predict button
    if st.button("🚀 Predict Now"):
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

        prediction = model.predict(input_data)

        st.markdown(f"""
        <div class="card">
        <h2>⏱️ {prediction[0]:.2f} minutes</h2>
        <p>Estimated Delivery Time</p>
        </div>
        """, unsafe_allow_html=True)