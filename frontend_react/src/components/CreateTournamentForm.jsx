import React, { useState } from "react";
import IADButton from "./Form/IncreaseAndDecreaseButton.jsx";
import TeamSelection from "./Form/TeamSelection.jsx";

const initialState = {
  teams: 2,
  rounds: 1,
  groups: 1,
  knockout: 1,
  final: 1,
};

const CreateTournamentForm = () => {
  const [state, setstate] = useState(initialState);
  const [teams, setTeams] = useState({});
  return (
    <div>
      <form>
        <label>
          Name
          <input type="text"></input>
        </label>
        <label>Type of Tournament</label>
        <select>
          <option value="----" disabled selected>
            ----
          </option>
          <option value="League">League</option>
          <option value="Knockout">Knockout</option>
          <option value="League & Knockout">League & Knockout</option>
          <option value="Groups">Groups</option>
        </select>
        <div>
          <label>Number of Teams</label>
          <IADButton updateState={setstate} state={state} field="teams" />
        </div>
        <div>
          <label>Number of Match Day Rounds</label>
          <IADButton updateState={setstate} state={state} field="rounds" />
        </div>
        <div>
          <label>Number of Groups</label>
          <IADButton updateState={setstate} state={state} field="groups" />
        </div>
        <div>
          <label>Number of Legs in Knockout</label>
          <IADButton updateState={setstate} state={state} field="knockout" />
        </div>
        <div>
          <label>Number of Final Legs</label>
          <IADButton updateState={setstate} state={state} field="final" />
        </div>
        <TeamSelection updateTeams={setTeams} nTeams={state.teams} />
      </form>
    </div>
  );
};

export default CreateTournamentForm;
