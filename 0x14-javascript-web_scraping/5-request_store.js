#!/usr/bin/node
// this script gets the contents of a webpage and stores it in a file

const fs = require("fs");
const request = require("request");

const cmdArgs = process.argv.slice(2);

if (cmdArgs.length < 2) {
  console.log("wrong number of input arguments. requires at least 2");
  process.exit(98);
}

let requestUrl = cmdArgs[0];
let filePath = cmdArgs[1];

const writeFileAsync = (filePath, content, encoding) => {
  return new Promise((resolve, reject) => {
    fs.writeFile(filePath, `${content}\n`, encoding, (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
};

const fetchEndpoint = async () => {
  return new Promise((resolve, reject) => {
    request(requestUrl, (err, res) => {
      if (err) {
        reject(err);
      }
      let body = res.body;
      resolve(body);
    });
  });
};

const fetchAndWrite = async () => {
  let body = await fetchEndpoint();
  await writeFileAsync(filePath, body, "utf8");
};

(async () => {
  try {
    await fetchAndWrite();
  } catch (err) {
    console.error(err);
  }
})();