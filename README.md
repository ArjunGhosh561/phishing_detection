# Phish Check Chrome Extension

Phish Check is a Chrome extension that allows users to quickly check if a website is potentially malicious or not. It utilizes a machine learning model deployed on a Flask server to analyze URLs and provide a prediction on their phishing likelihood.

## Features

- Input any URL and check if it's a phishing site
- Receive real-time predictions based on a machine learning model
- Easy-to-use Chrome extension interface

## Installation

### Chrome Extension

1. Clone or download this repository.

2. Open Chrome and go to `chrome://extensions/`.

3. Enable **Developer mode** in the top right corner.

4. Click on **Load unpacked** and select the `extension` folder from the downloaded repository.

5. The Phish Check extension will be installed and visible in your Chrome toolbar.

### Flask App (Backend)

1. Navigate to the `models` folder.

2. Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
