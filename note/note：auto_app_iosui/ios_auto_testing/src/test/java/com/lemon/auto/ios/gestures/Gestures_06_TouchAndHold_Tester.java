package com.lemon.auto.ios.gestures;

import java.net.URL;
import java.util.HashMap;
import java.util.Map;

import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;
import io.appium.java_client.remote.MobileBrowserType;
import io.appium.java_client.remote.MobileCapabilityType;

public class Gestures_06_TouchAndHold_Tester {
	/**
	 命令
		mobile: touchAndHold
		备注
		在指定控件上或屏幕上长按的手势操作
		参数
		element 
		需要长按的控件ID（十六进制哈希字符串）。如果没有提供该参数的话，则会使用App的控件作为替代
		duration
		长按的持续时间（秒），浮点型。强制性参数
		x 
		屏幕x轴坐标点，浮点型. 仅当element未设置时才是强制参数
		y
		屏幕y轴坐标点，浮点型. 仅当element未设置时才是强制参数
		示例
		// c# 
		Dictionary<string, object> tfLongTap = new Dictionary<string, object>(); 
		tfLongTap.Add("element", element.Id); 
		tfLongTap.Add("duration", 2.0); 
		((IJavaScriptExecutor)driver).ExecuteScript("mobile: touchAndHold", tfLongTap); 

	 * @param args
	 * @throws Exception
	 */
	public static void main(String[] args) throws Exception {
		// 期望的能力对象
		DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
		// 平台名
		desiredCapabilities.setCapability("platformName", "iOS");
		// 平台版本
		desiredCapabilities.setCapability("platformVersion", "12.1");
		// app文件的路径
		desiredCapabilities.setCapability(MobileCapabilityType.BROWSER_NAME, MobileBrowserType.SAFARI);
		
		// 设备名
		desiredCapabilities.setCapability("deviceName", "iPhone 8");
		// 是否重置app设置
		desiredCapabilities.setCapability("noReset", true);
		// 创建一个会话
		URL remoteAddress = new URL("http://localhost:4723/wd/hub");
		IOSDriver<IOSElement> driver = new IOSDriver<IOSElement>(remoteAddress, desiredCapabilities);
		
		driver.get("https://www.baidu.com");
		Thread.sleep(2000);
		Map<String,Object> params = new HashMap<String, Object>();
		params.put("duration", 2.0);
		params.put("x", 184.0);
		params.put("y", 164.0);
		driver.executeScript("mobile: touchAndHold", params);
//		Thread.sleep(3000);
//		driver.quit();

	}

}
