import React, { useEffect } from "react";

const IncreaseAndDecreaseButton = ({ updateState, state, field }) => {
  const increase = (e) => {
    e.preventDefault();
    let newState = {};
    newState[field] = state[field] + 1;
    updateState({ ...state, ...newState });
  };

  const decrease = (e) => {
    e.preventDefault();
    let newState = {};
    newState[field] = state[field] - 1;
    updateState({ ...state, ...newState });
  };
  return (
    <div>
      <button onClick={decrease}>-</button>
      <input type="text" value={state[field]}></input>
      <button onClick={increase}>+</button>
    </div>
  );
};

export default IncreaseAndDecreaseButton;
