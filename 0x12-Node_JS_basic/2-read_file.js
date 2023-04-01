const fs = require('fs');

module.exports = function countStudents(filename) {
  fs.readFile(filename, 'utf8', (err, data) => {
    if (err) {
      throw new Error('Cannot load the database');
    }
    console.log(data.split('\n').filter((e) => e).length - 1);
  });
}
