var age = 26;
const birthArea = 'seoul';

var 예금액 = 60000;
var 미래예금액 = 0;

if(예금액<50000){
    미래예금액 = 예금액 * (1.15)**2;
}else{
    미래예금액 = 예금액 * (1.2)**2;
}

console.log(미래예금액);

var first = 360;

console.log(first*19/9)