# 🌟 **Anime Recommendation System** 🎥

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) 
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

Welcome to the **Anime Recommender System**! This is a Streamlit-based Anime Recommendation System that provides recommendations using content-based filtering (**Bag of Words model**) and displays the **top 50 anime** based on **popularity**. The app is built using the Kaggle Anime Dataset 2023. The system uses a pre-trained similarity matrix to suggest anime similar to the one selected by the user.

---

## 🎯 Features

✅**User-Friendly Interface**: Built with **Streamlit** for a clean and intuitive user experience.  
✅**Anime Recommendations**: Suggests **10 similar anime** based on user selection using content-based filtering.  
✅**Top 50 Anime**: Displays the **most popular 50 anime** with their images.


---

## 🎮 How It Works

1. **Data Loading**:
   - The system loads anime data from a pre-processed `anime.pkl` file and List of top 50 anime form `top_50.pkl`
   - A precomputed similarity matrix is loaded from `similarity.pkl`. 

2. **Recommendation Engine**:
   - The user selects an anime from a dropdown list.
   - The system calculates the most similar anime using the similarity matrix and displays the top 10 recommendations.

3. **Poster Display**:
   - The system fetches and displays posters for the recommended anime using their image URLs.

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Pandas
- Pickle

### Steps

### 📥 Clone the Repository:
   ```bash
   https://github.com/pranayganvir/anime-recomendation-system.git
   cd anime-recomendation-system
   ```

### 📦 Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```
####  🔧 Ensure Required Files are Present:

- anime.pkl → Anime dataset 📂

- similarity.pkl → Precomputed similarity matrix 🧠

- top_50.pkl → List of top 50 anime 🌟 

**Note**- You can easily generate above three files using [model_building.py](https://github.com/pranayganvir/anime-recomendation-system/blob/main/model_building.py)

### 🚀 Run the Streamlit App:
   ```bash
   streamlit run app.py
   ```

🚀 Run the Streamlit App: `http://localhost:8501` to use the app.

---

## 📂 File Structure

```
anime-recommender-system/
├── app.py                  # Main Streamlit application
├── anime.pkl               # Pre-processed anime data
├── similarity.pkl          # Precomputed similarity matrix
├── README.md               # Project documentation
├── requirements.txt        # List of dependencies
└── top_50.pkl              # List of top 50 anime
```

---

## 📌 Usage

1️⃣ Open the app in your browser.

2️⃣ Use the sidebar to select:

- Top 50 Anime: Explore the most popular anime. 🎬

- Anime Recommender System: Choose an anime and get personalized recommendations. 🔍

3️⃣ Click the "Recommend" button and view suggested anime with images! 🖼️



---
## 🎥 Simple demo

<video width="600" controls>
  <source src="https://github.com/pranayganvir/anime-recomendation-system/blob/main/Images/working.mp4" type="video/mp4">
</video>

## 📸 Screenshots
--
![Top 50 Anime](https://github.com/pranayganvir/anime-recomendation-system/blob/main/Images/Screenshot%202025-01-30%20124134.png)
![Anime Recommendation Dashboard](https://github.com/pranayganvir/anime-recomendation-system/blob/main/Images/Screenshot%202025-01-30%20124235.png)
![Anime Recommendation For Death Note](https://github.com/pranayganvir/anime-recomendation-system/blob/main/Images/Screenshot%202025-01-30%20124749.png)
![Anime Recommendation For One Piece](https://github.com/pranayganvir/anime-recomendation-system/blob/main/Images/Screenshot%202025-01-30%20124820.png)


---
 


---
## 🛠️ Technologies Used

🐍 Python (Pandas, Pickle, Requests)

🤖 Machine Learning (Bag of Words Model, Similarity Matrix)

🎨 Streamlit (For interactive UI and deployment)

## 🙌 Acknowledgments

Special thanks to:

- Kaggle for providing the Anime Dataset 2023 📊
- Streamlit for enabling an interactive web-based UI 🎨
- Open-source contributors who inspire and support development 💡
- Anime enthusiasts who continue to make the anime community vibrant! 🎥

---
## 👨‍💻 Author

Developed with ❤️ by Pranay Ganvir.
## ☎️ Contact

For any questions or feedback, feel free to reach out:

- **Pranay Ganvir**  
- **GitHub**: [Pranay Ganvir](https://github.com/pranayganvir)  

---
## 📜 License

This project is licensed under the MIT License. 📝

Enjoy and happy anime watching! 🎉🍿
