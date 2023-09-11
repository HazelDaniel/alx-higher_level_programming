#!/usr/bin/node

exports.callMeMoby = function (arg1, func) {
  for (let i_ = 0; i_ < arg1; i++) func();
};
