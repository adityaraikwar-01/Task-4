// Simulated heavy third-party/analytics script loaded synchronously in <head>
function busyWait(ms) { var s = Date.now(); while (Date.now() - s < ms) {} }
busyWait(350); // blocks the main thread
window.trackEvent = function (name) { console.log("event:", name); };
trackEvent("page_load");
