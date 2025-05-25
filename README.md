# QR Code Generator

A simple Flask web app to generate QR codes from URLs. Enter a URL, generate a QR code, and download the image.

## Features

- Generate QR codes for any URL
- Download the generated QR code as a PNG image
- Responsive, modern UI with light/dark mode toggle

## Demo

![Screenshot](static/qr.png)

## Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/qr-code-generator.git
   cd qr-code-generator
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

### Running the App

```sh
python app.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

### Deployment

You can deploy this app using Gunicorn:

```sh
gunicorn app:app
```

## Project Structure

```
app.py
requirements.txt
static/
    qr.png
templates/
    index.html
```

- `app.py`: Main Flask application
- `templates/index.html`: HTML template
- `static/qr.png`: Generated QR code image

## License

MIT License
