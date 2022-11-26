import { IHelmet } from "../shared/helmet";
import Helmet from "react-helmet";

const Meta = ({ title, desc, children }: IHelmet) => {
  return (
    <>
      <Helmet>
        <meta charSet="utf-8" />
        <title>{title}</title>
        <meta name="desctiption" content={desc} />
        <link rel="canonical" href="http://cringesvoyak.com/example" />
        <script
          src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
          integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4"
        ></script>
      </Helmet>
      {children}
    </>
  );
};

export default Meta;
