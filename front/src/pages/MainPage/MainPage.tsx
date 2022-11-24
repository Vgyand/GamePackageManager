import styles from "./MainPage.module.scss";
import ContentWrapper from "components/ContentWrapper/ContentWrapper";

const MainPage = () => {
  return (
    <div className="mx-auto max-w-5xl container">
      <div className="grid grid-cols-12 mx-auto">
        <div className={styles.logo}>logo</div>
        <div className={styles.content}>
          <ContentWrapper />
        </div>
        <div className={styles.filter}>filters</div>
      </div>
    </div>
  );
};

export default MainPage;
