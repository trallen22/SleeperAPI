import { useState, useEffect } from "react";
import { useParams, useSearchParams } from "react-router-dom";

function RosterScorecard({ title, players }) {
  return (
    <>
      <h1>{title}:</h1>
      <ul>
        {players.map(([player, points], index) => (
            <li key={index}>{player} {Number(points).toFixed(2)}</li>
        ))}
      </ul>
    </>
  )
}

function MatchupRoster() {
  const { league_id, roster_id } = useParams();
  const [searchParams] = useSearchParams();

  const week = searchParams.get("week") ?? "0";

  const [matchup_roster, setMatchupRoster] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const controller = new AbortController();

    setLoading(true);
    setError(null);
    setMatchupRoster(null);

    const params = new URLSearchParams({
      week,
    });

    if (week == "0") {
      return
    }

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
      .then((data) => setMatchupRoster(data))
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

  if (week == "0") return <p>No week selected</p>
  if (loading) return <p>Loading league...</p>;
  if (error) return <p>Error: {error}</p>;
  if (!matchup_roster) return <p>No matchup roster found.</p>;

  return (
    <main>
      <h1>Roster: {roster_id} Week: {week}</h1>
      <RosterScorecard title="Starters" players={matchup_roster.starters} />
      <RosterScorecard title="Bench" players={matchup_roster.bench} />
      <RosterScorecard title="IR" players={matchup_roster.reserve} />
      <RosterScorecard title="Taxi" players={matchup_roster.taxi} />
    </main>
  );
}

export default MatchupRoster;