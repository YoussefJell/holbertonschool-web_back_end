export default function signUpUser(firstName, lastName) {
  return Promise.resolve({'firstname': firstName,
  'lastname': lastName});
}
