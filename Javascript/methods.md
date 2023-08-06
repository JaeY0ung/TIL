# Methods

```javascript
const user = {
    name : 'mike',
    age : 30,
    gender : 'male'.
}
```
### Object.assign() : 객체 복사
```javascript
const user2 = Object.assign({}, user)
```

### Object.keys() : 키 값만 반환
```javascript 
Object.keys(user)
```

### Object.values() : value 값만 반환
```javascript 
Object.values(user)
```

### Object.entries() : 키, value 값 모두 반환 (2차원 배열 형태로)
```javascript 
Object.entries(user)
```

### Object.fromEntries() : 2차원 배열 형태를 입력하면 객체로 반환
```javascript 
const arr = [
    ["name","Mike"],
    ["age", 30],
    ["gender", "male"]
];

Object.fromEntries(arr)
```



## 문자열 Methods
```javascript 
let desc = "Hi guys. Nice to meet you."

desc.toUpperCase();
desc.toLowerCase();
desc.indexOf('to'); // 14
desc.indexOf('man'); // -1
desc.substring(0,5); // Hi gu
desc.substring(5,0); // Hi gu
desc.substr(5,5); // ys. N
desc.trim(); // 앞 뒤 공백 제거
desc.repeat(2); // 문자열 2번 반복

1 < 3 //true
"a" < "c" // true
"a".codePointAt(0); // 97 (아스키코드)
String.fromCodePoint(97); // "a"
```