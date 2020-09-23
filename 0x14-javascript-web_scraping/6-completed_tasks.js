#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const obj = {};
request(url, (err, res, body) => {
  if (err) { console.log(err); }
  const taskList = JSON.parse(body);
  taskList.forEach((task) => {
    if (!obj[task.userId] && task.completed) {
      obj[task.userId] = 0;
    }
    if (task.completed) {
      obj[task.userId]++;
    }
  });
  console.log(obj);
});
