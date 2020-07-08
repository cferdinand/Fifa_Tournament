import React from "react";

const CarouselCardsTemplate = ({ tournament }) => {
  return (
    <div className="carousel-card" key={tournament.id}>
      <div className="carousel-body">
        <div className="carousel-text">
          <p className="carousel-tournament-name">{tournament.name}</p>
          <p className="carousel-tournament-winner">{tournament.winner}</p>
        </div>
      </div>
      <div className="carousel-image">
        <img
          className="trophy-image"
          src="../../public/images/trophy.png"
        ></img>
      </div>
    </div>
  );
};

export default CarouselCardsTemplate;
