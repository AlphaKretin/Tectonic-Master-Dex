import { useParams } from "react-router-dom";
import pokemonJson from "../data/pokemon.json";

interface Ability {
  InternalName: string;
  Name: string;
  Description: string;
}

interface Evolution {
  Pokemon: string;
  Method: string;
  Condition: string;
}

interface Pokemon {
  Name: string;
  InternalName: string;
  Types: string[];
  BaseStats: {
    hp: number;
    attack: number;
    defense: number;
    speed: number;
    sp_atk: number;
    sp_def: number;
  };
  GenderRate: string;
  GrowthRate: string;
  BaseEXP: number;
  CatchRate: number;
  Happiness?: number;
  Abilities: Ability[];
  Moves: (string | number)[][];
  LineMoves?: string[];
  TutorMoves?: string[];
  Tribes?: string[];
  Height: number;
  Weight: number;
  Color: string;
  Shape: string;
  Kind: string;
  Pokedex: string;
  WildItemCommon?: string;
  WildItemUncommon?: string;
  WildItemRare?: string;
  FormName?: string;
  Evolutions?: Evolution[];
  Prevolutions?: Evolution[];
}

function AbilityRender(currentMon: Pokemon) {
  if (currentMon.Abilities.length > 1) {
    return (
      <div>
        <h3>{currentMon.Abilities[0].Name}</h3>
        <p>{currentMon.Abilities[0].Description}</p>

        <h3>{currentMon.Abilities[1].Name}</h3>
        <p>{currentMon.Abilities[1].Description}</p>
      </div>
    );
  } else {
    return (
      <div>
        <h3>{currentMon.Abilities[0].Name}</h3>
        <p>{currentMon.Abilities[0].Description}</p>
      </div>
    );
  }
}

export default function Pokemon() {
  const pokemon: Record<string, Pokemon> = pokemonJson;
  const params = useParams();
  const currentMon = pokemon[params.pokemonId!];

  return (
    <div id="contact">
      <div id="heading">
        <h1>{currentMon.Name}</h1>
        <i>{currentMon.Kind} Pokémon</i>
      </div>
      <div id="basics">
        <ul>
          <li>{currentMon.Types.join(", ")}</li>
          <li>Height: {currentMon.Height.toFixed(1)} m</li>
          <li>Weight: {currentMon.Weight.toFixed(1)} kg</li>
        </ul>
      </div>

      <div id="entry">
        <p>{currentMon.Pokedex}</p>
      </div>
      <div id="abilities">
        <h2>Abilities</h2>
        {AbilityRender(currentMon)}
      </div>
    </div>
  );
}
