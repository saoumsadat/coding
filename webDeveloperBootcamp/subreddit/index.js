const express = require('express');
const app = express();
const port = 3000;
const path = require('path');
const redditData = require('./data.json');
console.log(redditData);

//serving static files
app.use(express.static(path.join(__dirname, 'public')));

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');


app.get('/', (req, res) => {
  res.render('home');
  // console.log('got request');
})

app.get('/r/:sub', (req, res) => {
  const { sub } = req.params;
  const data = redditData[sub];
  console.log(data);

  if (data) {
    res.render('subreddit', { ...data });
  } else {
    res.render('notfound', { sub })
  }

})

app.get('/rand', (req, res) => {
  const randNum = Math.floor(Math.random() * 50) + 1;
  res.render('rand', { num: randNum });
})

app.listen(port, () => {
  console.log("Listening on port", port);
})