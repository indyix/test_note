package com.lemon.auto.ios.driver.command_02_excuteScript;

import java.net.URL;
import java.util.HashMap;
import java.util.Map;

import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;

public class ExcuteTester {
	public static void main(String[] args) throws Exception {
		// 期望的能力对象
		DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
		// 平台名
		desiredCapabilities.setCapability("platformName", "iOS");
		// 平台版本
		desiredCapabilities.setCapability("platformVersion", "13.1");
		// app文件的路径
		desiredCapabilities.setCapability("app", "/Users/nick/Desktop/tools/app/UICatalog.app");
		// 设备名
		desiredCapabilities.setCapability("deviceName", "iPhone 8");
		// 创建一个会话
		URL remoteAddress = new URL("http://localhost:4723/wd/hub");
		IOSDriver<IOSElement> driver = new IOSDriver<IOSElement>(remoteAddress, desiredCapabilities);
		
		Map<String, Object> params = new HashMap<String, Object>();
		params.put("direction", "down");
		driver.executeScript("mobile: scroll", params); 

		
		Thread.sleep(3000);
		driver.quit();

	}

}
