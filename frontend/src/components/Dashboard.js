import React, { useState, useEffect } from 'react';
import { fetchMutualFunds } from '../services/api';
import MutualFund from './MutualFund';

function Dashboard({ token }) {
  const [funds, setFunds] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadFunds = async () => {
      try {
        const data = await fetchMutualFunds(token);
        setFunds(data);
      } catch (err) {
        setError('Failed to fetch mutual funds.');
      }
    };
    loadFunds();
  }, [token]);

  return (
    <div className="dashboard">
      <h2>Mutual Fund Dashboard</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <div className="fund-list">
        {funds.length > 0 ? (
          funds.map((fund, index) => <MutualFund key={index} fund={fund} token={token} />)
        ) : (
          <p>No funds available.</p>
        )}
      </div>
    </div>
  );
}

export default Dashboard;
