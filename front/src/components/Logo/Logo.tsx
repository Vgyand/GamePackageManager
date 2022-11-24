import styles from "./Logo.module.scss";
import logo from "assets/logo.png";
import { Link } from "react-router-dom";

const Logo = () => {
  return (
    <Link to="/">
      <img className={styles.logo} src={logo} alt="cringe" />
    </Link>
  );
};

export default Logo;
