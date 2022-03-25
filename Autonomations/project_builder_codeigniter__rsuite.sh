#!/bin/bash
# TODO:
installCodeIgniter() {
  echo " ------------ < Installing CodeIgniter > -------------- ";
  if [ -n "$1" ]
    then project_name="$1";
  else  read -p "Enter Project Name: " project_name;
  fi;
  echo " Project name sat to $project_name ";
  echo "Installing with command 'create-project codeigniter4/appstarter ci-news'....";
  composer create-project codeigniter4/appstarter $project_name

  echo " Writing Composer Example (Here important are the scripts)";
   cat <<EOF >./composer_example.json
{
   "name": "koubae/appstarterReady",
   "type": "project",
   "description": "Koubae starter app",
   "homepage": "https://codeigniter.com",
   "license": "MIT",
   "require": {
       "php": "^7.3 || ^8.0",
       "codeigniter4/framework": "^4"
   },
   "require-dev": {
       "fakerphp/faker": "^1.9",
       "mikey179/vfsstream": "^1.6",
       "phpunit/phpunit": "^9.1"
   },
   "suggest": {
       "ext-fileinfo": "Improves mime type detection for files"
   },
   "autoload": {
       "psr-4": {
           "App\\": "app",
           "Config\\": "app/Config"
       },
       "exclude-from-classmap": [
           "**/Database/Migrations/**"
       ]
   },
   "autoload-dev": {
       "psr-4": {
           "Tests\\Support\\": "tests/_support"
       }
   },
   "scripts": {
       "start-dev": [
           "Composer\\Config::disableProcessTimeout",
           "php spark serve "
       ],
       "test": "phpunit"
   },
   "support": {
       "forum": "http://forum.codeigniter.com/",
       "source": "https://github.com/codeigniter4/CodeIgniter4",
       "slack": "https://codeigniterchat.slack.com"
   }
}
EOF


}
installCodeIgniter $@

function createBuildsScripts() {
  echo "Creating React Scripts into your project ....";
    # Creating Scripts to easy run React and its build (DEV)
    cat <<EOF >./app_builder_dev.sh
#!/bin/bash -e
NODE_ENV=development
./backend.sh &
PIDS[0]=$!
./front_end/compile.sh &
PIDS[1]=$!
./front_end/build.sh &
PIDS[2]=$!

trap "kill ${PIDS[*]}" SIGINT

wait
EOF

  chmod +777 app_builder_dev.sh

   # Create shell script for running CodeIgniter as well; commented as default
   cat <<EOF >./backend.sh
#!/bin/bash

#composer run-script start-dev
#gnome-terminal -e "composer run-script start-dev"
EOF
  chmod +777 backend.sh

      # Creating Scripts to easy run React and its build (PRO)
    cat <<EOF >./app_builder_pro.sh
#!/bin/bash -e
NODE_ENV=production
./backend.sh &
PIDS[0]=$!
./front_end/compile_prod.sh &
PIDS[1]=$!
./front_end/build_prod.sh &
PIDS[2]=$!

trap "kill ${PIDS[*]}" SIGINT

wait
EOF

  chmod +777 app_builder_pro.sh

    # Create Front End directory
    mkdir front_end; cd front_end;

    # Babale presets
    cat <<EOF >./.babelrc.js

module.exports = api => {
  api.cache(() => process.env.NODE_ENV);

  return {
    presets: ['@babel/preset-env', '@babel/preset-react'],
  };
};

EOF
  chmod +777 .babelrc.js

  # Run Web-Pack Build (DEV)
  cat <<EOF >./build.sh
#!/bin/bash

npm run pack-dev --prefix ./front_end
#gnome-terminal -e "npm run pack-dev --prefix ./front_end"
EOF
  chmod +777 build.sh
      # Run Web-Pack Build (PRO)
    cat <<EOF >./build_prod.sh
#!/bin/bash

npm run build --prefix ./front_end
#gnome-terminal -e "npm run pack-dev --prefix ./front_end"
EOF
    chmod +777 build_prod.sh
    # Babel profile (DEV)
      cat <<EOF >./compile.sh
#!/bin/bash

npm run watcher-babel --prefix ./front_end

#gnome-terminal -e "npm run watcher-babel --prefix ./front_end"
EOF

  chmod +777 compile.sh

    # Babel profile (PRO)
    cat <<EOF >./compile_prod.sh
#!/bin/bash

npm run watcher-babel-prod --prefix ./front_end

#gnome-terminal -e "npm run watcher-babel --prefix ./front_end"
EOF

  chmod +777 compile_prod.sh
  # WebPack Dev
  cat <<EOF >./webpack.config.js
const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    entry: './src_compiled/index.js',
    devtool: 'inline-source-map',
    output: {
        filename: 'build.js',
        path: path.resolve(__dirname, '../public/static/js'),
        publicPath: 'public_html',
        clean: true,
    },
    mode: 'development',
    watch: true,
    module: {
        rules: [
          {
            test: /\.(less|css)$/,
            use: [
              {
                loader: MiniCssExtractPlugin.loader
              },
              'css-loader',
              'less-loader?javascriptEnabled=true'
            ]
          }
        ]
      },
    plugins: [
      new MiniCssExtractPlugin({
        filename: '[name].css',
        chunkFilename: '[id].css'
      })
    ]

};

EOF

  chmod +777 webpack.config.js

  # WebPack Production
  cat <<EOF >./webpack.production.config.js

const path = require('path');

module.exports = {
    entry: './src_compiled/index.js',
    devtool: 'source-map',
    output: {
        filename: 'build.js',
        path: path.resolve(__dirname, '../public/static/js'),
        publicPath: 'public_html'
        clean: true,
    },
    mode: 'production',
    watch: false,
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: ["style-loader", "css-loader"],
            },
        ],
    },


};



