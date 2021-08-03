#!/usr/bin/node
/* first argument can be converted to an integer */

if (!parseInt(process.argv[2])) { // parseInt: conviert de str to int
  console.log('Not a number');
} else {
  console.log('My number: %d', parseInt(process.argv[2]));
}
