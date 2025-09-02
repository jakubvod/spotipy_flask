## spotipy_flask
Flask app (CRUD) project, built with Flask, Spotipy, SQLAlchemy.

## 🔧 Features
- See your Spotify stats past 1 month (no premium required).
- Create account with your favourite album and see other's favourite albums.

## 🚀 Getting Started

You can run this project by:
1. Downloading it as a ZIP file
2. Cloning the repository
3. Running the app on a server: https://spotipy-flask.onrender.com
> ⚠️ Note: The Spotify app is currently in **development mode**. Only users added as testers in the Spotify Dashboard can access Spotify stats.

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
### 4. Get your ID and SECRET from [Spotify's Dashboard](https://developer.spotify.com/dashboard)
- (you need to create an app) and replace the xxxxxxxxx values with your credentials.
### 5. Start the app
- Change `app.run()` to `app.run(port=8888)` in main.
- Run `main.py`
- The website will be available at http://localhost:8888

## 🖼️ Images
<img width="1900" height="1061" alt="Image" src="https://github.com/user-attachments/assets/4b813b2a-2733-414a-bf78-bc159c2c4248" />
<img width="1919" height="1058" alt="Image" src="https://github.com/user-attachments/assets/675d9f19-cde7-4da8-86ce-96c4d89dc7c1" />
<img width="1903" height="1061" alt="Image" src="https://github.com/user-attachments/assets/6aced82e-9540-4cfe-b53b-dfc0df786b6c" />
<img width="1900" height="1061" alt="Image" src="https://github.com/user-attachments/assets/ca414429-418e-4bc5-84c5-7d77e6e58929" />
<img width="1920" height="1062" alt="Image" src="https://github.com/user-attachments/assets/709ff3fb-25df-4323-b400-d000d2f323cf" />
