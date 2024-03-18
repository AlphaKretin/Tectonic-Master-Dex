import { Link, Outlet } from "react-router-dom";
import pokemon from "../data/pokemon.json";

export default function Root() {
  const listItems = Object.values(pokemon).map((p) => (
    <li>
      <Link to={`pokemon/${p.InternalName}`}>{p.Name}</Link>
    </li>
  ));
  return (
    <>
      <div id="sidebar">
        <h1>Pokemon Tectonic MasterDex</h1>
        <div>
          <form id="search-form" role="search">
            <input
              id="q"
              aria-label="Search contacts"
              placeholder="Search"
              type="search"
              name="q"
            />
            <div id="search-spinner" aria-hidden hidden={true} />
            <div className="sr-only" aria-live="polite"></div>
          </form>
        </div>
        <nav>
          <ul>{listItems}</ul>
        </nav>
      </div>
      <div id="detail">
        <Outlet />
      </div>
    </>
  );
}
