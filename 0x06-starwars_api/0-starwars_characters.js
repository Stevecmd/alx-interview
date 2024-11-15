#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

request(url, (error, response, body) => {
  // Check for request error
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Check if the response status code indicates a successful request
  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie:', response.statusCode);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  // Create an array of promises for fetching character names
  const characterPromises = characters.map(characterUrl => getCharacterName(characterUrl));

  // Wait for all promises to resolve
  Promise.all(characterPromises)
    .then(names => {
      names.forEach(name => console.log(name)); // Print each character name
    })
    .catch(err => {
      console.error('Error fetching character names:', err);
    });
});

// Function to fetch character name from API URL
function getCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch character: ${response.statusCode}`));
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
}
