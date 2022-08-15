import { useAuth0 } from "@auth0/auth0-react";

export const NavBar = (): JSX.Element => {
  const { user, isAuthenticated, isLoading } = useAuth0();

  if (isLoading) {
    return <div>Loading...</div>
  }

  return (
    isAuthenticated && user ? (
      <p>Logged in as {user.name} ({user.email})</p>
    ) : (
      <p>Logged out</p>
    )
  );
};
