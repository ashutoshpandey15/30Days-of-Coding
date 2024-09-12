// beginning of the revision of js from scratch
const ashu = "Ashu";     //value remians constant cannot be changed
let myName = "Ashu";    //another way of declaring variable but mostly used because of scope
var myAdd = "Address";  //most common way to declare the variable (not used cause of block and function scope)
let myName1 ;  // variale declared but not initialized hence => undefined
console.table({ashu, myName, myAdd , myName1}); // to consolelog in table format


// "use strict" this treats the JS code as newwe version of JS.

// Data types in js
// Primitive data types
// 1. String
let name = "ashu";
let age = 18
let islogged = false
console.table({name,age,islogged})
// 2. Number => int , float
// 3. Boolean
// 4. Null=> standalone value / representation of empty value.(special type)
// 5. Undefined => when the value is not defined
// 6.bigint = to store large numbers
// 7.symbol => used to identify unique 
// 8. object => key value pair

//typeof=> gives the type of the variable
console.log(typeof name)
console.log(typeof null) // null is an object
console.log(typeof undefined)