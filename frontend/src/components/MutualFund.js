import React, { useState } from 'react';
import { purchaseUnits } from '../services/api';

function MutualFund({ fund, token }) {
  const [units, setUnits] = useState(0);
  const [purchaseMessage, setPurchaseMessage] = useState('');

  const handlePurchase = async () => {
    try {
      const response = await purchaseUnits(token, fund.isin_div_payout, units);
      setPurchaseMessage(response.message);
    } catch (error) {
      setPurchaseMessage('Failed to purchase units.');
    }
  };

  return (
    <div className="fund-item">
      <h3>{fund.scheme_name}</h3>
      <p>Fund Family: {fund.mutual_fund_family}</p>
      <p>Scheme Type: {fund.scheme_type}</p>
      <p>Category: {fund.scheme_category}</p>
      <p>Date: {fund.date}</p>
      <p>Net Asset Value (NAV): ${fund.net_asset_value}</p>
      <input
        type="number"
        value={units}
        onChange={(e) => setUnits(e.target.value)}
        placeholder="Units"
      />
      <button onClick={handlePurchase}>Purchase</button>
      {purchaseMessage && <p>{purchaseMessage}</p>}
    </div>
  );
}

export default MutualFund;
