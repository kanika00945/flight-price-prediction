
import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Flight Price Predictor", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #e0f7fa, #ffffff);
        color: #000000;
    }
    h1, h2, p {
        color: #4B0082;
    }
    .stButton>button {
        background-color: #CC95FF;
        color: #ffffff;
        font-weight: bold;
        border-radius: 12px;
        height: 45px;
        width: 220px;
        font-size: 16px;
        transition: background 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #6a0dad;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load model
model = pickle.load(open("model.pickle", "rb"))

# Title
st.markdown("<h1 style='text-align: center;'>✈️ Flight Price Predictor</h1>", unsafe_allow_html=True)

# Correct Mappings (same as dataset)
airline_options = {'AirAsia':0, 'Indigo':1, 'GO_FIRST':2, 'SpiceJet':3, 'Air_India':4, 'Vistara':5}
source_city_options = {'Delhi':0, 'Hyderabad':1, 'Bangalore':2, 'Mumbai':3, 'Kolkata':4, 'Chennai':5}
destination_city_options = {'Delhi':0, 'Hyderabad':1, 'Mumbai':2, 'Bangalore':3, 'Chennai':4, 'Kolkata':5}

departure_time_options = {
    'Early Morning': 0,
    'Morning':1,
    'Afternoon':2,
    'Evening':3,
    'Night':4,
    'Late Night':5
}
arrival_time_options = departure_time_options

# Stops mapping (UI → dataset → numeric)
stops_display = {'Zero':'zero', 'One':'one', 'Two or More':'two_or_more'}
stops_numeric = {'zero':0, 'one':1, 'two_or_more':2}

class_options = {'Economy':0, 'Business':1}

col1, col2 = st.columns(2)

with col1:
    airline = st.selectbox("Airline", list(airline_options.keys()))
    source_city = st.selectbox("Source City", list(source_city_options.keys()))
    departure_time = st.selectbox("Departure Time", list(departure_time_options.keys()))
    stops = st.selectbox("Stops", list(stops_display.keys()))

with col2:
    destination_city = st.selectbox("Destination City", list(destination_city_options.keys()))
    arrival_time = st.selectbox("Arrival Time", list(arrival_time_options.keys()))
    flight_class = st.selectbox("Class", list(class_options.keys()))
    extra_feature = st.number_input("Additional Feature (numeric)", min_value=0, value=1)

st.markdown("---")

# Prediction Button
if st.button("Predict Price"):
    input_data = np.array([[
        airline_options[airline],
        source_city_options[source_city],
        destination_city_options[destination_city],
        departure_time_options[departure_time],
        arrival_time_options[arrival_time],
        stops_numeric[stops_display[stops]],
        class_options[flight_class],
        extra_feature
    ]])

    prediction = model.predict(input_data)[0]

    # 💥 FIX: never allow negative output
    prediction = max(0, prediction)

    st.success(f"💰 Estimated Flight Price: ₹{round(prediction, 2)}")
    st.balloons()

