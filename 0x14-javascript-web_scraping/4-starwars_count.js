#!/usr/bin/node
// a script that prints the number of movies
// where the character “Wedge Antilles” is present.

const request = require("request");
const cmdArgs = process.argv.slice(2);
let request_url = "https://swapi-api.alx-tools.com/api/films"

request_url = cmdArgs.length > 0 ? cmdArgs[0] : request_url;

const getMovies = async () => {
  return new Promise((resolve, reject) => {
    request(request_url, (err, res) => {
      if (err) {
        reject(err);
      }
      let body = JSON.parse(res.body);
      resolve(body);
    });
  });
};

(async () => {
  let movie = await getMovies();
  if (movie.results && Array.isArray(movie.results)) {
    movie.results = movie.results.filter(result => result.characters.some(char => {
      reg_test = /.*18\/$/
      return char.match(reg_test)
    }))
  }
  console.log(movie.results.length)
})();
