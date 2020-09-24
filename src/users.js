'use strict';
import './base.js';

// elm
var Elm = require('./Users.elm').Elm;

var app = Elm.Users.init({
    node: document.getElementById('users')
});
