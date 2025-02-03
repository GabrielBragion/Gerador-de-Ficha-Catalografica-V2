import React from "react";
import styles from "./Button.module.css";

const Button = ({ onClick, disabled, children }) => {
  return (
    <button 
      className={styles.button} 
      onClick={onClick} 
      disabled={disabled}
    >
      {children}
    </button>
  );
};

export default Button;