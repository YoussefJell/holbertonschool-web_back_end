export default function cleanSet(set, startString) {
  let res = '';
  if (!startString || !startString.length) {
    return res;
  }
  set.forEach((i) => {
    if (i && i.startsWith(startString)) {
      res += `${i.slice(startString.length)}-`
    };
  });
  res = res.slice(0, res.length - 1)
  return res;
}
