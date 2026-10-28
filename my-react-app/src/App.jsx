import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

function App() {
  const { league_id } = useParams();
  const [league, setLeague] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const controller = new AbortController();

    setLoading(true);
    setError(null);
    setLeague(null);

    fetch(`/api/${encodeURIComponent(league_id)}`, {
      signal: controller.signal,
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error(`Request failed: ${res.status}`);
        }
        return res.json();
      })
      .then((data) => setLeague(data))
      .catch((err) => {
        if (err.name !== "AbortError") {
          setError(err.message);
        }
      })
      .finally(() => {
        if (!controller.signal.aborted) {
          setLoading(false);
        }
      });

    return () => controller.abort();
  }, [league_id]);

  if (loading) return <p>Loading league...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <main>
      <h1>{league.name} League</h1>
      <pre>{JSON.stringify(league, null, 2)}</pre>
    </main>
  );
}

export default App;