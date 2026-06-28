"use client";

import { useState } from "react";
import { sendQuery } from "../lib/api";
import ResponseCard from "./ResponseCard";

export default function ChatBox() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const handleSend = async () => {
    const data = await sendQuery(input);
    setResponse(data.response);
  };

  return (
    <div style={{ marginTop: 20 }}>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask a research question..."
        style={{ width: "100%", padding: 10 }}
      />

      <button onClick={handleSend} style={{ marginTop: 10 }}>
        Ask
      </button>

      {response && <ResponseCard text={response} />}
    </div>
  );
}