EOF

  chmod +777 webpack.production.config.js

  echo "React Script Ready!";

}

function setUpReactSimple()  {
    echo " ------------ < Installing React > -------------- ";
  # Create Build scripts
   createBuildsScripts;
  # todo: npm init with the project name
  echo "Preparing Node Packages";
  npm init -y
  echo "Done.\n Installing NPM packages";


   echo " ------------ < Installing React END. Enjoy > -------------- ";
   cat <<EOF >./package_example.json
{
  "name": "Koubae Generator",
  "version": "1.0.0",
  "description": "TODO",
  "private": true,
  "directories": {
    "test": "tests"
  },
  "scripts": {
    "preinstall": "cd $(pwd)",
    "test": "echo \"Error: no test specified\" && exit 1",
    "watcher-babel": "BABEL_ENV=development npx babel --watch src --out-dir ./src_compiled  --copy-files --source-maps",
    "pack-dev": "webpack",
    "build-test": "npm run dev && npm run watcher-babel",
    "watcher-babel-prod": "BABEL_ENV=production NODE_ENV=production npx babel --watch src --out-dir ./src_compiled --copy-files --source-maps",
    "build": "webpack --config ./webpack.production.config.js"
  },
  "author": "",
  "license": "MIT",
   "dependencies": {
      "react": "latest",
      "react-dom": "latest",
      "rsuite": "latest",


  },
  "devDependencies": {
    "babel": "^6.23.0"
    "babel-cli": "^6.26.0",
    "@babel/core": "latest",
    "@babel/plugin-proposal-class-properties": "latest",
    "@babel/preset-env": "latest",
    "@babel/preset-react": "latest",
    "babel-loader": "latest",
    "babel-plugin-lodash": "latest",
    "babel-preset-rsuite": "latest",
    "css-loader": "latest",
    "html-webpack-plugin": "latest",
    "less": "latest",
    "less-loader": "latest",
    "lodash-webpack-plugin": "latest",
    "mini-css-extract-plugin": "^0.4.3",
    "optimize-css-assets-webpack-plugin": "^5.0.1",
    "style-loader": "^0.20.3",
    "uglifyjs-webpack-plugin": "^2.0.1",
    "webpack": "^4.20.2",
    "webpack-cli": "^3.1.2",
  }
}
EOF

  declare -A npmPackageToInstall=(
        ["react" ]="pro"
        ["react-dom" ]="pro"
        ["rsuite" ]="pro"

        ["babel-cli@6" ]="dev"
        ["babel-preset-react-app@3" ]="dev"        
        [ "css-loader" ]="dev"
        [ "html-webpack-plugin" ]="dev"
        ["less" ]="dev"
        ["less-loader" ]="dev"
        ["lodash-webpack-plugin" ]="dev"
        ["mini-css-extract-plugin"]="dev"
        [ "style-loader"]="dev"
        ["webpack"]="dev"
        ["webpack-cli"]="dev"
        ["npm-add-script"]="dev" # enables add scripts programmaticallty
    )
    for package in "${!npmPackageToInstall[@]}";
       do
          if [ ${npmPackageToInstall[$package]} == 'dev' ]
            then echo "Installing NPM Package $package as dev dependency ...."; eval "npm i $package --save-dev";
            else echo "Installing NPM Package $package ...."; eval "npm i $package";
          fi;
    done;
    echo "Add Scripts to npm package.json... ";

    npx npm-add-script \
      -k "watcher-babel" \
      -v "BABEL_ENV=development npx babel --watch src --out-dir ./src_compiled  --copy-files --source-maps" \
      --force;

    npx npm-add-script \
      -k "pack-dev" \
      -v "webpack" \
      --force;

    npx npm-add-script \
      -k "build-test" \
      -v "npm run dev && npm run watcher-babel" \
      --force;

    npx npm-add-script \
      -k "watcher-babel-prod" \
      -v "BABEL_ENV=production NODE_ENV=production npx babel --watch src --out-dir ./src_compiled --copy-files --source-maps" \
      --force;

    npx npm-add-script \
      -k "build" \
      -v "webpack --config ./webpack.production.config.js" \
      --force;

    echo "Creating .eslintrc.json";
    cat <<EOF >./.eslintrc.json
    {
      "parserOptions": {
        "ecmaVersion": 6
      }
    }
EOF
      chmod +777 .eslintrc.json
    echo "Creating .prettierrc"
    cat <<EOF >./.prettierrc
    {
      "printWidth": 100,
      "tabWidth": 2,
      "singleQuote": true
    }
EOF
          chmod +777 .prettierrc
  echo "Creating .gitignore"
      cat <<EOF >./.gitignore
      node_modules
      src_compiled
EOF

  echo "Creating React Source Folder";
  mkdir src;
  cd src;
  cat <<EOF >./index.js
  'use strict';

  import React, { useState, useEffect } from 'react';
  import ReactDOM from 'react-dom';

  import App from './App';

  /**
   * Allow Libs to load
   */
  window.addEventListener('DOMContentLoaded', (event) => {
      const ROOT = document.getElementById('root');
      ReactDOM.render(
          <React.StrictMode>
              <App/>
          </React.StrictMode>
          , ROOT
      );
  });
EOF

  cat <<EOF >./App.js
"use strict";

import React from "react";

const App = () => {

return (
<div>
    <h1> Hello world </h1>
</div>
)};

export default App;
EOF

  mkdir Components;
  mkdir Config;
  mkdir Layouts;
  mkdir Utils;
  mkdir Views;
  mkdir styles;
  mkdir tools;
}


setUpReactSimple;


