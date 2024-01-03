#!/usr/bin/node
// a script that computes the number of tasks completed by user id.

const request = require("request");
const cmdArgs = process.argv.slice(2);
const users_obj = {}
let requestUrl;

if (cmdArgs.length < 1) {
  console.log("wrong number of input arguments. requires at least 1");
  process.exit(98);
}

requestUrl = cmdArgs[0];

const fetchEndpoint = async () => {
  return new Promise((resolve, reject) => {
    request(requestUrl, (err, res) => {
      if (err) {
        reject(err);
      }
      let body = JSON.parse(res.body);
      resolve(body);
    });
  });
};

(async () => {
	response = await fetchEndpoint();
  for (let todo of response) {
    if (todo.completed) {
      if (!(users_obj.hasOwnProperty(todo.userId))) {
        console.log(todo.userId);
        users_obj[todo.userId] = 1;
      }
      else {
        users_obj[todo.userId] = users_obj[todo.userId] + 1;
      }
    }
  }
	console.log(users_obj);
})();
