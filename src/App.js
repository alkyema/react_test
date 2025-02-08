import React, { useState } from "react";

const ChatBot = () => {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState("");

  const sendMessage = async (event) => {
    event.preventDefault();
    if (userInput.trim() === "") {
      return;
    }

    const userMessage = { sender: "user", text: userInput };
    setMessages((prevMessages) => [...prevMessages, userMessage]);

    setUserInput("");

    // Fetch bot response from the given URL
    try {
      const response = await fetch("http://13.60.45.204:8888/response", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ user_input: userInput }),
      });
      const data = await response.text(); // Assuming the response is plain text

      const botMessage = { sender: "bot", text: data };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error("Error fetching bot response:", error);
      const errorMessage = { sender: "bot", text: "Error: Unable to fetch response." };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    }
  };

  return (
    <div
      style={{
        fontFamily: "Arial, sans-serif",
        backgroundColor: "#f5f5f5",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "100vh",
        margin: 0,
      }}
    >
      <div
        style={{
          width: "100%",
          maxWidth: "400px",
          backgroundColor: "#ffffff",
          boxShadow: "0px 8px 16px rgba(0, 0, 0, 0.1)",
          borderRadius: "12px",
          overflow: "hidden",
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          height: "80%",
        }}
      >
        <div
          style={{
            backgroundColor: "#007bff",
            color: "#ffffff",
            padding: "16px",
            textAlign: "center",
            fontSize: "20px",
            fontWeight: "bold",
          }}
        >
          ChatBot
        </div>
        <div
          id="chat-box"
          style={{
            flex: 1,
            overflowY: "auto",
            padding: "16px",
          }}
        >
          {messages.map((message, index) => (
            <div
              key={index}
              style={{
                marginBottom: "10px",
                display: "flex",
                justifyContent:
                  message.sender === "user" ? "flex-end" : "flex-start",
              }}
            >
              <div
                style={{
                  backgroundColor:
                    message.sender === "user" ? "#007bff" : "#28a745",
                  color: "#ffffff",
                  padding: "8px 12px",
                  borderRadius: "8px",
                  maxWidth: "70%",
                  wordWrap: "break-word",
                }}
              >
                {message.text}
              </div>
            </div>
          ))}
        </div>
        <form
          onSubmit={sendMessage}
          style={{
            display: "flex",
            alignItems: "center",
            padding: "8px",
            borderTop: "1px solid #ddd",
          }}
        >
          <input
            type="text"
            value={userInput}
            onChange={(e) => setUserInput(e.target.value)}
            placeholder="Type your message..."
            required
            style={{
              flex: 1,
              padding: "8px",
              border: "1px solid #ddd",
              borderRadius: "4px",
              fontSize: "14px",
            }}
          />
          <button
            type="submit"
            style={{
              padding: "8px 16px",
              backgroundColor: "#007bff",
              color: "#ffffff",
              border: "none",
              borderRadius: "4px",
              cursor: "pointer",
              fontSize: "14px",
              marginLeft: "10px",
            }}
          >
            Send
          </button>
        </form>
      </div>
    </div>
  );
};

export default ChatBot;