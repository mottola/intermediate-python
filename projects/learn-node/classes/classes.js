'use strict';

var EventEmitter = require('events');

var Greetr = require('./greetr');

var greeter1 = new Greetr();

greeter1.('greet', function (data) {
    console.log('Someone greeted!' + data);
});

greeter1.greet('Tony');


