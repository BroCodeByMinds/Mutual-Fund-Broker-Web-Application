// types/Auth.ts
export interface LoginResponse {
    status_code: number;
    message: string | null;
    data: {
      email: string;
      access_token: string;
    } | null;
  }
  