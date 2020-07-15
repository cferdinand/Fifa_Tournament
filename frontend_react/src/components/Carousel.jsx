import React, { useState, useEffect } from "react";
import Flickity from "react-flickity-component";
import CarouselCardsTemplate from "./CarouselCardsTemplate.jsx";
import axios from "axios";

const Carousel = () => {
  const [tournaments, setTournaments] = useState([]);

  const Cards = () => {
    let options = { wrapAround: true, pageDots: false };
    return (
      <Flickity options={options}>
        {tournaments.map((tournament) => {
          return <CarouselCardsTemplate tournament={tournament} />;
        })}
      </Flickity>
    );
  };

  useEffect(() => {
    axios.get("/tournament?name=").then(({ data }) => {
      setTournaments(data.tournament);
    });
  }, []);
  return (
    <div>
      <div>
        <Cards />
      </div>
      <div>
        <button>View All</button>
      </div>
    </div>
  );
};

export default Carousel;
