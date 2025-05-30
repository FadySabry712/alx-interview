#!/usr/bin/node

const request = require('request');

const Id = process.argv[2];

if (!Id) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${Id}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  function fetchCharacterName(characterUrl, callback) {
    request(characterUrl, (err, res, data) => {
      if (err) {
        callback(err, null);
        return;
      }
      if (res.statusCode !== 200) {
        callback(new Error(`Status code ${res.statusCode}`), null);
        return;
      }
      const character = JSON.parse(data);
      callback(null, character.name);
    });
  }

  let count = 0;
  const names = [];

  characters.forEach((charUrl, idx) => {
    fetchCharacterName(charUrl, (err, name) => {
      if (!err) {
        names[idx] = name;
      } else {
        names[idx] = '';
      }
      count++;
      if (count === characters.length) {
        names.forEach((name) => console.log(name));
      }
    });
  });
});

