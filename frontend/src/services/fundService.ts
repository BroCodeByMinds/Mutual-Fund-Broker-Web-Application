import axios from 'axios';
import { FundFamiliesResponse, OpenEndedScheme } from '../types/fundTypes';
import { USER_ENDPOINTS } from '../constants/api';

export const getFundFamilies = async () => {
  const token = localStorage.getItem('access_token');
  return axios.get<FundFamiliesResponse>(USER_ENDPOINTS.FUND_FAMILIES, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
};

export const getOpenEndedSchemes = async (mutualFundFamily: string) => {
  const token = localStorage.getItem('access_token');
  return axios.get<OpenEndedScheme[]>(USER_ENDPOINTS.OPEN_ENDED, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    params: {
      mutual_fund_family: mutualFundFamily,
    },
  });
};
