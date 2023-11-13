#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let i_ = 0; i_ < x; i++) theFunction();
};
