const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n');
      const studentsLines = lines.slice(1).filter((line) => line.trim() !== '');

      const fields = {};

      for (const line of studentsLines) {
        const parts = line.split(',');
        const firstName = parts[0];
        const field = parts[3];

        if (!fields[field]) {
          fields[field] = { count: 0, names: [] };
        }

        fields[field].count += 1;
        fields[field].names.push(firstName);
      }

      console.log(`Number of students: ${studentsLines.length}`);

      for (const [field, info] of Object.entries(fields)) {
        console.log(
          `Number of students in ${field}: ${info.count}. List: ${info.names.join(', ')}`
        );
      }

      resolve();
    });
  });
}

module.exports = countStudents;
