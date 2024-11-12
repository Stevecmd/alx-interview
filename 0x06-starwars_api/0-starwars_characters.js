#!/usr/bin/node
// Fetches and prints all characters of a Star Wars movie
const request = require('request');
// Get the movie ID passed as command line argument
const movieId = process.argv[2];
// Construct the API URL for the given movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

request(url, async (error, response, body) => {
  // Check for request error
  if (error) {
    console.error('Error:', error); // Log error to console
    return; // Exit function if error occurs
  }

  // Check if the response status code indicates a successful request
  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie:', response.statusCode); // Log failure message with status code
    return; // Exit function if the request was unsuccessful
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  // Iterate over the characters API URLs
  for (const characterUrl of characters) {
    try {
      const characterName = await getCharacterName(characterUrl);
      console.log(characterName);
    } catch (err) {
      console.error('Error:', err);
    }
  }
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
