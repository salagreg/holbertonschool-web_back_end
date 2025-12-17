export default function updateStudentGradeByCity(listStudents, city, newGrades) {
  if (!Array.isArray(listStudents) || typeof city !== 'string' || !Array.isArray(newGrades)) {
    return [];
  }

  return listStudents
    .filter(student => student.location === city)
    .map(student => {
      const gradeObj = newGrades.find(
        grade => grade.studentId === student.id
      );

      return {
        ...student,
        grade: gradeObj ? gradeObj.grade : 'N/A',
      };
    });
}
