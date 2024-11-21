import React from "react";
import EntranceForm from "./components/EntranceForm/EntranceForm";
import Body from "./components/Body/Body";

function App() {
  //состояние авторизованности пользователя
  const [authorized, setAuthorized] = React.useState(false);

  //пользователь вошёл в систему
  const handleAuthorize = () => {
    setAuthorized(true);
  };

  return authorized === false ? (
    <EntranceForm onAuthorize={handleAuthorize} />
  ) : (
    <Body />
  );
}

export default App;
