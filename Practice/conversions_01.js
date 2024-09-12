// Integer
let score = 33;
// console.log(typeof score);

// COnvert to string
let valueInNumber = Number(score);
// console.log(typeof(valueInNumber));

// "33" => 33
// "33abc" => NaN
// True => 1
 // 1 => true
 // 0 => false
 // "" => 0
 // "abc" =>false

 ////////////////////////////////operations////////////////////////////////
//console.log( 3+3);
// console.log( 3-3);
// console.log( 3*3);
// console.log( 3/3);
// console.log( 3%3);
// console.log( 3**3); // gives power of 3

/************************** Tricky conversions ************************************** */

console.log("1" + 2); //gives 12 as string
console.log(1 + "2"); //gives 12 as string
console.log(1 + "2" + 3);//gives 123 as string
console.log(1 + 2 + "3") //gives 33 as string
//pls dont write this type of code 

console.log(+true);//gives 1
console.log(+false);//gives 0
console.log(+"");//gives 0

// again dont write this type of code

console.log(null > 0); //false
console.log(null == 0); //false
console.log(null >= 0); //true 
//In these examples js converts null to 0 and then compares them
//always compare with the same datatype
//=== checks the value as well as datatype 