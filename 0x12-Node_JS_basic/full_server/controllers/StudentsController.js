import readDatabase from '../utils';

export default class StudentController {

  static getAllStudents(request, response, path) {
    response.set('Content-Type', 'text/html');
    readDatabase(path)
      .then((data) => {
        let resp = [];
        resp.push('This is the list of our students');
        for (const key of Object.keys(data)) {
          console.log(data);
          resp.push(`Number of students in ${key}: ${data[key].length}. List: ${data[key].join(', ')}`);
        }
        response.status(200).send(resp.join('\n'));
      })
      .catch((err) => {
        response.status(500).send(err.message);
      });

  }

  static getAllStudentsByMajor(request, response, path) {
    console.log(request.params);
    if (request.params.major != 'CS' && request.params.major != 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
    }
    response.set('Content-Type', 'text/html');
    readDatabase(path)
      .then((data) => {
        response.send(`List: ${data[request.params.major].join(', ')}`);
        response.status(200).end();
      })
      .catch((err) => {
        response.status(500).send(err.message);
      });
  }
}
