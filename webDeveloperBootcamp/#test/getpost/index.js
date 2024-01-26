const express = require('express');
const app = express();

app.use(express.urlencoded({ extended: true }));

app.get('/tacos', (req, res) => {
  console.log(req.query);
  res.send('GET /tacos response found');
})

app.post('/tacos', (req, res) => {
  console.log(req.body);
  res.send('POST /tacos response found');
})

app.listen(3000, () => {
  console.log('listening on port 3000');
})