import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000', // Adjust as needed
});

axiosInstance.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers = config.headers || {};
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default axiosInstance;
