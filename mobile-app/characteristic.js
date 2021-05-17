var bleno = require('bleno');
var util = require('util');
var fs = require('fs');

var BlenoCharacteristic = bleno.Characteristic;

var EchoCharacteristic = function() {
  EchoCharacteristic.super_.call(this, {
    uuid: 'e3754285-8072-458b-a45b-94a0dab36801',
    properties: ['read', 'write', 'notify'],
    value: null
  });

  this._value = new Buffer(0);
  this._updateValueCallback = null;
};

var scanFileTimer;

util.inherits(EchoCharacteristic, BlenoCharacteristic);

EchoCharacteristic.prototype.onReadRequest = function(offset, callback) {
  console.log('EchoCharacteristic - onReadRequest: value = ' + this._value.toString('hex'));

  callback(this.RESULT_SUCCESS, this._value);
};

EchoCharacteristic.prototype.onWriteRequest = function(data, offset, withoutResponse, callback) {
  this._value = data;

  console.log('EchoCharacteristic - onWriteRequest: value = ' + this._value.toString('hex'));

  if (this._updateValueCallback) {
    console.log('EchoCharacteristic - onWriteRequest: notifying');

    this._updateValueCallback(this._value);
  }

  callback(this.RESULT_SUCCESS);
};

EchoCharacteristic.prototype.onSubscribe = function(maxValueSize, updateValueCallback) {
  console.log("BLE server - connected to app");

  fs.writeFileSync("transfer.txt");
  
  scanFileTimer = setInterval(function() {
    var value = fs.readFileSync("transfer.txt").toString();
    if (value.includes("new") && value.length > 3) {
      value = value.replace("new","");
      fs.writeFileSync("transfer.txt", value, {encoding:'utf8',flag:'w'})
      updateValueCallback(new Buffer(value));
    };
  }, 200);

};

EchoCharacteristic.prototype.onUnsubscribe = function() {
  clearInterval(scanFileTimer)
  fs.unlinkSync("transfer.txt")
  console.log("BLE server - disconnected from app");

  this._updateValueCallback = null;
};

EchoCharacteristic.prototype.start = function() {
  console.log("started");
}

module.exports = EchoCharacteristic;
