const request = require('request');

function getMovieCharacters(movieId) {
  const filmUrl = `https://swapi-api.alx-tools.com/films/${movieId}`;

  return new Promise((resolve, reject) => {
    request.get(filmUrl, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        console.error("Failed to retrieve movie data from SWAPI.");
        reject(error);
      } else {
        const filmData = JSON.parse(body);
        const characters = filmData.characters;

        const characterPromises = characters.map(characterUrl => {
          return new Promise((resolve, reject) => {
            request.get(characterUrl, (error, response, body) => {
              if (error || response.statusCode !== 200) {
                console.error(`Failed to retrieve character data from ${characterUrl}.`);
                reject(error);
              } else {
                const characterData = JSON.parse(body);
                resolve(characterData.name);
              }
            });
          });
        });

        Promise.all(characterPromises)
          .then(characterNames => resolve(characterNames))
          .catch(error => reject(error));
      }
    });
  });
}

// Get the movie ID from the command-line argument
const movieId = process.argv[2];

// Check if movieId is provided
if (!movieId) {
  console.error("Please provide a movie ID as a command-line argument.");
} else {
  getMovieCharacters(movieId)
    .then(characters => {
      if (characters) {
        characters.forEach(character => {
          console.log(character);
        });
      }
    })
    .catch(error => {
      console.error("Error:", error);
    });
}
