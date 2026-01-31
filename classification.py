import streamlit as st
import pandas as pd
import joblib

# Load model (encoder not needed for this deployment)
model = joblib.load(r"C:\Forest_Cover_Classification\forest_model.pkl")

# App title
st.set_page_config(page_title="EcoType - Forest Cover Prediction", layout="centered")
st.title("🌿 EcoType: Forest Cover Type Prediction")
st.write("Predict forest cover type using cartographic and environmental features")

st.markdown("---")

# User Inputs
st.subheader("📥 Enter Input Features")

elevation = st.number_input("Elevation (meters)", 0, 5000, 2500)
aspect = st.number_input("Aspect (degrees)", 0, 360, 180)
slope = st.number_input("Slope (degrees)", 0, 60, 10)

h_dist_hydro = st.number_input("Horizontal Distance to Hydrology (m)", 0, 10000, 200)
v_dist_hydro = st.number_input("Vertical Distance to Hydrology (m)", -500, 500, 30)
h_dist_road = st.number_input("Horizontal Distance to Roadways (m)", 0, 10000, 300)

hillshade_9am = st.slider("Hillshade at 9 AM", 0, 255, 120)
hillshade_noon = st.slider("Hillshade at Noon", 0, 255, 200)
hillshade_3pm = st.slider("Hillshade at 3 PM", 0, 255, 150)

h_dist_fire = st.number_input("Horizontal Distance to Fire Points (m)", 0, 10000, 500)

# (Shown only for UI completeness – not used in model)
st.selectbox("Wilderness Area", ["Rawah", "Neota", "Comanche Peak", "Cache la Poudre"])
st.selectbox("Soil Type", [f"Soil_Type_{i}" for i in range(1, 41)])

# Create input DataFrame (ONLY numeric features)
final_input = pd.DataFrame({
    "Elevation": [elevation],
    "Aspect": [aspect],
    "Slope": [slope],
    "Horizontal_Distance_To_Hydrology": [h_dist_hydro],
    "Vertical_Distance_To_Hydrology": [v_dist_hydro],
    "Horizontal_Distance_To_Roadways": [h_dist_road],
    "Hillshade_9am": [hillshade_9am],
    "Hillshade_Noon": [hillshade_noon],
    "Hillshade_3pm": [hillshade_3pm],
    "Horizontal_Distance_To_Fire_Points": [h_dist_fire]
})

# Prediction
st.markdown("---")
if st.button("🌲 Predict Forest Cover Type"):
    prediction = model.predict(final_input)

    cover_type_map = {
        1: "Spruce / Fir",
        2: "Lodgepole Pine",
        3: "Ponderosa Pine",
        4: "Cottonwood / Willow",
        5: "Aspen",
        6: "Douglas-fir",
        7: "Krummholz"
    }

    st.success(f"✅ Predicted Forest Cover Type: **{cover_type_map[int(prediction[0])]}**")
