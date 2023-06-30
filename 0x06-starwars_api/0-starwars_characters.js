#!/usr/bin/node
/*
This script prints characters of a Star Wars movie using the Star Wars:
The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name per line in the same order as the “characters” list in the /films/ endpoint
You must use the Star wars API
You must use the request module
*
*/

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) throw error;

  if (response.statusCode === 200) {
    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;
    const characters = [];

    function fetchCharacterData (characterUrl) {
      return new Promise((resolve, reject) => {
        request(characterUrl, function (error, response, body) {
          if (error) {
            reject(error);
          } else if (response.statusCode === 200) {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          } else {
            reject(new Error(`Failed to fetch character data for ${characterUrl}`));
          }
        });
      });
    }

    async function fetchCharacters () {
      try {
        for (const characterUrl of characterUrls) {
          const characterName = await fetchCharacterData(characterUrl);
          characters.push(characterName);
        }

        console.log(characters.join('\n'));
      } catch (error) {
        console.log(error.message);
      }
    }

    fetchCharacters();
  } else {
    console.log(`Failed to fetch film data for Movie ID ${movieId}`);
  }
});
