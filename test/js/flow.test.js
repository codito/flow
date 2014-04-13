//var assert = require("assert")
//describe('Array', function(){
  //describe('#indexOf()', function(){
    //it('should return -1 when the value is not present', function(){
      //assert.equal(-1, [1,2,3].indexOf(5));
      //assert.equal(-1, [1,2,3].indexOf(0));
    //})
  //})
//});

function ok(expr, msg) {
  if (!expr) throw new Error(msg);
}

mocha.setup('qunit');

suite('Array');

test('#length', function(){
  var arr = [1,2,3];
  ok(arr.length == 3);
});

test("Sample test", function() {
    // Assertions
    expect(1);

    ok(true, "passes because true is true");
});
