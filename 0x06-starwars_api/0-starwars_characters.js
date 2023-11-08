const request = require('request');

// Define the base URL for the Star Wars API
const baseUrl = 'https://swapi.dev/api';

// Function to fetch movie details using the provided Movie ID
function getMovieCharacters (movieId) {
  return new Promise((resolve, reject) => {
    // Make a request to fetch movie details
    const movieUrl = `${baseUrl}/films/${movieId}/`;
    request(movieUrl, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const movieData = JSON.parse(body);
        const characterUrls = movieData.characters;
        resolve(characterUrls);
      } else {
        reject(`Failed to fetch movie details. Status code: ${response ? response.statusCode : 'N/A'}`);
      }
    });
  });
}

// Function to fetch and print character names
function printCharacterNames (characterUrls) {
  for (const characterUrl of characterUrls) {
    request(characterUrl, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      } else {
        console.log(`Failed to fetch character details. Status code: ${response ? response.statusCode : 'N/A'}`);
      }
    });
  }
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <Movie ID>');
} else {
  const movieId = process.argv[2];
  getMovieCharacters(movieId)
    .then((characterUrls) => {
      if (characterUrls) {
        printCharacterNames(characterUrls);
      }
    })
    .catch((error) => {
      console.error(error);
    });
}
