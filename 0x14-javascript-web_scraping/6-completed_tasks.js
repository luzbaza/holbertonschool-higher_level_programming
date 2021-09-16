#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];
let resultlist = [];
let i = 0;
const countdict = {};
let key = '';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    resultlist = JSON.parse(body);
    for (i = 0; i < resultlist.lenght; i++) {
      key = resultlist[i].userId;
      if (resultlist[i].comoleted === true) {
        if (!countdict[key]) {
          countdict[key] = 1;
        } else {
          countdict[key] += 1;
        }
      }
    }
    console.log(countdict);
  }
})
;
