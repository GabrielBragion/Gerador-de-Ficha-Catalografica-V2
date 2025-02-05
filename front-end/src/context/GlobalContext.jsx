import React, { createContext, useContext, useState } from 'react';

// 1️⃣ Criação do contexto
const GlobalContext = createContext();

// 2️⃣ Componente Provider para encapsular a aplicação
export const GlobalProvider = ({ children }) => {
  const [globalData, setGlobalData] = useState("");

  return (
    <GlobalContext.Provider value={{ globalData, setGlobalData }}>
      {children}
    </GlobalContext.Provider>
  );
};

// 3️⃣ Hook personalizado para consumir o contexto de forma mais fácil
export const useGlobalContext = () => useContext(GlobalContext);
