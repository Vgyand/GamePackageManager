import "./index.scss";
import Meta from "./services/Meta";
import MainPage from "pages/MainPage/MainPage";
import React from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";

const container = document.getElementById("root")!;
const root = createRoot(container);

root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Meta title="Cringe Svoyak" desc="Downloable packs">
        <MainPage />
      </Meta>
    </BrowserRouter>
  </React.StrictMode>
);
