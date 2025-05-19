import axios from 'axios';
import { USER_ENDPOINTS } from '../constants/api';
import axiosInstance from '../utils/axiosInstance';
import { LoginResponse } from '../types/Auth';



export const registerUser = async (payload: { email: string; password: string }) => {
  const response = await axiosInstance.post<LoginResponse>(USER_ENDPOINTS.REGISTER, payload);
  return response;
};

export const loginUser = async (payload: { email: string; password: string }) => {
  const response = await axiosInstance.post<LoginResponse>(USER_ENDPOINTS.LOGIN, payload);
  return response;
};