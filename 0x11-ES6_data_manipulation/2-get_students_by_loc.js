export default function getStudentsByLocation(list, city) {
  return list.filter((elem) => elem.location === city);
}
