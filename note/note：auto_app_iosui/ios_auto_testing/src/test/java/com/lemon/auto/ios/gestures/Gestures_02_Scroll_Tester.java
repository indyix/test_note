package com.lemon.auto.ios.gestures;

import java.net.URL;
import java.util.HashMap;
import java.util.Map;

import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;

public class Gestures_02_Scroll_Tester {
	public static void main(String[] args) throws Exception {
		// 期望的能力对象
		DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
		// 平台名
		desiredCapabilities.setCapability("platformName", "iOS");
		// 平台版本
		desiredCapabilities.setCapability("platformVersion", "12.1");
		// app文件的路径
		desiredCapabilities.setCapability("app", "/Users/happy/Desktop/tools/app/UICatalog.app");
		// 设备名
		desiredCapabilities.setCapability("deviceName", "iPhone 8");
		// 是否重置app设置
		desiredCapabilities.setCapability("noReset", true);
		// 创建一个会话
		URL remoteAddress = new URL("http://localhost:4723/wd/hub");
		IOSDriver<IOSElement> driver = new IOSDriver<IOSElement>(remoteAddress, desiredCapabilities);
		/**
		 * mobile: scroll
		 * 备注
			滑动元素或整个屏幕。支持不同的滑动策略。该方法提供了4种滑动策略：“name”，“direction”，“predicateString”或“toVisible”。4种滑动策略都是排他性的，一次滑动只能选择一个策略。可使用mobile:scroll来对表格中或者集合视图中的某个已知控件进行精确的滚动操作
			参数
			element 
			需要滚动的控件ID，缺省将使用App的控件
			name 
			需要执行滚动的子控件的accessibility id。 将predicateString参数设置为“name == accessibilityId”可以实现相同的结果。如果element不是容器，则不起作用
			direction
			'up', 'down', 'left' or 'right'. 该参数与swipe中的比，差别在于scroll会尝试将当前界面完全移动到下一页
			predicateString
			需要被执行滚动操作的子控件的NSPredicate定位器。如果控件不是容器，则不起作用
			toVisible
			布尔类型的参数。如果设置为true，则表示要求滚动到父控件中的第一个可见到的子控件。如果element未设置，则不生效
			示例
			# Python 
			driver.execute_script('mobile: scroll', {'direction': 'down'});

		 */
		
		Thread.sleep(2000);
		Map<String,Object> params = new HashMap<String, Object>();
		params.put("direction", "down");
		driver.executeScript("mobile: scroll", params);
//		Thread.sleep(3000);
//		driver.quit();

	}

}
