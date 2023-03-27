export default function updateStudentGradeByCity(listOfStudents, city, newGrades) {
  return listOfStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const gradeFilter = newGrades.filter(
        (newGrade) => newGrade.studentId === student.id,
      );

      let grade = gradeFilter[0] ? gradeFilter[0].grade : 'N/A';

      return {
        ...student,
        grade,
      };
    });
}
