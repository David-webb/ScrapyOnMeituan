page = require('webpage').create();
page.open(
	'http://nj.meituan.com/category/meishi?mtt=1.index%2Ffloornew.nc.1.ilvprxya', 
	function(status) 
	{
    		var title = page.evaluate
    		(
    			function(s) {return document.querySelector(s).innerText;} ,
    			'title'
    		);
    		setTimeout(function(){console.log(title)},1000);
    		console.log('1 sec over');
    		setTimeout(console.log(title),1000);
    		console.log('2 sec over');
    		phantom.exit();
    	}
    );



