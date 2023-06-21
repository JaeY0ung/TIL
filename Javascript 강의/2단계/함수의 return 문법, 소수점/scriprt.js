function 함수(){
    return 123;
}

function 함수(a){
    num =  (a * 1.1).toFixed(1); //! 반올림 : 문자열임
    return num;
}


function 함수(a){
    num =  (a * 1.1).toFixed(1);
    return parseFloat(num); //! 문자형을 숫자형으로 변환해주는 함수 : parseFloat()
}

//! 숙제
function tomillisecond(min,sec){
    var millis = (min*60+sec) * 1000;
    return millis;
}

console.log(tomillisecond(1,30));
console.log(tomillisecond(2,10));

function salePrice(originalPrice, isFirstBuy){
    var price = originalPrice * 0.9;
    if (isFirstBuy == true){
        price -= 1.5
    }
    return parseFloat(price.toFixed(1));
}

console.log(salePrice(70, false));
console.log(salePrice(10, true));