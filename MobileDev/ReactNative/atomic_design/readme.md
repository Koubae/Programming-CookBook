React-Native | Atomi Design
==========================



Documentation
--------------

- [Atomic Design with React](https://cheesecakelabs.com/blog/atomic-design-react/)



Structure the Project
----------------------



``
.
├── src
│   ├── assets
│   │  ├── fonts
│   │  ├── images
│   ├── components
│   │  ├── atoms
│   │  ├── molecules
│   │  ├── organisms
│   ├── navigations
│   ├── scenes
│   ├── styles
│   ├── utils
│   ├── index.js

``

### configure directory aliases


``
$ yarn add -D eslint-import-resolver-babel-module@^5.1.0
eslint-plugin-import@^2.18.2 babel-plugin-module-resolver@^3.2.0

``
### Configure .babelrc



``
{
  "plugins": [
    [
      "module-resolver",
      {
        "cwd": "babelrc",
        "root": ["./src"],
        "extensions": [".js", ".ios.js", ".android.js"],
        "alias": {
          "_assets": "./src/assets",
          "_components": "./src/components",
          "_atoms": "./src/components/atoms",
          "_molecules": "./src/components/molecules",
          "_organisms": "./src/components/organisms",
          "_navigations": "./src/navigations",
          "_scenes": "./src/scenes",
          "_services": "./src/services",
          "_styles": "./src/styles",
          "_utils": "./src/utils"
        }
      }
    ]
  ]
}

``

### Edit the .eslintrc.j

* [Babel Plugin Module Resolver](https://github.com/tleunen/babel-plugin-module-resolver#getting-started)

``
module.exports = {
        root: true,
        extends: '@react-native-community',
        plugins: ['import'],
        settings: {
            'import/resolver': {
            node: {
                paths: ['src'],
                alias: {
                _assets: './src/assets',
                _components: './src/components',
                _atoms: './src/components/atoms',
                _molecules: './src/components/molecules',
                _organisms: './src/components/organisms',
                _navigations: './src/navigations',
                _scenes: './src/scenes',
                _services: './src/services',
                _styles: './src/styles',
                _utils: './src/utils',
                },
            },
            },
        },
        };
``

# Enable editors to alias autocompletion

Create  jsconfig.json


{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "_assets": ["src/assets/*"],
      "_components": ["src/components/*"],
      "_atoms": ["src/components/atoms/*"],
      "_molecules": ["src/components/molecules/*"],
      "_organisms": ["src/components/organisms/*"],
      "_navigations": ["src/navigations/*"],
      "_scenes": ["src/scenes/*"],
      "_services": ["src/services/*"],
      "_styles": ["src/styles/*"],
      "_utils": ["src/utils/*"]
    }
  }
}
``

# src/index.js` / adding a test component

`` 
import React from 'react';
import {View,Text} from 'react-native';

const App = () => (
  <View>
    <Text>Hello World</Text>
  </View>
);

export default App;

``

#  index.js

`` import App from './src';``



Atomic Design with React.
=========================

* Atoms – The smallest possible components, such as buttons, titles, inputs or event color pallets, animations, and fonts.

* Molecules – They are the composition of one or more components of atoms.

* Organisms – The combination of molecules that work together or even with atoms that compose more elaborate interfaces.

### src/atoms/hello-world.js


`` 
import React from 'react';
import {Text} from 'react-native';

const HelloWorld = ({name}) => <Text>Hello World {name}!</Text>;

export default HelloWorld;
``

### src/atoms/index.js


`` export {default as HelloWorld} from './hello-world';
`` 

### src/index.js

`` 
import React from 'react';
import {HelloWorld} from '_atoms';

const App = () => <HelloWorld name="Helder Burato Berto" />;
export default App;
`` 
**Note: The App.js in the project root can be removed, it will no longer be used.**


Our Scenes
----------

`` 
.
├── src
│   ├── scenes
│   │  ├── login
│   │  │	 ├── index.js // LoginScreen
│   │  ├── home
│   │  │	 ├── index.js // HomeScreen
│   │  ├── about
│   │  │	 ├── index.js // AboutScreen
`` 

### Login 

`` 
import React from 'react';
import {SafeAreaView, Text, TouchableHighlight} from 'react-native';

const LoginScreen = ({navigation}) => (
  <SafeAreaView>
    <Text>Screen: Login</Text>

    <TouchableHighlight onPress={() => navigation.navigate('Home')}>
      <Text>Go to home</Text>
    </TouchableHighlight>
  </SafeAreaView>
);

export default LoginScreen;
`` 


* Add dependency

`` 
$ yarn add react-navigation@^4.0.0 react-navigation-stack@^1.5.3
react-navigation-tabs@^2.4.0 react-native-gesture-handler@^1.4.1
react-native-reanimated@^1.2.0
`` 


### In src/navigations

`` 
.
├── src
│   ├── navigations
│   │  ├── index.js            // RootNavigator
│   │  ├── auth-navigator.js   // AuthNavigator
│   │  ├── app-navigator.js    // AppNavigator
`` 

### auth-navigator.js 

``
import {createStackNavigator} from 'react-navigation-stack';

import LoginScreen from '_scenes/login';

