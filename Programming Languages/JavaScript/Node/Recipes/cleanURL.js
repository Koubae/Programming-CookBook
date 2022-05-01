function cleanURL(url) {
    /*Remove trailing Slashes to the given URL */
   return url.replace(/^\/+|\/+$/g, '');
}