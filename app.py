import streamlit as st
from PIL import Image
import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim

# App configuration
st.set_page_config(page_title="SketchAssist", layout="wide")
st.title("🎨 SketchAssist – Your Sketch Review Buddy")

st.markdown("Upload your **sketch** and the **reference image** to see them side-by-side. More features coming soon!")

# Upload columns
col1, col2 = st.columns(2)

# Sketch uploader
with col1:
    sketch_file = st.file_uploader("Upload your sketch", type=["jpg", "jpeg", "png"], key="sketch")
    if sketch_file:
        sketch_img = Image.open(sketch_file)
        st.image(sketch_img, caption="🖌️ Your Sketch", use_container_width=True)

# Reference uploader
with col2:
    reference_file = st.file_uploader("Upload your reference image", type=["jpg", "jpeg", "png"], key="ref")
    if reference_file:
        ref_img = Image.open(reference_file)
        st.image(ref_img, caption="📸 Reference Image", use_container_width=True)

# User experience level selector
experience_level = st.selectbox(
    "🧠 Choose your sketching experience level:",
    ["🎨 Beginner", "✏️ Intermediate", "🧠 Expert"]
)

# Image comparison & feedback
if sketch_file and reference_file:
    # Convert to NumPy arrays
    sketch_np = np.array(sketch_img.convert("L"))  # Grayscale
    ref_np = np.array(ref_img.convert("L"))        # Grayscale

    # Resize to match dimensions
    ref_np_resized = cv2.resize(ref_np, (sketch_np.shape[1], sketch_np.shape[0]))

    # Calculate SSIM and diff map
    score, diff = ssim(sketch_np, ref_np_resized, full=True)
    diff = (diff * 255).astype("uint8")  # Scale diff to 0-255

    # Invert diff for heatmap (brighter = more difference)
    heatmap = cv2.applyColorMap(255 - diff, cv2.COLORMAP_JET)

    # Display similarity score
    st.markdown(f"### 🔍 Similarity Score: **{round(score * 100, 2)}%**")

    # Interpret score based on user experience
    if experience_level == "🎨 Beginner":
        st.success("Great start! Don't worry about a low score — focus on shapes and placement. Keep practicing!")
    elif experience_level == "✏️ Intermediate":
        if score >= 0.7:
            st.success("Looking sharp! Your sketch closely mirrors the reference.")
        else:
            st.info("You're getting there! Pay attention to proportions and angles.")
    elif experience_level == "🧠 Expert":
        if score >= 0.85:
            st.success("Excellent technical match — impressive accuracy!")
        elif score >= 0.6:
            st.info("Well done. Small tweaks could push this to perfection.")
        else:
            st.warning("Consider revisiting alignment or key feature proportions for higher realism.")

    # Display heatmap
    st.markdown("### 🔥 Difference Heatmap")
    st.image(heatmap, channels="BGR", use_container_width=True)
    