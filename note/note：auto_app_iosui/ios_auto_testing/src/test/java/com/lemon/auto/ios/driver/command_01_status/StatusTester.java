package com.lemon.auto.ios.driver.command_01_status;

import java.net.URL;
import java.util.HashMap;
import java.util.Map;

import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.SessionId;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.ios.IOSElement;

public class StatusTester {
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
		
		//1:创建会话
		IOSDriver<IOSElement> driver = new IOSDriver<IOSElement>(remoteAddress, desiredCapabilities);
		
		Map<String, Object> infoMap = driver.getStatus();
		System.out.println(infoMap);

		Thread.sleep(3000);
//		driver.quit();

	}

}
