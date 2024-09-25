# Mutual Fund Broker Web Application

## Overview

This is a Mutual Fund Broker Web Application using default credentials for log in, select a fund family house, fetch open-ended schemes, and view their portfolio with current investment values tracked hourly. The application integrates with the RapidAPI to fetch mutual fund data.

## Technologies Used

- **Backend:** FastAPI
- **Frontend:** React.js
- **API Integration:** RapidAPI (Latest Mutual Fund NAV API)

## Features

- User  Login
- Fetch open-ended schemes for selected fund family
- Display portfolio and track current investment value
- Purchase mutual fund
- API integration with RapidAPI for mutual fund data

## Getting Started

### Prerequisites

- Python 3.7+
- Node.js and npm

### Setup Instructions

#### Backend Setup (FastAPI)

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration:**

   Create a `.env` file in the root directory and add the following:

   ```env
    EMAIL = 'selva@gmail.com'
    PASSWORD = '12345678'
    ACCESS_TOKEN = 'selfincj@fjslmdifsnkldf'
    RAPID_API_KEY = 
    RAPID_API_URL = 
   ```

5. **Run the Backend:**

   ```bash
   uvicorn app.main:app --reload
   ```

#### Frontend Setup (React)

1. **Navigate to Frontend Directory:**

   ```bash
   cd frontend
   ```

2. **Install Dependencies:**

   ```bash
   npm install
   ```

3. **Run the Frontend:**

   ```bash
   npm start
   ```

## Postman Collection
https://documenter.getpostman.com/view/30326706/2sAXqwXzAM

## Testing

### Backend Testing

Run the following command to execute backend tests:

```bash
pytest
```

### Frontend Testing

Run the following command to execute frontend tests:

```bash
npm test
```

## Acknowledgments

Thanks to [RapidAPI](https://rapidapi.com/) for providing the mutual fund data API.
