// page = require('webpage').create();
// page.open( "http://nj.meituan.com/category/meishi?mtt=1.index%2Ffloornew.nc.1.ilvprxya",
// 	function(status) {
// 		        page.evaluate(function(){
// 		        	window.document.body.scrollTop = document.body.scrollHeight;

// 		        	// window.document.body.scrollTop = document.body.scrollHeight;
// 		        	// setTimeout(console.log('wait for sec POST'), 2000)
// 		        });
// 		        setTimeout(console.log('wait for first POST'), 6000)
// 		        page.render('bild.png')
// 	        	        console.log('picture is ready!')
// 	        	        phantom.exit()
//     	}
//     )


var page = require('webpage').create();
var url = 'http://nj.meituan.com/category/meishi?mtt=1.index%2Ffloornew.nc.1.ilvprxya';
page.open(url, function (status)
{
    if (status != "success")
    {
        console.log('FAIL to load the address');
        phantom.exit();
    }

   var  t = page.evaluate(function()
    {
        //此函数在目标页面执行的，上下文环境非本phantomjs，所以不能用到这个js中其他变量
       // window.scrollTo(0,10000);//滚动到底部
        window.document.body.scrollTop = document.body.scrollHeight;
        return 'trdy'
        // window.setTimeout(function()
        // {
        //     var plist = document.querySelectorAll("a");
        //     var len = plist.length;
        //     while(len)
        //     {
        //         len--;
        //         var el = plist[len];
        //         el.style.border = "1px solid red";
        //     }
        // },5000);
    });

    window.setTimeout(function ()
    {
        // page.render("json2form.png");
        console.log(t);
        phantom.exit();
    }, 5000+500);


});
