# 🧠 Deepfake Detection for Identifying Machine-generated Tweets Using NLP and DL

A Django-based web application that utilizes Natural Language Processing (NLP) and Deep Learning techniques to detect machine-generated (bot) tweets and classify them as either **Normal** or **Bot Fake**.

---

## 🔧 Software Configuration

### 1. Python Installation

- Download Python 3.7.6: [Official Download Page](https://www.python.org/downloads/release/python-376/)
- During installation:
  - ✅ Check **"Add Python to PATH"**
  - Click **Install Now**
- Verify installation:
  ```bash
  python --version
  ```
  Should display: `Python 3.7.6`

---

### 2. Virtual Environment Setup

```bash
python -m venv environment
.\environment\Scripts\activate         # On Windows
source environment/bin/activate       # On macOS/Linux
```

---

### 3. Install Dependencies

- Install Django:
  ```bash
  pip install Django
  django-admin --version
  ```

- Install project dependencies:
  ```bash
  pip install -r set1.txt
  ```

- Download NLP datasets:
  ```bash
  python -m nltk.downloader all
  ```

---

### 4. Django Project Setup

```bash
django-admin startproject Deep
cd Deep
django-admin startapp Deepapp
python manage.py runserver
```

---

## 🚀 Project Execution Steps

### Step 1: Start the Project

- Double-click `run.bat` to launch the Django server.
- Open browser at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

### Step 2: User Registration

- Click **New User** on the login page.
- Fill in your **Name**, **Email ID**, and **Password**.
- Click **Register**.

---

### Step 3: User Login

- Log in using your registered **Email ID** and **Password**.
- Successful login redirects you to the **User Welcome Page**.

---

### Step 4: Admin Login

- Click **Manage Users**.
- Enter **Admin Credentials** (superuser).
- Admin Features:
  - View registered users
  - Delete users
  - Logout

---

### Step 5: Deepfake Application

#### 📊 Model Metrics

- Click **Model Metrics** to view:
  - Sample dataset
  - FastText embeddings
  - F1-scores of algorithms
  - Accuracy bar graph
- Click **Home Page** or **Logout** to return.

#### 🤖 Predict Deepfake

- Click **Predict Deepfake**.
- Enter a tweet and click **Submit**.
- View prediction: **Normal** or **Bot Fake**.
- Click **Logout** to end session.

---

## 📁 Project Structure Overview

```
Deep/
│── Dataset/
│   │── Tweepfake.csv
│
│── Deep/
│   │── __init__.py
│   │── settings.py
│   │── wsgi.py
│   │── asgi.py
│   │── urls.py
│
│── DeepApp/
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── models.py
│   │── tests.py
│   │── urls.py
│   │── views.py
│   │── templates/
│   │   │── admin_login.html
│   │   │── DetectFake.html
│   │   │── index.html
│   │   │── UserLogin.html
│   │   │── UserRegister.html
│   │   │── user_list.html
│   │   │── UserScreen.html
│   │   │── ViewGraph.html
│   │   │── ViewOutput.html
│   │── static/
│   │   │── style.css
│   │   │── templatemo_style.css
│   │   │── images/
│
│── model/
│   │── cnn_history.pckl
│   │── cnn_weights.hdf5
│   │── tfidf.pckl
│   │── X.npy
│   │── Y.npy
│
│── requirements.txt
│── nltkdownload.py
│── set1.txt
│── download_nltk.bat
│── run.bat
│── manage.py
```

---

## 👨‍💻 Developed By Team A-15

**1. Madhuri Ediga** <br>
**2. Nadeem Avulapalli** <br>
**3. Charan Kumar Reddy Dayyam** <br>
**4. Harshavardhan Lourdu Reddy Yeruva** <br>
**Students of Dept. of Computer Science & Engineering (Data Science)** <br>  
**Under the Guidance of Mrs.G.Shabana, Assistant Professor, Dept. of Computer Science & Engineering (AI&ML)** <br><br>
**SRINIVASA RAMANUJAN INSTITUTE OF TECHNOLOGY, Rotarypuram, Anantapur**
