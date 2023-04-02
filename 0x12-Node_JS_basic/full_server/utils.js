import e from 'express';

const fs = require('fs');

export default function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }
      else {
        const studentArr = {};
        const content = data.split('\n').filter((e) => e);
        for (let i = 1; i < content.length; i++) {
          const element = content[i].split(',');
          if (!studentArr[element[3]]) studentArr[element[3]] = [];
          studentArr[element[3]].push(element[0]);
        }
        resolve(studentArr);
      }
    });
  });
}
