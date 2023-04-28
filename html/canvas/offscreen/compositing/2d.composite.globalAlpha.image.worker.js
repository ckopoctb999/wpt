// DO NOT EDIT! This test has been generated by /html/canvas/tools/gentest.py.
// OffscreenCanvas test in a worker:2d.composite.globalAlpha.image
// Description:
// Note:

importScripts("/resources/testharness.js");
importScripts("/html/canvas/resources/canvas-tests.js");

promise_test(async t => {

  var canvas = new OffscreenCanvas(100, 50);
  var ctx = canvas.getContext('2d');

  ctx.fillStyle = '#0f0';
  ctx.fillRect(0, 0, 100, 50);
  // Avoiding any potential alpha = 0 optimisations.
  ctx.globalAlpha = 0.01;
  const response = await fetch('/images/red.png');
  const blob = await response.blob();
  const bitmap = await createImageBitmap(blob);

  ctx.drawImage(bitmap, 0, 0);
  _assertPixelApprox(canvas, 50,25, 2,253,0,255, 2);
  t.done();
}, "");
done();
