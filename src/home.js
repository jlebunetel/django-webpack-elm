'use strict';
import './base.js';

// elm
var Elm = require('./Main.elm').Elm;

var app = Elm.Main.init({
    node: document.getElementById('home')
});
