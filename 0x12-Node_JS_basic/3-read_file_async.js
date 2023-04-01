const fs = require('fs');

module.exports = async function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }
      let response = '';
      const csv = data.toString().split('\n');
      const students = csv.filter((item) => item)
        .map((item) => item.split(','));
      students.shift();
      const studentAmnt = students.length ? students.length : 0;
      console.log(`Number of students: ${studentAmnt}`);
      response += `Number of students: ${studentAmnt}\n`;

      const fields = {};
      for (let i = 0; i < students.length; i += 1) {
        if (!fields[students[i][3]]) fields[students[i][3]] = [];
        fields[students[i][3]].push(students[i][0]);
      }

      for (const key of Object.keys(fields)) {
        console.log(`Number of students in ${key}: ${fields[key].length}. List: ${fields[key].join(', ')}`);
        response += `Number of students in ${key}: ${fields[key].length}. List: ${fields[key].join(', ')}\n`;
      }
      resolve(response);
    });
  });
};
