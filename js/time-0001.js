function time(){//时间函数
	var date=new Date();//创建时间对象
	
	var years = date.getFullYear();//获取此刻年份
	
	var month = date.getMonth()+1;
	month = month<10?"0"+month:month;//获取此刻月份
	
	var day=date.getDate();
	day = day<10?"0"+day:day;//获取此刻几号
	
	var week = date.getDay();

	//var week="日一二三四五六".charAt(date.getDay());//获取此刻周几
	
	//根据id="time"获取span标签并调用innerHTML方法为标签内添加内容
	document.getElementById("ga-time-day").innerHTML = "今天是"+years+"年"+month+"月"+day+"日";
	document.getElementById("ga-time-week").innerHTML = " "+week;
	//添加时间信息
}