import React, { Children, createContext, useState } from 'react'

export const ThemeContext  = createContext();


const ThemeContextProvider = ({ children }) => {
    const [theme, setTheme] = useState({
        isLightTheme:true,
        light: {syntax: "#555", ui: "#ddd", bg:"#eee"},
        dark:{syntax: "#ddd", ui:"#333",bg:"#555"}
    });

    const toggleTheme = () => {
        setTheme(prevTheme => ({
            ...prevTheme,
            isLightTheme: !prevTheme.isLightTheme
        }));
    }

  return (
    <ThemeContext.Provider value={{ ...theme,toggleTheme }}>
        {children}
    </ThemeContext.Provider>
  )
}

export default ThemeContextProvider;