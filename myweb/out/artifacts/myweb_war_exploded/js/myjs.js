//严格检查模式，必须写在第一行
'use strict';

// 数据类型
// 数、字符串、布尔值、数组、对象
let i = 1;

/**
 * 字符串
 * 1、正常字符串 用单引号，或者双引号
 * 2、转义字符 \
 * 3、多行字符串编写 用 ·· tab键上面
 * 4、支持模板字符串！！！ ${}
 * 5、可以通过下标像数组一样访问，但是不可以改变
 * 6、字符串也有很多方法，像java
 * indexOf, substring, toUpperCase, toLowerCase...
 */
let str = "String"
console.log(str)
//第4条
let name = "curry";
let age = 4;
let meg = `hello, + ${name} + ${age}`;//!!!
console.log(meg)


/**
 * 数组
 * 1、数组可以包含任意数据类型，即使是混合的
 * 2、数组长度可以变长，多出来就是空的，undefine；也可以变短，元素丢失！！！
 * 3、数组的方法和java类似
 *      indexOf,
 *      1) slice() (类似于substring)
 *      2) push, pop 向数组最后面添加元素、弹出元素。
 *      3) unshift(), shift() 向头部添加元素、弹出元素
 *      4) sort() 排序  reverse() 反转
 *      5) concat() 拼接数组，返回新的数组，并不改变原数组
 *      6) join() 打印拼接数组
 * 4、多维数组
 * 5、数组的循环 forEach
 *
 */
let array = [1,2,3,4]
console.log(array)
// 5
array.forEach(function (value){
    console.log(value);
})
/**
 * 对象
 * 所有的键都是字符串，值是任意类型
 * 1、对象定义: 若干个键值对
 *      var 对象名 {
 *          属性名: 属性值,
 *          属性名: 属性值,
 *          属性名: 属性值
 *      }
 *      像 python 中的 字典
 * 2、不存在的对象属性，不会报错，undefine
 * 3、动态的删减属性 delete person.mvp ; 增加属性 直接进行赋值 person.mvp = 2;
 * 4、判断属性值是否在这个对象中 xxx in xxx  返回 布尔值
 * 5、判断一个属性是否是这个对象自身拥有的属性 hasOwnProperty()  !!! 键是字符串
 *
 */

let person = {
    name: "curry",
    age: 33,
    mvp: 2
}

delete person.mvp;
person.mvp = 2;
console.log(person.hasOwnProperty('age'));
console.log(person);

/**
 * 流程控制
 * 1、分支 if  else
 * 2、循环 for  while
 * 3、for(let index in array) 其中 index 只是索引
 * 4、for(let item of array) 其中 item 为元素
 */

for (let index in array){
    console.log(array[index])
}

/**
 * ES6 的新特性
 * Map 和 Set
 *
 */

let map = new Map([['curry',100],['james',99]]);  // python 中的 字典
console.log(map.get('curry'))
map.delete('james');
map.set('durant',80);

let set = new Set([1,1,4,3]);
set.add(5);
set.delete(1);
console.log(set.has(2));
console.log(map.get('curry'));


// let names = ['curry','james'];
// let scores = [100,99];

/**
 * ES6 新特性
 * iterator
 */
let arr = [3,4,5,6];
// arr.name = '123'  早期bug  for .. in .. 会打印出 name 其他仍为索引
//                           for .. of .. 不会打印出name
for (let item of arr){
    console.log(item);
}

for (let m of map){
    console.log(m);
}

for (let s of set){
    console.log(s);
}

/**
 * 函数
 * 1、定义函数 都用 function 定义
 * 2、像和变量一样去定义
 * 3、参数多和少都不报错
 * 4、argument 包含了所有的参数
 * 5、rest  ES6新特性   获取除了已经定义的参数之外的所有参数
 */

function abs1(x,...rest)
{
    if (typeof x !== 'number'){
        throw 'Not a Number';
    }

    console.log("x==>"+x)

    // for (let i = 0; i < arguments.length; ++i)
    //     console.log(arguments[i])
    console.log(rest)

    return x > 0 ? x : -1 * x;
}

let abs2 = function (x)
{
    return x > 0 ? x : -1 * x;
}

console.log(abs1(-100))

