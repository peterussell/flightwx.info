import { Link } from 'react-router-dom';

const LandingPage = () => {
  return (
    <>
      <h1>Welcome to FlightWX</h1>
      <h3>Aviation weather.</h3>
      <Link to="/login">Log In</Link>
    </>
  )
}

export default LandingPage;
