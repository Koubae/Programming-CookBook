try {
    console.log(require.resolve("moment-timezone"));
} catch(e) {
    console.error("moment-timezone is not found");
    // process.exit(e.code);
}