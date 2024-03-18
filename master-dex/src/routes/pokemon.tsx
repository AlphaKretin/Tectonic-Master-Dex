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
  const bst = Object.values(currentMon.BaseStats).reduce((a, b) => a + b, 0);

  let wildItems: string | undefined;

  return (
    <div id="contact">
      <div id="heading">
        <h1>{currentMon.Name}</h1>
        <i>{currentMon.Kind} Pokémon</i>
      </div>
      <div className="flexbox-container">
        <div id="image">
          <img
            src={`https://raw.githubusercontent.com/xeuorux/Pokemon-Tectonic/main/Graphics/Pokemon/Front/${currentMon.InternalName}.png`}
          ></img>
        </div>
        <div id="basics">
          <ul>
            <li>{currentMon.Types.join(", ")}</li>
            <li>Height: {currentMon.Height.toFixed(1)} m</li>
            <li>Weight: {currentMon.Weight.toFixed(1)} kg</li>
          </ul>
        </div>
      </div>
      <div id="entry">
        <p>{currentMon.Pokedex}</p>
      </div>
      <div id="abilities">
        <h2>Abilities</h2>
        {AbilityRender(currentMon)}
      </div>
      <div id="stats">
        <div className="flexbox-container">
          <div id="base-stats">
            <h2>Base Stats</h2>
            <table>
              <tr>
                <th>HP</th>
                <td>{currentMon.BaseStats.hp}</td>
              </tr>
              <tr>
                <th>Attack</th>
                <td>{currentMon.BaseStats.attack}</td>
              </tr>
              <tr>
                <th>Defense</th>
                <td>{currentMon.BaseStats.defense}</td>
              </tr>
              <tr>
                <th>Sp. Atk</th>
                <td>{currentMon.BaseStats.sp_atk}</td>
              </tr>
              <tr>
                <th>Sp. Def</th>
                <td>{currentMon.BaseStats.sp_def}</td>
              </tr>
              <tr>
                <th>Speed</th>
                <td>{currentMon.BaseStats.speed}</td>
              </tr>
              <tr>
                <th>Total</th>
                <td>{bst}</td>
              </tr>
            </table>
          </div>

          <div id="other-stats">
            <h2>Other Stats</h2>
            <table>
              <tr>
                <th>Gender Rate</th>
                <td>{currentMon.GenderRate}</td>
              </tr>
              <tr>
                <th>Growth Rate</th>
                <td>{currentMon.GrowthRate}</td>
              </tr>
              <tr>
                <th>Catch Rate</th>
                <td>{currentMon.CatchRate}</td>
              </tr>
              <tr>
                <th>Experience Granted</th>
                <td>{currentMon.BaseEXP}</td>
              </tr>
              <tr>
                <th>Physical EHP</th>
                <td>000</td>
              </tr>
              <tr>
                <th>Special EHP</th>
                <td>000</td>
              </tr>
            </table>
          </div>
        </div>
        <h3>Wild Held Items</h3>
        {wildItems || "None"}
      </div>
    </div>
  );
}
