#!/usr/bin/node
//  script that writes a string to a file

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
})
;
