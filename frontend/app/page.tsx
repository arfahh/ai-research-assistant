"use client";

import ChatBox from "../components/ChatBox";

export default function Page() {
  return (
    <main style={{ maxWidth: 800, margin: "0 auto", padding: 20 }}>
      <h1>AI Research Assistant</h1>
      <ChatBox />
    </main>
  );
}