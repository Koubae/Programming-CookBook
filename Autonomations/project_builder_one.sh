#!/bin/bash

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

./backend.sh &
PIDS[0]=$!
./front_end/compile.sh &
PIDS[1]=$!
./front_end/build.sh &
PIDS[2]=$!

trap "kill ${PIDS[*]}" SIGINT

wait
EOF

   # Create shell script for running CodeIgniter as well; commented as default
   cat <<EOF >./backend.sh
#!/bin/bash

#composer run-script start-dev
#gnome-terminal -e "composer run-script start-dev"
EOF

      # Creating Scripts to easy run React and its build (PRO)
    cat <<EOF >./app_builder_pro.sh
#!/bin/bash -e

./backend.sh &
PIDS[0]=$!
./front_end/compile_prod.sh &
PIDS[1]=$!
./front_end/build_prod.sh &
PIDS[2]=$!

trap "kill ${PIDS[*]}" SIGINT

wait
EOF

    # Create Front End directory
    mkdir front_end; cd front_end;

    # Babale presets
    cat <<EOF >./.babelrc
{
  "presets": ["react-app"]
}
EOF

  # Run Web-Pack Build (DEV)
  cat <<EOF >./build.sh
#!/bin/bash

npm run pack-dev --prefix ./front_end
#gnome-terminal -e "npm run pack-dev --prefix ./front_end"
EOF
      # Run Web-Pack Build (PRO)
    cat <<EOF >./build_prod.sh
#!/bin/bash

npm run build --prefix ./front_end
#gnome-terminal -e "npm run pack-dev --prefix ./front_end"
EOF
    # Babel profile (DEV)
      cat <<EOF >./compile.sh
#!/bin/bash

npm run watcher-babel --prefix ./front_end

#gnome-terminal -e "npm run watcher-babel --prefix ./front_end"
EOF

    # Babel profile (PRO)
    cat <<EOF >./compile_prod.sh
#!/bin/bash

npm run watcher-babel-prod --prefix ./front_end

#gnome-terminal -e "npm run watcher-babel --prefix ./front_end"
EOF

  # WebPack Dev
  cat <<EOF >./webpack.config.js

const path = require('path');

module.exports = {
    entry: './src_compiled/index.js',
    devtool: 'inline-source-map',
    output: {
        filename: 'build.js',
        path: path.resolve(__dirname, '../public/static/js'),
        clean: true,
    },
    mode: 'development',
    watch: true,
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

  # WebPack Production
  cat <<EOF >./webpack.production.config.js

const path = require('path');

module.exports = {
    entry: './src_compiled/index.js',
    devtool: 'source-map',
    output: {
        filename: 'build.js',
        path: path.resolve(__dirname, '../public/static/js'),
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

// module.exports = {
//     entry: './src_compiled/index.js',
//     devtool: 'source-map',
//     output: {
//         filename: 'build.js',
//         path: path.resolve(__dirname, '../public/static/js'),
//         clean: true,
//     },
//     mode: 'production',
//     watch: false,
//     plugins: [
//         new MiniCssExtractPlugin({
//             filename: "[name].css",
//         }),
//     ],
//     module: {
//         rules: [
//             {
//                 test: /\.css$/i,
//                 use: [MiniCssExtractPlugin.loader,  "css-loader"],
//             },
//         ],
//     },
//     optimization: {
//         splitChunks: {
//             cacheGroups: {
//                 styles: {
//                     name: "styles",
//                     type: "css/mini-extract",
//                     chunks: "all",
//                     enforce: true,
//                 },
//             },
//         },
//     },
//
//
// };

EOF

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

  declare -A npmPackageToInstall=(
      ["react" ]="pro"
      ["react-dom" ]="pro"

      ["css-loader" ]="dev"
      ["style-loader" ]="dev"
      ["babel-cli" ]="dev"
      ["babel-preset-react-app" ]="dev"
      ["webpack" ]="dev"
      ["webpack-cli" ]="dev"
    )
  for package in "${!npmPackageToInstall[@]}";
     do
        if [ ${npmPackageToInstall[$package]} == 'dev' ]
          then echo "Installing NPM Package $package as dev dependency ...."; eval "npm i $package --save-dev";
          else echo "Installing NPM Package $package ...."; eval "npm i $package";
        fi;
  done;
  echo "Creating Example NPM Package, containigs the scripts for building your app";


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
    "watcher-babel": "NODE_ENV=development npx babel --watch src --out-dir ./src_compiled --presets react-app/prod --copy-files --source-maps",
    "pack-dev": "webpack",
    "build-test": "npm run dev && npm run watcher-babel",
    "watcher-babel-prod": "BABEL_ENV=production NODE_ENV=production npx babel --watch src --out-dir ./src_compiled --presets react-app/prod --copy-files --source-maps",
    "build": "webpack --config ./webpack.production.config.js"
  },
  "author": "",
  "license": "MIT",
  "dependencies": {
    "babel-cli": "^6.26.0",
    "babel-preset-react-app": "^3.1.2",
    "bootswatch": "^5.1.3",
    "react": "^17.0.2",
    "react-dom": "^17.0.2"
  },
  "devDependencies": {
    "css-loader": "^6.6.0",
    "style-loader": "^3.3.1",
    "webpack": "^5.69.1",
    "webpack-cli": "^4.9.2"
  }
}
EOF
}

setUpReactSimple;