const AuthNavigatorConfig = {
  initialRouteName: 'Login',
  header: null,
  headerMode: 'none',
};

const RouteConfigs = {
  Login:LoginScreen,
};

const AuthNavigator = createStackNavigator(RouteConfigs, AuthNavigatorConfig);

export default AuthNavigator;

`` 

## app-navigator.js

`` 
import {createBottomTabNavigator} from 'react-navigation-tabs';

import HomeScreen from '_scenes/home';
import AboutScreen from '_scenes/about';

const TabNavigatorConfig = {
  initialRouteName: 'Home',
  header: null,
  headerMode: 'none',
};

const RouteConfigs = {
  Home:{
    screen:HomeScreen,
  },
  About:{
    screen:AboutScreen,
  },
};

const AppNavigator = createBottomTabNavigator(RouteConfigs, TabNavigatorConfig);

export default AppNavigator;

`` 

## index.js / RootNavigator merging the auth and app navigators

`` 

import {createAppContainer, createSwitchNavigator} from 'react-navigation';

import AuthNavigator from './auth-navigator';
import AppNavigator from './app-navigator';

const RootNavigator = createSwitchNavigator(
  {
    Auth: AuthNavigator,
    App: AppNavigator,
  },
  {
    initialRouteName: 'Auth',
  },
);

export default createAppContainer(RootNavigator);

`` 

##  import the Navigator object into your src/index.js


`` 

import React from 'react';

import Navigator from '_navigations';

const App = () => <Navigator />;

export default App;

`` 

Shared Styles
------------

``
.
├── src
│   ├── styles
│   │  ├── index.js        // Export all
│   │  ├── colors.js       // Colors pallet
│   │  ├── mixins.js       // Mixins to use CSSinJS
│   │  ├── spacing.js      // Paddings, margins and scale
│   │  ├── typography.js   // Fonts types and sizes

`` 



### index.js
`` 
import * as Colors from './colors';
import * as Spacing from './spacing';
import * as Typography from './typography';
import * as Mixins from './mixins';

export { Typography, Spacing, Colors, Mixins };
`` 

### color.js

`` 

export const PRIMARY = '#1779ba';
export const SECONDARY = '#767676';
export const WHITE = '#FFFFFF';
export const BLACK = '#000000';

// ACTIONS
export const SUCCESS = '#3adb76';
export const WARNING = '#ffae00';
export const ALERT = '#cc4b37';

// GRAYSCALE
export const GRAY_LIGHT = '#e6e6e6';
export const GRAY_MEDIUM = '#cacaca';
export const GRAY_DARK = '#8a8a8a';

`` 

## mixins.js

`` 
import {Dimensions,PixelRatio} from 'react-native';
const WINDOW_WIDTH = Dimensions.get('window').width;
const guidelineBaseWidth = 375;

export const scaleSize = size => (WINDOW_WIDTH/guidelineBaseWidth) * size;

export const scaleFont = size => size * PixelRatio.getFontScale();

function dimensions(top, right = top, bottom = top, left = right, property){
  let styles = {};

  styles[`${property}Top`] = top;
  styles[`${property}Right`] = right;
  styles[`${property}Bottom`] = bottom;
  styles[`${property}Left`] = left;

  return styles;
}

export function margin(top, right, bottom, left){
  return dimensions(top, right, bottom, left, 'margin');
}

export function padding(top, right, bottom, left){
  return dimensions(top, right, bottom, left, 'padding');
}

export function boxShadow(color, offset = {height:2,width:2},
                           radius = 8, opacity = 0.2){
  return {
    shadowColor: color,
    shadowOffset: offset,
    shadowOpacity: opacity,
    shadowRadius: radius,
    elevation: radius,
  };
}
`` 


### spacing.js

``
import {scaleSize} from './mixins';

export const SCALE_18 = scaleSize(18);
export const SCALE_16 = scaleSize(16);
export const SCALE_12 = scaleSize(12);
export const SCALE_8 = scaleSize(8);
``

### typography.js

``
import { scaleFont } from './mixins';

// FONT FAMILY
export const FONT_FAMILY_REGULAR = 'OpenSans-Regular';
export const FONT_FAMILY_BOLD = 'OpenSans-Bold';

// FONT WEIGHT
export const FONT_WEIGHT_REGULAR = '400';
export const FONT_WEIGHT_BOLD = '700';

// FONT SIZE
export const FONT_SIZE_16 = scaleFont(16);
export const FONT_SIZE_14 = scaleFont(14);
export const FONT_SIZE_12 = scaleFont(12);

// LINE HEIGHT
export const LINE_HEIGHT_24 = scaleFont(24);
export const LINE_HEIGHT_20 = scaleFont(20);
export const LINE_HEIGHT_16 = scaleFont(16);

// FONT STYLE
export const FONT_REGULAR = {
  fontFamily: FONT_FAMILY_REGULAR,
  fontWeight: FONT_WEIGHT_REGULAR,
};

export const FONT_BOLD = {
  fontFamily: FONT_FAMILY_BOLD,
  fontWeight: FONT_WEIGHT_BOLD,
};

``

** react-native.config.js in the project root and set the directory where your .ttf files are as follows:**

`` 
module.exports = {
  assets:['./src/assets/fonts/'],
};
`` 