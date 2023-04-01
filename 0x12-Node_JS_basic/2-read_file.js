const fs = require('fs');

module.exports = function countStudents(filename) {
  let content;
  try {
    content = fs.readFileSync(filename);
  } catch (err) {
    throw new Error('Cannot load the database');
  }
  const studentArr = {};
  content = content.toString().split('\n').filter((e) => e);
  for (let i = 1; i < content.length; i += 1) {
    const element = content[i].split(',');
    if (!studentArr[element[3]]) studentArr[element[3]] = [];
    studentArr[element[3]].push(element[0]);
  }
  console.log(`Number of students: ${content.length - 1}`);
  for (const key of Object.keys(studentArr)) {
    console.log(`Number of students in ${key}: ${studentArr[key].length}. List: ${studentArr[key].join(', ')}`);
  }
};
