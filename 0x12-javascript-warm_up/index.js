#!/usr/bin/node
const dic = [
    { id: 1, name: 'John', age: 24 },
    { id: 2, name: 'Paul', age: 26 },
    { id: 3, name: 'George', age: 22 },
    { id: 4, name: 'Ringo', age: 27 }

]

const { add } = require("./13-add");
const person = dic.find((person) => person.id === 2);

console.log(add(dic[1]['id'], dic[3]['id']));
