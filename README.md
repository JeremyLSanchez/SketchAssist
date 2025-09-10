# 🎨 SketchAssist – AI-Powered Sketch Evaluation Tool

**SketchAssist** is a creative AI tool that helps artists evaluate their sketches before painting.  
It allows users to upload a hand-drawn sketch alongside a reference image, and instantly get feedback on alignment, proportion, and structure.

> 💡 Perfect for beginners, intermediate artists, or advanced illustrators looking to spot imperfections before committing to paint.

---

## 📸 What It Does

- 🖌️ Upload your **sketch**
- 🧾 Upload your **reference image**
- 🧠 Choose your **experience level** (Beginner / Intermediate / Expert)
- 🧮 Calculates a **visual similarity score** using Structural Similarity Index (SSIM)
- 🔥 Shows a **heatmap** of areas that differ between the sketch and reference
- 💬 Provides **tailored feedback** based on your selected skill level

---

## 🧪 Example Output

| Sketch vs Reference | Similarity Score | Heatmap |
|---------------------|------------------|---------|
| ![Sketch](path-to-sketch.jpg) | `🔍 Similarity Score: 76.45%` | ![Heatmap](path-to-heatmap.jpg) |

> Replace image paths with your screenshots!

---

## 🛠️ Tech Stack

| Layer        | Tool |
|--------------|------|
| Language     | Python 3.13 |
| Interface    | Streamlit |
| Image Utils  | OpenCV, Pillow |
| Comparison   | scikit-image (SSIM) |
| Deployment   | (Coming soon: Streamlit Cloud or Hugging Face Spaces) |

---

## 🔧 How to Run Locally

1. Clone the repo:

```bash
git clone https://github.com/yourusername/sketchassist.git
cd sketchassist
```

2. Create a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
streamlit run app.py
```

---

## 💡 Future Features (Roadmap)

- [ ] Auto-suggest sketch corrections (AI overlay)
- [ ] Face landmark comparison
- [ ] Pose analysis and skeleton matching
- [ ] Practice mode with challenge sketches
- [ ] Upload grid overlays or guidelines
- [ ] User profiles for tracking progress over time

---

## 👨‍🎨 Creator

Built by **Jeremy L. Sanchez**  
Graduate student in Computer Science + Business Intelligence, artist, and future data analyst.

Let’s connect!  
🔗 [LinkedIn](https://www.linkedin.com/in/jeremylsanchez) | 📧 jlsanchez1100@gmail.com

---

## 🫶 Support

Feel free to fork this repo, try the app, and suggest improvements!

---
---

git init
git add .
git commit -m "Initial commit with README and app files"
git branch -M main
git remote add origin https://github.com/JeremyLSanchez/SketchAssist.git
git push -u origin main

git remote add origin https://github.com/JeremyLSanchez/SketchAssist.git
git branch -M main
git push -u origin main
