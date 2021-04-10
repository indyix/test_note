package com.lemon.auto.ios.gestures;

import java.net.URL;
import java.util.HashMap;
import java.util.Map;

import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;
import io.appium.java_client.remote.MobileBrowserType;
import io.appium.java_client.remote.MobileCapabilityType;

public class Gestures_03_Pinch_Tester {
	public static void main(String[] args) throws Exception {
		// 期望的能力对象
		DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
		// 平台名
		desiredCapabilities.setCapability("platformName", "iOS");
		// 平台版本
		desiredCapabilities.setCapability("platformVersion", "12.1");
		// app文件的路径
//		desiredCapabilities.setCapability("app", "/Users/happy/Desktop/tools/app/UICatalog.app");
		desiredCapabilities.setCapability(MobileCapabilityType.BROWSER_NAME, MobileBrowserType.SAFARI);
		
		// 设备名
		desiredCapabilities.setCapability("deviceName", "iPhone 8");
		// 是否重置app设置
		desiredCapabilities.setCapability("noReset", true);
		// 创建一个会话
		URL remoteAddress = new URL("http://localhost:4723/wd/hub");
		IOSDriver<IOSElement> driver = new IOSDriver<IOSElement>(remoteAddress, desiredCapabilities);
		
		driver.get("https://www.baidu.com/img/bd_logo1.png");
		/**
		 * 命令
		mobile: pinch
		备注
		在给定的控件或应用程序控件上执行捏合手势
		参数
		element 
		需要捏合的控件ID（作为十六进制哈希字符串）。如果没有提供该参数的话，则会使用App的控件作为替代
		scale 
		浮点型，使用0和1之间的比例来“捏紧”或缩小，大于1的比例“撑开”或放大
		强制参数
		velocity
		每秒缩放速度（浮点值）
		强制参数
		示例
		# Ruby 
		execute_script 'mobile: pinch', scale: 0.5, velocity: 1.1, element: element.ref
		 */
		
		Thread.sleep(2000);
		Map<String,Object> params = new HashMap<String, Object>();
		params.put("scale", 0.5);
		params.put("velocity", -2.0);//velocity must be less than zero when scale is less than 1
		driver.executeScript("mobile: pinch", params);
//		Thread.sleep(3000);
//		driver.quit();

	}

}
