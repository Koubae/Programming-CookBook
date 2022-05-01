//Install 
/*
npm install eslint --save-dev
npm install --save-dev eslint-plugin-react
*/


module.exports = {
    'env': {
        'browser': true,
        'es6': true,
        'jest': true
    },
    'parser': 'babel-eslint',
    'parserOptions': {
        'ecmaFeatures': {
            'ecmaVersion': 8,
            'experimentalObjectRestSpread': true,
            'jsx': true,
        },
        'sourceType': 'module',
    },
    'plugins': ['react', 'react-native'],
    'rules': {
        'arrow-parens': ['error', 'as-needed', {
            'requireForBlockBody': true
        }],
        'react/jsx-props-no-spreading': 'off',
        'react/jsx-sort-props': ['error', {
            'reservedFirst': ['key']
        }],
        'react/require-default-props': 'off',
        'react/sort-prop-types': 'error',
        'react/state-in-constructor': ['error', 'never'],
        'semi-spacing': 'warn',
        'indent': ['warn', 4, { 'SwitchCase': 1 }],
        'semi': ['error', 'always'],
        'linebreak-style': ['error', 'unix'],
        'no-undef': ['error'],
        'no-console': ['off'],
        'no-unused-vars': ['warn'],
        'react/prop-types': ['warn'],
        'react-native/no-unused-styles': ['warn'],
        'react-native/split-platform-components': ['warn'],
        'react-native/no-inline-styles': ['warn'],
        'react-native/no-color-literals': ['off'],
    },
    'overrides': [
        {
            'files': [
                'sample/**',
                'test/**'
            ],
            'rules': {
                'import/no-unresolved': 'off'
            }
        }
    ]
};
// module.exports = {
//   root: true,
//   extends: '@react-native-community',
// };

