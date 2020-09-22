#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let countOccurences = 0;
  for (let i = 0, j = list.length - 1; i <= list.length / 2, j >= list.length / 2; i++, j--) {
    if (list[i] === searchElement || list[j] === searchElement) {
      countOccurences++;
    }
    if (list[i] === list[j] && list[i] === searchElement) {
      countOccurences++;
    }
  }
  return countOccurences;
};
