const colors = require("tailwindcss/colors");
const plugin = require("tailwindcss/plugin");

const primary = "red";

module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx}",
    "./src/components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      spacing: {
        0.5: "0.12rem",
        layout: "2.75rem",
      },
      fontSize: {
        "2lg": "1.38rem",
      },
      borderRadius: {
        image: "0.5rem",
        layout: "0.8rem",
      },
      transitionTimingFunction: {
        DEFAULT: "ease-in-out",
      },
      transitionDuration: {
        DEFAULT: "200ms",
      },
      zIndex: {
        1: "1",
        2: "2",
        3: "3",
      },
      keyframes: {
        fade: {
          from: { opacity: 0 },
          to: { opacity: 1 },
        },
        scaleIn: {
          "0%": {
            opacity: 0,
            transform: "scale(0.9)",
          },
          "50%": {
            opacity: 0.3,
          },
          "100%": {
            opacity: 1,
            transform: "scale(1)",
          },
        },
      },
      animation: {
        fade: "fade .5s ease-in-out",
        scaleIn: "scaleIn .35s ease-in-out",
      },
    },
    colors: {
      primary,
      black: colors.black,
      white: colors.white,
      transparent: colors.transparent,
      yellow: colors.yellow,
      gray: colors.gray,
      red: colors.red,
    },
  },
  plugins: [
    plugin(({ addComponents, theme, addUtilities }) => {
      addComponents({
        ".btn-primary": {
          backgroundColor: primary,
          color: "#fff",
          borderRadius: "0.65rem",
          transition: "background-color .3 ease-in-out",
          "&:hover": {
            backgroundColor: "red",
          },
        },
      });
    }),
  ],
};
