#!/usr/bin/node

// Fetches and prints all characters of a Star Wars movie
const request = require('request');

// Check if the user passed a movie ID as argument
if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Get the movie ID passed as command line argument
const movieId = process.argv[2];

// Construct the API URL for the given movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
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
  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      // Check for request error
      if (error) {
        console.error('Error:', error);
        return;
      }

      // Check if the response status code indicates a successful request
      if (response.statusCode !== 200) {
        console.error('Failed to fetch character:', response.statusCode);
        return;
      }

      // Parse the character API response
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
