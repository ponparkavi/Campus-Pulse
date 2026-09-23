import { apiClient } from './axios';
import { User } from '../store/authStore';

interface LoginData {
  username: string; // OAuth2 form uses 'username' for email
  password: string;
}

interface TokenResponse {
  access_token: string;
  token_type: string;
}

export const authApi = {
  login: async (data: LoginData) => {
    const formData = new URLSearchParams();
    formData.append('username', data.username);
    formData.append('password', data.password);
    
    const response = await apiClient.post<TokenResponse>('/auth/login', formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });
    return response.data;
  },
  
  getMe: async () => {
    const response = await apiClient.get<User>('/auth/me');
    return response.data;
  }
};
