import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(page_title="AI Collateral Intelligence", layout="wide")

st.title("📦 AI-Based Warehouse Stock Verification System")

st.markdown("Upload warehouse image to estimate stock and detect risk.")

# Upload image
uploaded_file = st.file_uploader("Upload Warehouse Image", type=["jpg", "png"])

declared_stock = st.number_input("Enter Declared Stock (MT)", min_value=0, value=1000)

if uploaded_file
image = Image.open(uploaded_file)
st.image(image, caption="Uploaded Image", use_column_width=True)

# Simulated AI logic
estimated_stock = int(np.random.normal(loc=declared_stock, scale=50))
variance = estimated_stock - declared_stock
variance_percent = (variance / declared_stock) * 100 if declared_stock > 0 else 0

# Risk logic
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
col3.metric("Variance %", f"{variance_percent:.2f}%")

st.subheader("🚨 Risk Level")
st.markdown(f"### {risk}")

# Chart
st.subheader("📈 Stock Comparison")

labels = ["Declared", "Estimated"]
values = [declared_stock, estimated_stock]

fig, ax = plt.subplots()
ax.bar(labels, values)
ax.set_ylabel("Stock (MT)")
ax.set_title("Declared vs Estimated Stock")

st.pyplot(fig)

# Insights
st.subheader("🧾 Insights")
if risk == "🔴 HIGH":
st.error("High discrepancy detected. Immediate audit recommended.")
elif risk == "🟡 MEDIUM":
st.warning("Moderate discrepancy. Review advised.")
else:
st.success("Stock levels are within acceptable limits.")
commit message:
Add app.py-Capstone working prototype
