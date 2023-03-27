export default function getStudentsByLocation(list) {
  return list.reduce((accumulator, i) => accumulator + i.id, 0);
}
