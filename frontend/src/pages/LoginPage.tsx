import React, { useState } from 'react';
import { loginUser } from '../services/userauthAPI';
import { useNavigate, Link } from 'react-router-dom';
import { MESSAGES } from '../constants/messages';
import '../styles/AuthForm.css';
import { LoginResponse } from '../types/Auth';


const LoginPage: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const response = await loginUser({ email, password });
  
      if (response.data.status_code === 200 && response.data.data?.access_token) {
        localStorage.setItem('access_token', response.data.data.access_token);
        navigate('/dashboard');
      } else {
        // Show alert for invalid credentials (non-200 but no crash)
        window.alert(response.data.message || 'Invalid credentials. Please try again.');
      }
    } catch (error: any) {
      // Handle server errors like 500 or network issues
      const errorMessage =
        error?.response?.data?.message ||
        'Something went wrong. Please try again later.';
      window.alert(errorMessage);
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        <h2>Login</h2>
        <div className="form-group">
          <label>Email</label>
          <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Enter email" />
        </div>
        <div className="form-group">
          <label>Password</label>
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Enter password" />
        </div>
        <button className="btn" onClick={handleLogin}>Login</button>
        <p>Don't have an account? <Link to="/register">Register here</Link></p>
      </div>
    </div>
  );
};

export default LoginPage;
