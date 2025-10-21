# Fyra
teknologia

## Streamlit Map Application

This project contains a Streamlit web application that displays an interactive map with sample data points.

### Prerequisites

- Python 3.12 or higher
- UV package manager

### Setup

1. **Install UV** (if not already installed):
```bash
pip install uv
```

2. **Create a virtual environment**:
```bash
uv venv
```

3. **Activate the virtual environment**:
```bash
source .venv/bin/activate  # On Linux/Mac
# or
.venv\Scripts\activate  # On Windows
```

4. **Install dependencies**:
```bash
uv pip install -r requirements.txt
```

### Running the Application

To run the Streamlit application:

```bash
streamlit run app.py
```

The application will start and open in your default web browser at `http://localhost:8501`.

### Features

- **Interactive Map**: Displays location data on an interactive map
- **Filtering**: Filter data points by category using the sidebar
- **Statistics**: View real-time statistics about the displayed data
- **Data View**: Optional toggle to view the raw data table

### Project Structure

```
fyra/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .venv/             # Virtual environment (created by uv)
└── README.md          # This file
```
