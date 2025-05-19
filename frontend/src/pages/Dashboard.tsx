import React, { useEffect, useState } from 'react';
import { getFundFamilies, getOpenEndedSchemes } from '../services/fundService';
import { FundFamily, OpenEndedScheme } from '../types/fundTypes';

const Dashboard: React.FC = () => {
  const [fundFamilies, setFundFamilies] = useState<FundFamily[]>([]);
  const [selectedFundFamily, setSelectedFundFamily] = useState('');
  const [openEndedSchemes, setOpenEndedSchemes] = useState<OpenEndedScheme[]>([]);

  useEffect(() => {
    const fetchFundFamilies = async () => {
      try {
        const response = await getFundFamilies();
        if (response.data.status_code === 200) {
          setFundFamilies(response.data.data);
        }
      } catch (error) {
        console.error('Failed to fetch fund families', error);
      }
    };

    fetchFundFamilies();
  }, []);

  const handleSelectChange = async (event: React.ChangeEvent<HTMLSelectElement>) => {
    const selectedValue = event.target.value;
    setSelectedFundFamily(selectedValue);

    try {
      const response = await getOpenEndedSchemes(selectedValue);
      if (Array.isArray(response.data)) {
        setOpenEndedSchemes(response.data);
      } else {
        console.warn('Unexpected response structure:', response.data);
      }
    } catch (error) {
      console.error('Failed to fetch open-ended schemes', error);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-r from-blue-50 via-white to-blue-50 flex items-center justify-center p-6">
      <div className="max-w-7xl w-full bg-white rounded-2xl shadow-xl p-8 space-y-8">
        <h2 className="text-3xl font-extrabold text-blue-900 drop-shadow-sm">
          📊 Mutual Fund Dashboard
        </h2>

        <div className="max-w-sm w-full">
          <label htmlFor="fund-family" className="block mb-2 text-gray-700 font-semibold text-lg">
            Select Mutual Fund Family
          </label>
          <select
            id="fund-family"
            value={selectedFundFamily}
            onChange={handleSelectChange}
            className="block w-full rounded-lg border border-gray-300 px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
          >
            <option value="" disabled>
              Select a fund family
            </option>
            {fundFamilies.map((fund) => (
              <option key={fund.family_fund_id} value={fund.family_fund_name}>
                {fund.family_fund_name}
              </option>
            ))}
          </select>
        </div>

        {openEndedSchemes.length > 0 && (
          <div className="overflow-x-auto rounded-lg shadow-md border border-gray-200">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-blue-100">
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-semibold text-blue-900 uppercase tracking-wider">
                    Scheme Name
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-semibold text-blue-900 uppercase tracking-wider">
                    ISIN (Growth)
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-semibold text-blue-900 uppercase tracking-wider">
                    ISIN (Reinvest)
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-semibold text-blue-900 uppercase tracking-wider">
                    NAV
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-semibold text-blue-900 uppercase tracking-wider">
                    NAV Date
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-semibold text-blue-900 uppercase tracking-wider">
                    Category
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-semibold text-blue-900 uppercase tracking-wider">
                    Type
                  </th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {openEndedSchemes.map((scheme, idx) => (
                  <tr
                    key={idx}
                    className="hover:bg-blue-50 transition-colors duration-200 cursor-pointer"
                  >
                    <td className="px-6 py-4 whitespace-nowrap text-gray-900 font-medium">
                      {scheme.Scheme_Name}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-gray-700">
                      {scheme.ISIN_Div_Payout_ISIN_Growth}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-gray-700">
                      {scheme.ISIN_Div_Reinvestment}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-gray-900 font-semibold">
                      {scheme.Net_Asset_Value}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-gray-700">{scheme.Date}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-gray-700">
                      {scheme.Scheme_Category}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-gray-700">
                      {scheme.Scheme_Type}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {selectedFundFamily && openEndedSchemes.length === 0 && (
          <p className="text-center text-gray-500 italic mt-6">No schemes found for this fund family.</p>
        )}
      </div>
    </div>
  );
};

export default Dashboard;
