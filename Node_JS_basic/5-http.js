const http = require('http');
const countStudents = require('./3-read_file_async');

const port = 1245;

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.statusCode = 200;
    res.write('This is the list of our students\n');

    const database = process.argv[2];

    countStudents(database)
      .then((output) => {
        res.end(output);
      })
      .catch((error) => {
        res.end(error.message);
      });
  } else {
    res.statusCode = 404;
    res.end();
  }
});

app.listen(port);

module.exports = app;