/**
 * 变量的作用域
 *
 * 全局变量要用  var 定义
 * 1、window 是全局对象 只有一个全局作用域 所有的全局变量都绑定到 window 上
 *      自己定义一个唯一的全局变量，降低全局命名冲突的库
 * 2、函数可以赋给变量
 *
 * 局部作用域
 * 引入 let 关键字
 *
 * 常量  const
 */
const t = '1234';
// alert(t);
// alert(window.t);

// 定义自己的全局命名空间
var global = {};


/**
 * 方法
 * 1、就是对象中的函数
 * 也可以拆开写，但是调用的时候，那个函数不能单独调
 * 2、apply  在 js 中可以控制 this 的指向
 * 就是拆开写，函数单独调用的时候用apply来指向对象
 */
let zheng = {
    name: "curry",
    birthday: 2020,
    three: 2960,
    // 方法
    age: function () {
        let now = new Date().getFullYear();
        return now - this.birthday
    },
    three_balls: cal
};

function cal(){
    return this.three;
}

cal.apply(zheng,[]);


/**
 * 内部对象
 * 1、标准对象
 * typeof 123 --> 'number'
 *
 * 2、Data 对象
 *
 * 3、JSON 对象
 */

let date = new Date();
date.getFullYear(); // 年
date.getMonth();  // 月
date.getDate();  // 日
date.getDay(); //星期几
date.getHours();  // 时
date.getMinutes();  // 分钟
date.getSeconds();  // 秒
date.getTime(); //时间戳

console.log(new Date(date.getTime())); // 时间戳转时间


/**
* JSON 对象
* 在 javaScript 中一切都是对象，任何 js 支持的类型都可以用 JSON 来表示
*  对象 {}
*  数组 []
*  所有键值对都是用 kry:value
*/

let j = {
    name:"durant",
    age:33,
    sex:"男"
};

// 对象 转换为 json 字符串
let json = JSON.stringify(j);

// json 字符串转成 对象
let obj = JSON.parse('{"name":"durant","age":3,"sex":"男"}')


/**
 * 面向对象编程
 * 原型  __proto__
 * class 继承 和 java 中的类一样
 * ES6 引入
 */

// 原型对象

let player = {
    name: "curry",
    age:32,
    play: function (){
        console.log(this.name + "play");
    }
};

let me = {
    name:"zhenghanchao"
};

me.__proto__ = player;

//==============================================
// 类对象

class NBA_PLAYER{

    constructor(name){
        this.name = name;
    }

    hello(){
        console.log(this.name + "hello");
    }
}

let zhen = new NBA_PLAYER("durant")
zhen.hello();

class GSW_PLAYER extends NBA_PLAYER{
    constructor(name) {
        super(name);
    }
    hello() {
        console.log("GSW's " + this.name + " hello");
    }
}

zhen = new GSW_PLAYER("james");
zhen.hello();


/**
 * 操作 BOM
 * BOM : 浏览器对象模型
 * js的诞生就是为了让他在浏览器中运行
 * 操作浏览器
 *
 * 1、window对象 代表浏览器窗口
 *
 * 2、Navigator 封装了浏览器的信息
 * 包括 userAgent
 * 不建议使用 Navigator 对象
 * 因为会被认为修改
 * 不建议使用这些属性来判断和编写代码
 *
 * 3、screen 获取当前屏幕的信息
 *
 * 4、location 代表当前页面的URL信息（重要）
 *
 * location.assign(url) 设置新的地址并跳转
 *
 * 5、document 代表当前的页面 HTML DOM 文档树
 * document.title
 *
 * 获取具体的文档树节点
 *
 * 获取cookie
 *
 * 6.history 代表浏览器的历史记录
 *
 * history.back()
 * history.forward()
 */

/**
 * DOM
 * DOM: 文档对象模型
 * 核心
 * 浏览器就是一个DOM树形结构
 * 1.更新：
 *
 * 2.遍历：get...这样的方法根据id或class来获取元素
 *
 * 3.删除：先获取父节点，再通过父节点删除自己
 * removeChild
 *
 * 4.添加：
 * 追加  appendChild()
 * 创建  creatElement()
 * innerHTML() 适用于空的 DOM 节点
 * 如果原本DOM节点就有元素,就会被覆盖
 * 先获得一个DOM节点
 */


/**
 * 表单  form   DOM树
 * 文本框、单选框、多选框
 *
 * 提交表单
 *
 */


