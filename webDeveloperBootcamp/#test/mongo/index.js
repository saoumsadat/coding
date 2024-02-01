const mongoose = require('mongoose');
mongoose.connect('mongodb://127.0.0.1:27017/movieApp')
  .then(() => {
    console.log("CONNECTION ESTABLISHED")
  })
  .catch((e) => {
    console.log("ERROR")
    console.log(e)
  })

const movieSchema = new Schema({
  title: String,
  year: Number,
  score: Number,
  isGood: Boolean
})

const Movie = mongoose.model('Movie', movieSchema)
const bestMovie = new Movie({title: 'Bogo', year: 2025, score: 10.99, isGood: true})