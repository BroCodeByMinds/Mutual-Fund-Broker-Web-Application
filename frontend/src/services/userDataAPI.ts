import axiosInstance from '../utils/axiosInstance';

export const getUserDetails = async () => {
  const response = await axiosInstance.get('/user/details');
  return response.data;
};
