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

export default function Pokemon() {
  const pokemon: Record<string, Pokemon> = pokemonJson;
  const params = useParams();
  const currentMon = pokemon[params.pokemonId!];

  return (
    <div id="contact">
      <div>
        <h1>{currentMon.Name}</h1>
      </div>
    </div>
  );
}
