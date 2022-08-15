import { LoginButton, LogoutButton } from "features/login/components";

const LoginPage = () => {
  return (
    <>
      <h1>Log in to FlightWX</h1>
      <div><LoginButton /></div>
      <div><LogoutButton /></div>
    </>
  )
};

export default LoginPage;
