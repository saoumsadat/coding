const express = require('express');
const app = express();
const port = 8080;
// console.dir(app);

// app.use((req, res) => {
//     console.log("Got new request");
//     res.send("<h1>Here is your response bogo bogo</h1>");
// })

app.get("/", (req, res) => {
    res.send("<h1>Home Page</h1>");
})
app.get("/r/:sub", (req, res) => {
    console.log(req.params);
    const { sub } = req.params;
    res.send(`You are browsing the ${sub} subreddit`);
})
app.get("/r/:sub/:id", (req, res) => {
    console.log(req.params);
    const { sub, id } = req.params;
    res.send(`Viewing Post ID: ${id} on the ${sub} subreddit`);
})
app.get("/search", (req, res) => {
    console.log(req.query);
    if (!(Object.keys(req.query).length)) {
        res.send("idiot");
    }
    const { type, color } = req.query;
    res.send(`Searching for ${color} colored ${type} type`);
})

app.get('*', (req, res) => {
    res.send("Can't find");
})

app.listen(port, () => {
    console.log("Listening on port", port);
})