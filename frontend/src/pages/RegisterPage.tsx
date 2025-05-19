import React, { useState } from 'react';
import { registerUser } from '../services/userauthAPI';
import { MESSAGES } from '../constants/messages';
import { useNavigate, Link } from 'react-router-dom';
import '../styles/AuthForm.css';

const RegisterPage: React.FC = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();
  
    const handleRegister = async () => {
        try {
          const response = await registerUser({ email, password });
      
          if (response.data.status_code === 200) {
            // Navigate to dashboard on successful registration
            navigate('/dashboard');
          } else {
            window.alert(response.data.message || 'Registration failed. Please try again.');
          }
        } catch (error: any) {
          const errorMessage =
            error?.response?.data?.message ||
            'Something went wrong. Please try again later.';
          window.alert(errorMessage);
        }
      };
      
      
  
    return (
      <div className="auth-container">
        <div className="auth-card">
          <h2>Register</h2>
          <div className="form-group">
            <label>Email</label>
            <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Enter email" />
          </div>
          <div className="form-group">
            <label>Password</label>
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Enter password" />
          </div>
          <button className="btn" onClick={handleRegister}>Register</button>
          <p>Already have an account? <Link to="/login">Login here</Link></p>
        </div>
      </div>
    );
  };
  
  export default RegisterPage;