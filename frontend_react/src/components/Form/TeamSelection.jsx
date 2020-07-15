import React from "react";

const TeamSelection = ({ updateTeams, nTeams }) => {
  const TeamForm = () => {
    let teams = [];
    for (let i = nTeams; i > 0; i--) {
      teams.push(
        <div>
          <div>
            <label>Player: </label>
            <input type="text" name="player" placeholder="Name" value="" />
          </div>
          <div>
            <label>Team: </label>
            <input type="text" name="teams" placeholder="Team" value="" />
          </div>
        </div>
      );
    }
    return teams;
  };
  return (
    <div>
      <TeamForm />
    </div>
  );
};

export default TeamSelection;
