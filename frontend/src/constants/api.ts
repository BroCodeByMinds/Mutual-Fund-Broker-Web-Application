export const API_BASE_URL = process.env.REACT_APP_API_BASE || 'http://localhost:8000';

export const USER_ENDPOINTS = {
  REGISTER: `${API_BASE_URL}/user/register`,
  LOGIN: `${API_BASE_URL}/user/login`,
  FUND_FAMILIES: `${API_BASE_URL}/funds/fund-families`,
  OPEN_ENDED: `${API_BASE_URL}/funds/open-ended`,
};