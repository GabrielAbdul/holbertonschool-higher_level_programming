#!/usr/bin/node

exports.converter = function (base) {
	return function (string) {
		return string.toString(base);
	}
};
