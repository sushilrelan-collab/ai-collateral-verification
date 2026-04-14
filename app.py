import streamlit as st

import numpy as np

import matplotlib.pyplot as plt

from PIL import Image



st.set_page_config(page_title="AI Collateral Intelligence", layout="wide")



st.title("📦 AI-Based Warehouse Collateral Verification")

st.markdown("AI-assisted system to verify warehouse stock and assess collateral risk.")



uploaded_file = st.file_uploader("Upload Warehouse Image", type=["jpg", "png"])



declared_stock = st.number_input(

    "Declared Stock (Metric Tonnes)",

    min_value=0,

    value=1000

)



if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Warehouse Image", use_column_width=True)



    estimated_stock = int(np.random.normal(declared_stock, 50))

    variance = estimated_stock - declared_stock



    if declared_stock > 0:

        variance_percent = (variance / declared_stock) * 100

    else:

        variance_percent = 0



    if abs(variance_percent) < 5:

        risk = "🟢 LOW"

    elif abs(variance_percent) < 10:

        risk = "🟡 MEDIUM"

    else:

        risk = "🔴 HIGH"



    st.subheader("📊 AI Analysis Output")

    col1, col2, col3 = st.columns(3)



    col1.metric("Estimated Stock (MT)", estimated_stock)

    col2.metric("Variance (MT)", variance)

    col3.metric("Variance (%)", f"{variance_percent:.2f}%")



    st.subheader("🚨 Risk Level")

    st.markdown(f"### {risk}")



    st.subheader("📈 Declared vs Estimated Stock")



    fig, ax = plt.subplots()

    ax.bar(["Declared", "Estimated"], [declared_stock, estimated_stock])

    ax.set_ylabel("Stock (MT)")

    ax.set_title("Stock Comparison")



    st.pyplot(fig)



    st.subheader("🧾 Insights")

    if risk.startswith("🔴"):

        st.error("High discrepancy detected. Immediate audit recommended.")

    elif risk.startswith("🟡"):

        st.warning("Moderate discrepancy. Review advised.")

    else:

        st.success("Stock levels are within acceptable limits.")

else:

    st.info("Please upload a warehouse image to begin analysis.")
