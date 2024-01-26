const express = require('express');
const app = express();
const port = 3000;
const path = require('path'); //built in module to work with directory

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '/views')); //finds views in the folder of index.js regardless of where it is being executed from

app.get('/', (req, res) => {
  console.log("New request from home page");
  // res.send("<h1>Home Page</h1>");
  res.render('home.ejs');
})

//generate randome number
app.get('/rand', (req, res) => {
  const num = Math.floor((Math.random()) * 10) + 1;
  res.render('random', { num });  //2nd argument --> pass variable to ejs file --> {num : num}
})

//my friends
app.get('/ds', (req, res) => {
  const friends = ['bogo', 'loneliness', 'abedu', 'depression'];
  res.render('friends', { friends });
})

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
})