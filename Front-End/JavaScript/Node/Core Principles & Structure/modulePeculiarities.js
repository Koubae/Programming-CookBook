/**
Credit: https://stackoverflow.com/a/62892482/13903942

Docs:  https://nodejs.org/api/esm.html 
https://nodejs.org/docs/latest-v15.x/api/esm.html#esm_no_require_exports_or_module_exports


*/ 


/*
If you are using Node.js modules, __dirname and __filename don't exist.
From the Node.js documentation:
No require, exports, module.exports, __filename, __dirname
These CommonJS variables are not available in ES modules.
require can be imported into an ES module using module.createRequire().
Equivalents of __filename and __dirname can be created inside of each file via import.meta.url:
*/

import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
// https://nodejs.org/docs/latest-v15.x/api/esm.html#esm_no_filename_or_dirname