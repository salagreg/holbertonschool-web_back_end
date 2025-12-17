export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString.length === 0) {
    return '';
  }

  const resultArray = [];
  for (const item of set) {
    if (item.startsWith(startString)) {
      resultArray.push(item.slice(startString.length));
    }
  }

  return resultArray.join('-');
}
