export default function getListStudentIds(students) {
  if(!Array.isArray(students)) {
    return [];
  }
  return students.map((args) => args.id);
}
