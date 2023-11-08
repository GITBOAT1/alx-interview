const axios = require('axios');

// Define the base URL for the Star Wars API
const baseUrl = 'https://swapi.dev/api';

// Function to fetch movie details using the provided Movie ID
async function getMovieCharacters(movieId) {
  try {
    // Make a request to fetch movie details
    const movieUrl = `${baseUrl}/films/${movieId}/`;
    const movieResponse = await axios.get(movieUrl);

    if (movieResponse.status === 200) {
      const movieData = movieResponse.data;
      const characterUrls = movieData.characters;
      return characterUrls;
    } else {
      console.log(`Failed to fetch movie details. Status code: ${movieResponse.status}`);
      return null;
    }
  } catch (error) {
    console.error(`Request error: ${error.message}`);
    return null;
  }
}

// Function to fetch and print character names
async function printCharacterNames(characterUrls) {
  for (const characterUrl of characterUrls) {
    try {
      const characterResponse = await axios.get(characterUrl);
      if (characterResponse.status === 200) {
        const characterData = characterResponse.data;
        console.log(characterData.name);
      } else {
        console.log(`Failed to fetch character details. Status code: ${characterResponse.status}`);
      }
    } catch (error) {
      console.error(`Request error: ${error.message}`);
    }
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
