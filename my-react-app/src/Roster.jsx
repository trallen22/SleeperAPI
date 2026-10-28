import { useState, useEffect } from "react";
import { useParams, useSearchParams } from "react-router-dom";

function Roster() {
  const { league_id } = useParams();
  const [searchParams] = useSearchParams();

  const roster_id = searchParams.get("roster_id") ?? "1";

  const [league, setLeague] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const controller = new AbortController();

    setLoading(true);
    setError(null);
    setLeague(null);

    const params = new URLSearchParams({
      roster_id,
    });

    fetch(
      `/api/${encodeURIComponent(league_id)}/roster?${params.toString()}`,
      { signal: controller.signal }
    )
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
  }, [league_id, roster_id]);

  if (loading) return <p>Loading league...</p>;
  if (error) return <p>Error: {error}</p>;
  if (!league) return <p>No matchup found.</p>;

  return (
    <main>
      <h1>Roster ID: {league.roster_id}</h1>
      <h2>starters: {league.starters}</h2>
      <ul>
        {league.starters.map((player, index) => (
            <li key={index}>{player}</li>
        ))}
      </ul>
      <h2>bench: {league.bench}</h2>
      <h2>taxi: {league.taxi}</h2>
    </main>
  );
}

export default Roster;