import { useState, useEffect } from "react";
import { useParams, useSearchParams } from "react-router-dom";

function MatchupRoster() {
  const { league_id, roster_id } = useParams();
  const [searchParams] = useSearchParams();

  const week = searchParams.get("week") ?? "7";

  const [league, setLeague] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const controller = new AbortController();

    setLoading(true);
    setError(null);
    setLeague(null);

    const params = new URLSearchParams({
      week,
    });

    fetch(
      `/api/${encodeURIComponent(league_id)}/matchups/${roster_id}?${params.toString()}`,
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
  }, [league_id, week, roster_id]);

  if (loading) return <p>Loading league...</p>;
  if (error) return <p>Error: {error}</p>;
  if (!league) return <p>No matchup found.</p>;

  return (
    <main>
      <h1>Starters: {league.starters}</h1>
    </main>
  );
}

export default MatchupRoster;