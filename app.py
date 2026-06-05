import streamlit as st
import time

# Set page config
st.set_page_config(
    page_title="NBA Player Tracker",
    page_icon="🏀",
    layout="wide"
)

# Main title and subtitle
st.title("🏀 NBA Player Tracker")
st.caption("Computer vision system that can detect, track, and recognize NBA players during a game")

# Custom CSS for centered tabs and larger font size
st.markdown("""
<style>
.stTabs [data-baseweb="tab-list"] {
    justify-content: center;
}
.stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size: 18px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# Create tabs with better styling
tab1, tab2 = st.tabs(["🎥 Upload & Analysis", "ℹ️ About"])

with tab1:
    # Center the content within the tab
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        # Upload section with styled container
        with st.container():
            st.header("📁 Upload Your Game Clip")
            st.write("Upload up to **30 seconds** of footage from the Knicks vs Celtics 2025 game.")
            
            uploaded_file = st.file_uploader(
                "Choose a video file",
                type=['mp4', 'avi', 'mov', 'mkv', 'wmv'],
                help="Upload a basketball video for analysis"
            )
            
            if uploaded_file is not None:
                # Display video details with better formatting
                st.success(f"✅ Video uploaded: {uploaded_file.name}")
                file_size_mb = uploaded_file.size / (1024 * 1024)
                st.write(f"📊 File size: {file_size_mb:.2f} MB")
                
                # Display the video
                st.video(uploaded_file)
                
                # Analysis section
                st.subheader("🔍 Video Analysis")
                
                # Center the analyze button
                col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
                with col_btn2:
                    if st.button("🚀 Analyze Video", type="primary", use_container_width=True):
                        st.info("You clicked on analyze button")
            else:
                st.info("📤 Please upload a video file to get started.")

with tab2:
    # Center the content within the About tab
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.header("ℹ️ About NBA Player Tracker")
        st.write("""
        This application demonstrates **computer vision for sports analytics** using advanced AI models 
        to analyze basketball gameplay footage.
        
        **Key Features:**
        - **Player Detection & Tracking**: Identifies and follows players throughout the game
        - **Jersey Number Recognition**: Reads player numbers using OCR technology
        - **Team Classification**: Distinguishes between teams based on jersey colors
        - **Ball Tracking**: Monitors basketball movement and trajectory
        - **Real-time Analytics**: Provides instant insights on player performance
        
        **Technology Stack:**
        - **RF-DETR**: State-of-the-art object detection for players, jersey numbers, and basketball objects
        - **SAM2**: Unified model for object segmentation and tracking across video frames
        - **SmolVLM2**: Compact vision-language model for OCR of jersey numbers
        - **ResNet**: Fine-tuned CNN for jersey number classification
        - **SigLIP**: Vision-language model for generating visual similarity embeddings
        - **K-means**: Clustering algorithm to separate players into teams based on embeddings
        
        Currently optimized for **Knicks vs Celtics 2025** broadcast footage.
        """)

# Enhanced sidebar
st.sidebar.title("🏀 NBA Player Tracker")
st.sidebar.markdown("""
**Computer Vision for Sports Analytics**

Using advanced AI models to:
- 🎯 Detect and track players
- 🔢 Recognize jersey numbers  
- 🎨 Cluster teams visually
- ⚡ Real-time analysis

Currently optimized for **Knicks vs Celtics 2025** footage.
""")

st.sidebar.divider()

st.sidebar.subheader("🤖 Model Information")
st.sidebar.write("""
- **Detection**: RF-DETR
- **Segmentation & Tracking**: SAM2
- **OCR**: SmolVLM2
- **Classification**: ResNet
- **Embeddings**: SigLIP
- **Clustering**: K-means
""")

st.sidebar.divider()

st.sidebar.subheader("🔗 Links")
st.sidebar.markdown("[📁 GitHub Repository](https://github.com/coreDaemon/basketball)")
st.sidebar.markdown("[📖 Documentation](https://github.com/coreDaemon/basketball/wiki)")

with st.sidebar.expander("❓ FAQ"):
    st.write("""
    **Q: What video formats are supported?**
    A: MP4, AVI, MOV, MKV, WMV
    
    **Q: What's the maximum file size?**
    A: 20MB recommended for best performance
    
    **Q: Can I analyze other games?**
    A: Currently optimized for Knicks vs Celtics 2025
    """)

# Footer
st.markdown("---")
st.caption("🏀 NBA Player Tracker — Powered by RF-DETR, SAM2, SmolVLM2, ResNet, SigLIP & K-means. © 2025")