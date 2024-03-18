import { useRouteError } from "react-router-dom";

export default function ErrorPage() {
  const error = useRouteError();
  console.error(error);
  let message: string;
  //if ("statusText" in error) message = error.statusText;
  if (error instanceof Error) message = error.message;
  else message = "oops";
  return (
    <div id="error-page">
      <h1>Oops!</h1>
      <p>Sorry, an unexpected error has occurred.</p>
      <p>
        <i>{message}</i>
      </p>
    </div>
  );
}
