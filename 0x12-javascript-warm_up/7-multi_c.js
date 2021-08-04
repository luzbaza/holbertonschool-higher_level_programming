#!/usr/bin/node
/* script that prints x times “C is fun" */
const i = parseInt(process.argv[2]);
if (isNaN(i)) {
  console.log('Missing number of occurrences');
} else {
  for (let j = 0; j < i; j++) {
    console.log('C is fun');
  }
}
