import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import {
  BrowserRouter,
  Routes,
  Route,
  Navigate,
} from 'react-router-dom';
import './index.css'
import App from './App.jsx'
import Matchups from './Matchups.jsx'
import Roster from './Roster.jsx';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/:league_id" element={<App />} />
        <Route path="/:league_id/matchups" element={<Matchups />} />
        <Route path="/:league_id/roster" element={<Roster />} />
      </Routes>
    </BrowserRouter>
  </StrictMode>,
)
