import React, { createContext, useContext, useEffect, useState } from "react";

interface AuthUser {
  email: string;
}

interface AuthContextValue {
  user: AuthUser | null;
  isAuthenticated: boolean;
  login: (data: { email: string; tokens?: { access?: string; refresh?: string } }) => void;
  logout: () => void;
}

const AuthContext = createContext<AuthContextValue | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<AuthUser | null>(null);

  useEffect(() => {
    const storedEmail = localStorage.getItem("userEmail");
    const accessToken = localStorage.getItem("accessToken");
    if (storedEmail && accessToken) {
      setUser({ email: storedEmail });
    }
  }, []);

  const login: AuthContextValue["login"] = (data) => {
    const { email, tokens } = data;
    if (tokens?.access) {
      localStorage.setItem("accessToken", tokens.access);
    }
    if (tokens?.refresh) {
      localStorage.setItem("refreshToken", tokens.refresh);
    }
    localStorage.setItem("userEmail", email);
    setUser({ email });
  };

  const logout = () => {
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
    localStorage.removeItem("userEmail");
    setUser(null);
  };

  const value: AuthContextValue = {
    user,
    isAuthenticated: !!user,
    login,
    logout,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = (): AuthContextValue => {
  const ctx = useContext(AuthContext);
  if (!ctx) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return ctx;
};
