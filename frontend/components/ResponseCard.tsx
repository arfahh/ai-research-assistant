export default function ResponseCard({ text }: { text: string }) {
  return (
    <div
      style={{
        marginTop: 20,
        padding: 15,
        border: "1px solid #ddd",
        borderRadius: 8,
        whiteSpace: "pre-wrap"
      }}
    >
      {text}
    </div>
  );
}