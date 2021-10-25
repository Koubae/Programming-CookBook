//Install 
/*
npm install eslint --save-dev
npm install --save-dev eslint-plugin-react
*/


module.exports = {
  "parser": "babel-eslint",
  "env": {
    "browser": true,
    "es6": true,
    "jest": true
  },

  "rules": {
    "arrow-parens": ["error", "as-needed", {
      "requireForBlockBody": true
    }],
    "react/jsx-props-no-spreading": "off",
    "react/jsx-sort-props": ["error", {
      "reservedFirst": ["key"]
    }],
    "react/require-default-props": "off",
    "react/sort-prop-types": "error",
    "react/state-in-constructor": ["error", "never"],
    "semi-spacing": "warn"
  },
  "overrides": [
    {
      "files": [
        "sample/**",
        "test/**"
      ],
      "rules": {
        "import/no-unresolved": "off"
      }
    }
  ]
};

// module.exports = {
//   root: true,
//   extends: '@react-native-community',
// };

