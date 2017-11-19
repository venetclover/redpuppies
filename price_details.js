var page = require('webpage').create();
page.open('https://www.redfin.com/CA/San-Jose/1485-De-Rose-Way-95126/unit-118/home/729396', function(status) {
  console.log("Status: " + status);
  if(status === "success") {
    page.render('detail_page.png');
  }
  phantom.exit();
});
