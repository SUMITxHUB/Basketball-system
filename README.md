# 🏀 Basketball Player Detection & Tracking System

A computer vision pipeline for detecting, tracking, and recognizing NBA players in live and recorded match footage — built using state-of-the-art transformer-based models and a Streamlit web interface.

---

## Overview

This project combines object detection, segmentation, OCR, and clustering to analyze basketball gameplay footage. Given a video clip, the system identifies every player on the court, tracks their movement across frames, reads jersey numbers, and classifies players by team.

The project is split across two repositories:
- **[Basketball-system](https://github.com/SUMITxHUB/Basketball-system)** — Streamlit frontend and web interface (this repo)
- **[rf-detr](https://github.com/SUMITxHUB/rf-detr)** — RF-DETR fine-tuning pipeline and model training notebooks

---

## Demo

> Upload up to 30 seconds of basketball footage and the system detects players, reads jersey numbers, and clusters teams in real time.

Currently optimized for **Knicks vs Celtics 2025** broadcast footage.

---

## Features

- **Player Detection** — Detects 10+ players per frame using a fine-tuned RF-DETR-Small model trained on a custom basketball dataset with 10 classes (player, ball, referee, rim, jersey number, and player action states)
- **Player Tracking** — Tracks player positions across frames using SAM2 segmentation
- **Jersey Number Recognition** — Reads player numbers via SmolVLM2 OCR
- **Team Classification** — Clusters players into two teams using SigLIP visual embeddings + K-means
- **Streamlit Dashboard** — Interactive web UI for video upload and inference output visualization

---

## Tech Stack

| Component | Technology |
|---|---|
| Object Detection | RF-DETR-Small (fine-tuned) |
| Segmentation & Tracking | SAM2 |
| OCR (Jersey Numbers) | SmolVLM2 |
| Jersey Classification | ResNet (fine-tuned CNN) |
| Visual Embeddings | SigLIP |
| Team Clustering | K-means |
| Web Interface | Streamlit |
| Language | Python |

---

## Model Training

The detection model was fine-tuned on a custom Roboflow basketball dataset containing diverse scenes with motion blur, player overlaps, and small jersey numbers.

- **500+ video frames** preprocessed and labeled for training
- **10 detection classes**: `player`, `player-in-possession`, `player-jump-shot`, `player-layup-dunk`, `player-shot-block`, `number`, `ball`, `ball-in-basket`, `referee`, `rim`
- Achieved **15% improvement** in tracking accuracy through parameter tuning and detection logic refinement
- RF-DETR-S outperforms YOLO11-L on the COCO benchmark while maintaining higher inference speed

See the full training notebook in the [rf-detr repo](https://github.com/SUMITxHUB/rf-detr).

---

## Getting Started

### Prerequisites

```bash
python >= 3.9
```

### Installation

```bash
git clone https://github.com/SUMITxHUB/Basketball-system.git
cd Basketball-system
pip install -r requirements.txt
```

### Run the app

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser, upload a video clip, and click **Analyze Video**.

---

## Project Structure

```
Basketball-system/
├── app.py               # Streamlit frontend
├── requirements.txt     # Python dependencies
└── .gitignore
```

---

## Future Work

- Complete integration of the model inference pipeline into the Streamlit UI
- Add play-by-play event detection (shots, dunks, blocks)
- Extend to support any NBA team matchup, not just Knicks vs Celtics
- Export structured analytics reports (player heatmaps, possession stats)

---

## Author

**Sumit Kumar**
- GitHub: [@SUMITxHUB](https://github.com/SUMITxHUB)
- LinkedIn: [in/sumit16](https://linkedin.com/in/sumit16)
- B.Tech CSE, KIIT University (2022–2026)

---

## License

This project uses models and components subject to their respective upstream licenses. See individual model repositories for details.
