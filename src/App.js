import React from 'react';

// Styling the app
const appStyle = {
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  height: '100vh',
  background: 'linear-gradient(135deg, #6a11cb, #2575fc)',
  color: '#ffffff',
  fontFamily: 'Arial, sans-serif',
  textAlign: 'center',
};

const headingStyle = {
  fontSize: '3rem',
  margin: '20px 0',
  animation: 'fadeIn 2s ease-in-out',
};

const subheadingStyle = {
  fontSize: '1.5rem',
  marginTop: '10px',
  opacity: 0.8,
};

// Add a subtle animation
const keyframesStyle = `
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
`;

function App() {
  return (
    <>
      <style>{keyframesStyle}</style>
      <div style={appStyle}>
        <h1 style={headingStyle}>🌟 Hello, World! 🌍</h1>
        <p style={subheadingStyle}>Welcome to your first creative React app!</p>
      </div>
    </>
  );
}

export default App;
