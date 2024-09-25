import axios from 'axios';

const API_URL = 'http://localhost:8000'; // Backend URL

// Login API request
export const loginUser = async (user) => {
  try {
    const response = await axios.post(`${API_URL}/login`, user);
    return response.data.access_token;
  } catch (error) {
    console.error('Login failed:', error);
    throw error;
  }
};

// Fetch all mutual fund schemes
export const fetchMutualFunds = async (token) => {
  try {
    const response = await axios.get(`${API_URL}/all-schemes`, {
      headers: {
        token: `${token}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Failed to fetch mutual funds:', error);
    throw error;
  }
};

// Purchase mutual fund units
export const purchaseUnits = async (token, isin, units) => {
  try {
    const response = await axios.post(`${API_URL}/purchase`, null, {
      headers: {
        token: `${token}`,
        ISIN: isin,
        Units: units,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Failed to purchase units:', error);
    throw error;
  }
};
