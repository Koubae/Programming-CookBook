// Source --> https://jakearchibald.com/2016/streams-ftw/

// fetch() returns a promise that
// resolves once headers have been received
fetch(url).then((response) => {
  // response.body is a readable stream.
  // Calling getReader() gives us exclusive access to
  // the stream's content
  var reader = response.body.getReader();
  var bytesReceived = 0;

  // read() returns a promise that resolves
  // when a value has been received
  return reader.read().then(function processResult(result) {
    // Result objects contain two properties:
    // done  - true if the stream has already given
    //         you all its data.
    // value - some data. Always undefined when
    //         done is true.
    if (result.done) {
      console.log('Fetch complete');
      return;
    }

    // result.value for fetch streams is a Uint8Array
    bytesReceived += result.value.length;
    console.log('Received', bytesReceived, 'bytes of data so far');

    // Read some more, and call this function again
    return reader.read().then(processResult);
  });
});