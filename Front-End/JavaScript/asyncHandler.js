// StackOVerflow Answer -> https://stackoverflow.com/a/70318671/13903942
function promiseHandle(promise) {
    return promise
            .then(data => [null, data])
            .catch(err => [err]);
}



async function asyncFunc(param1, param2) {
    const [err, data] = await promiseHandle(expensiveFunction(param1, param2));
    // This just to show, that in this way we can control what is going on..
    if (err || !data) {
        if (err) return Promise.reject(`Error but not data..`);
        return Promise.reject(`Error but not data..`);
    }
    return Promise.resolve(data);

}