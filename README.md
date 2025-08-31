## spotipy_flask
Flask app (CRUD) project, built with Flask, Spotipy, SQLAlchemy.

## 🔧 Features
- See your Spotify stats past 1 month.
- Create account with your favourite album and see other's favourite albums.

## 🚀 Getting Started

You can run this project by downloading it as a ZIP file or by cloning the repository.

## 🔧 Setup

### 1. (Recommended) Create and activate a virtual environment
- `python -m venv venv`
- Linux / macOS: `source venv/bin/activate`
- Windows: `venv\Scripts\activate`

> ⚠️ If you prefer not to use a virtual environment, you can install dependencies globally using `python -m pip install -r requirements.txt`.

### 2. Install dependencies
- Inside the virtual environment: `pip install -r requirements.txt`  
- Or globally: `python -m pip install -r requirements.txt` (especially on Windows if `pip install` fails)

### 3. Create a `.env` file with the following format:
```
CLIENT_ID = 'xxxxxxxxx'
CLIENT_SECRET = 'xxxxxxxxx'
REDIRECT_URI = 'http://localhost:8888/callback'
```
# 4. Get your ID and SECRET from [Spotify's Dashboard](https://developer.spotify.com/dashboard)
- (you need to create an app) and replace the xxxxxxxxx values with your credentials.
# 5. Start the app
- Run `main.py`
- The website will be available at http://localhost:8888

## 🖼️ Images
<img width="1906" height="1064" alt="Image" src="https://github.com/user-attachments/assets/de0cdc84-8a09-4d2d-a769-081c58eef0dc" />
<img width="1917" height="906" alt="Image" src="https://github.com/user-attachments/assets/6f4424d5-0e3f-46d9-accb-97c5c288574f" />
