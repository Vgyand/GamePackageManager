import "./index.scss";
import Meta from "./services/Meta";
import MainPage from "pages/MainPage/MainPage";
import React from "react";
import { createRoot } from "react-dom/client";

const container = document.getElementById("root")!;
const root = createRoot(container);

root.render(
  <React.StrictMode>
    <Meta title="Cringe Svoyak" desc="Downloable packs">
      <MainPage />
    </Meta>
  </React.StrictMode>
);
