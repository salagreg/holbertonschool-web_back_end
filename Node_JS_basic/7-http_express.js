const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.type('text/plain');
  res.write('This is the list of our students\n');

  const database = process.argv[2];

  countStudents(database)
    .then((output) => {
      res.end(output);
    })
    .catch((error) => {
      res.end(error.message);
    });
});

app.listen(port);

module.exports = app;
