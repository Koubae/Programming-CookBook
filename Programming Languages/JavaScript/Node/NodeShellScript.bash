# Collection of Node Command line commands 
# run Node
node app.js 

# Environment Variables
# The below code runs app.js and set USER_ID and USER_KEY.
USER_ID=239482 USER_KEY=foobar node app.js
# Create .env fiel in root dit , use dotenv to load in runtime --> https://www.npmjs.com/package/dotenvç
#  run node -r dotenv/config index.js, have dotenv installed globally but not in the project
# .env file
USER_ID="239482"
USER_KEY="foobar"
NODE_ENV="development"

# Signal Node.js that you are running in production
export NODE_ENV=production
#or 
NODE_ENV=production node app.js



# Installing Dependencies

# If a project has a package.json file, by running
npm install

# install & start
npm install & npm start

# Install a single package
npm install <package-name>

# global install 
npm install -g <package-name>
# Gives the directory of the Global Nodes modules
npm root -g

#  see the version of all installed npm packages, including their dependencie
# StackOverflow --> https://stackoverflow.com/a/70243395/13903942
npm list
npm list -g # global flag
# /Users/joe/dev/node/cowsay
# └─┬ cowsay@1.3.1
#   ├── get-stdin@5.0.1
#   ├─┬ optimist@0.6.1
#   │ ├── minimist@0.0.10
#   │ └── wordwrap@0.0.3
#   ├─┬ string-width@2.1.1
#   │ ├── is-fullwidth-code-point@2.0.0
#   │ └─┬ strip-ansi@4.0.0
#   │   └── ansi-regex@3.0.0
#   └── strip-eof@1.0.0

# get only your top-level packages
npm list --depth=0
# get the version of a specific package
npm list <package-name>
# see what's the latest available version of the package
npm view <package-name> version


# flags
--save-dev : installs and adds the entry to the package.json file devDependencies
--no-save :  installs but does not add the entry to the package.json file dependencies
--save-optional : installs and adds the entry to the package.json file optionalDependencies
--no-optional : will prevent optional dependencies from being installed
#Shorthands of the flags can also be used:
# -S: --save
# -D: --save-dev
# -O: --save-optional

# Debugging
# Mode options https://nodejs.org/en/docs/guides/debugging-getting-started/#command-line-options
node --inspect # default 127.0.0.1
# A minimal CLI debugger 
node inspect myscript.js