# 🕵️‍♂️ PhishDetect

**PhishDetect** is a **Machine Learning Phishing Email Detector** built with Python.

---

## 🚀 Features

* Predicts **overall verdict** for emails: Phishing or Legitimate
* Highlights **suspicious keywords** internally for better accuracy
* Supports **multi-line email input** for easy testing

---

## 🛠 How to Use

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/PhishDetect.git
cd PhishDetect
```

### 2️⃣ Set up your Python environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3️⃣ Prepare your dataset

* Place `phishing_emails.csv` inside the `dataset/` folder
* Make sure your CSV has these columns:

| Column          | Description                  |
| --------------- | ---------------------------- |
| `text_combined` | Email content                |
| `label`         | 0 = Legitimate, 1 = Phishing |


[![Kaggle Dataset](https://img.shields.io/badge/Kaggle-Phishing_Email_Dataset-blue?logo=kaggle&style=for-the-badge)](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset)
---

### 4️⃣ Run the program

```bash
python phishing_detector.py
```

---

### 5️⃣ Test your own email

* Paste your **multi-line email** in the terminal
* Type `END` on a new line when finished
* See the **overall verdict**

**Example Input:**

```
Dear user,

Please verify your account immediately by clicking the link below.

Thanks,
Support Team
END
```

**Output:**

```
Overall Verdict: Phishing Email
```

---

### 6️⃣ Exit

* Type `exit` at any time to quit the program

---
